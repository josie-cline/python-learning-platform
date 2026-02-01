"""
Test Runner
Safely executes user code and runs test cases
"""

import sys
import io
import traceback
from typing import Dict, List, Any
import ast
import time


class TestRunner:
    """Safely runs user code and test cases"""
    
    def __init__(self):
        self.timeout = 5  # seconds
    
    def run_tests(self, user_code: str, test_cases: List[Dict]) -> Dict:
        """
        Run test cases against user code
        
        Args:
            user_code: The code submitted by the user
            test_cases: List of test case dictionaries
        
        Returns:
            Dictionary with test results
        """
        results = {
            'passed': False,
            'total_tests': len(test_cases),
            'passed_tests': 0,
            'failed_tests': 0,
            'test_results': [],
            'error': None,
            'execution_time': 0
        }
        
        # First, check if code is syntactically valid
        try:
            ast.parse(user_code)
        except SyntaxError as e:
            results['error'] = f"Syntax Error: {str(e)}"
            return results
        
        # Run each test case
        start_time = time.time()
        
        for i, test_case in enumerate(test_cases):
            test_result = self._run_single_test(user_code, test_case, i + 1)
            results['test_results'].append(test_result)
            
            if test_result['passed']:
                results['passed_tests'] += 1
            else:
                results['failed_tests'] += 1
        
        results['execution_time'] = time.time() - start_time
        results['passed'] = results['passed_tests'] == results['total_tests']
        
        return results
    
    def _run_single_test(self, user_code: str, test_case: Dict, test_num: int) -> Dict:
        """Run a single test case"""
        result = {
            'test_number': test_num,
            'description': test_case.get('description', f'Test {test_num}'),
            'passed': False,
            'expected': test_case.get('expected'),
            'actual': None,
            'error': None,
            'output': ''
        }
        
        try:
            # Create isolated namespace
            namespace = {
                '__builtins__': __builtins__,
                'print': print  # Allow printing
            }
            
            # Capture stdout
            old_stdout = sys.stdout
            sys.stdout = captured_output = io.StringIO()
            
            try:
                # Execute user code
                exec(user_code, namespace)
                
                # Get the test input and expected output
                test_input = test_case.get('input')
                expected = test_case.get('expected')
                function_name = test_case.get('function')
                
                # Call the function with test input
                if function_name and function_name in namespace:
                    func = namespace[function_name]
                    
                    # Handle different input formats
                    if isinstance(test_input, dict):
                        actual = func(**test_input)
                    elif isinstance(test_input, list):
                        actual = func(*test_input)
                    elif test_input is None:
                        actual = func()
                    else:
                        actual = func(test_input)
                    
                    result['actual'] = actual
                    
                    # Smart comparison with better error messages
                    comparison_result = self._compare_values(actual, expected)
                    result['passed'] = comparison_result['match']
                    
                    if not result['passed']:
                        # Generate helpful error message
                        result['error'] = self._generate_helpful_error(
                            expected, actual, function_name, test_case, comparison_result
                        )
                else:
                    result['error'] = self._generate_function_not_found_error(
                        function_name, user_code, namespace
                    )
                
            finally:
                # Restore stdout and capture output
                sys.stdout = old_stdout
                result['output'] = captured_output.getvalue()
            
        except Exception as e:
            result['error'] = f"{type(e).__name__}: {str(e)}"
            result['traceback'] = traceback.format_exc()
        
        return result
    
    def validate_code(self, code: str) -> Dict:
        """Validate code without running tests"""
        result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        try:
            # Check syntax
            ast.parse(code)
        except SyntaxError as e:
            result['valid'] = False
            result['errors'].append(f"Syntax Error on line {e.lineno}: {e.msg}")
        
        # Check for common issues
        if 'import os' in code or 'import sys' in code:
            result['warnings'].append("System imports detected - be careful!")
        
        if 'exec' in code or 'eval' in code:
            result['warnings'].append("Dynamic execution detected - this can be dangerous!")
        
        return result
    
    def _compare_values(self, actual, expected) -> Dict:
        """Smart comparison that handles different types and edge cases"""
        result = {'match': False, 'issue': None}
        
        # Handle None
        if actual is None and expected is None:
            result['match'] = True
            return result
        
        if actual is None or expected is None:
            result['issue'] = 'none_mismatch'
            return result
        
        # Type mismatch
        if type(actual) != type(expected):
            # Allow int/float flexibility
            if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
                result['match'] = abs(actual - expected) < 0.01
                if not result['match']:
                    result['issue'] = 'number_mismatch'
                return result
            else:
                result['issue'] = 'type_mismatch'
                return result
        
        # String comparison (strip whitespace)
        if isinstance(expected, str):
            if actual.strip() == expected.strip():
                result['match'] = True
                return result
            elif actual == expected:
                result['match'] = True
                return result
            else:
                result['issue'] = 'string_mismatch'
                return result
        
        # Float comparison (handle precision)
        if isinstance(expected, float):
            if abs(actual - expected) < 0.01:
                result['match'] = True
                return result
            else:
                result['issue'] = 'float_precision'
                return result
        
        # List/Tuple comparison
        if isinstance(expected, (list, tuple)):
            if len(actual) != len(expected):
                result['issue'] = 'length_mismatch'
                return result
            
            # Element-by-element comparison
            for i, (a, e) in enumerate(zip(actual, expected)):
                sub_result = self._compare_values(a, e)
                if not sub_result['match']:
                    result['issue'] = f'element_{i}_mismatch'
                    return result
            
            result['match'] = True
            return result
        
        # Dict comparison
        if isinstance(expected, dict):
            if set(actual.keys()) != set(expected.keys()):
                result['issue'] = 'dict_keys_mismatch'
                return result
            
            for key in expected:
                sub_result = self._compare_values(actual.get(key), expected.get(key))
                if not sub_result['match']:
                    result['issue'] = f'dict_value_{key}_mismatch'
                    return result
            
            result['match'] = True
            return result
        
        # Default comparison
        if actual == expected:
            result['match'] = True
        else:
            result['issue'] = 'value_mismatch'
        
        return result
    
    def _generate_helpful_error(self, expected, actual, function_name, test_case, comparison_result) -> str:
        """Generate educational error message with debugging help"""
        issue = comparison_result.get('issue', 'unknown')
        
        # Build helpful message based on issue type
        if issue == 'type_mismatch':
            return f"""❌ Wrong Data Type

Expected: {type(expected).__name__} ({expected})
Got: {type(actual).__name__} ({actual})

💡 How to fix:
- If you need a number, remove quotes: 5 not "5"
- If you need text, add quotes: "hello" not hello
- Check your return statement returns the right type
- Example: return 5 (number) vs return "5" (string)
"""
        
        elif issue == 'string_mismatch':
            # Show character-by-character difference
            diff_hint = ""
            if len(str(actual)) != len(str(expected)):
                diff_hint = f"\n- Length: Expected {len(str(expected))}, got {len(str(actual))}"
            
            return f"""❌ String Doesn't Match

Expected: "{expected}"
Got: "{actual}"{diff_hint}

💡 How to fix:
- Check spelling and capitalization carefully
- Make sure punctuation matches exactly  
- Remove any extra spaces at start/end
- Use f-strings for variables: f"Hello, {{name}}!"
- Check quotes match: "text" or 'text' (be consistent)
"""
        
        elif issue == 'number_mismatch' or issue == 'float_precision':
            diff = abs(actual - expected) if isinstance(actual, (int, float)) and isinstance(expected, (int, float)) else 'N/A'
            return f"""❌ Number Doesn't Match

Expected: {expected}
Got: {actual}
Difference: {diff}

💡 How to fix:
- Check your math formula carefully
- Common mistakes: 
  * Using + instead of *
  * Forgetting parentheses: (a + b) * 2
  * Integer division: use / not //
- For rounding: round(result, 2) for 2 decimals
- Print intermediate values to debug: print(f"Result is: {{result}}")
"""
        
        elif issue == 'length_mismatch':
            return f"""❌ List/Collection Has Wrong Number of Items

Expected {len(expected)} items: {expected}
Got {len(actual)} items: {actual}

💡 How to fix:
- Check your loop - are you adding all items?
- Did you accidentally skip some? Check your 'if' conditions
- Are you adding extra items by mistake?
- Use print(my_list) before returning to see what you have
"""
        
        elif issue == 'dict_keys_mismatch':
            expected_keys = set(expected.keys())
            actual_keys = set(actual.keys())
            missing = expected_keys - actual_keys
            extra = actual_keys - expected_keys
            
            msg = "❌ Dictionary Keys Don't Match\n\n"
            if missing:
                msg += f"Missing keys: {list(missing)}\n"
            if extra:
                msg += f"Extra keys: {list(extra)}\n"
            msg += f"\n💡 How to fix:\n"
            msg += f"- Check key names for typos\n"
            msg += f"- Make sure you're creating all required keys\n"
            msg += f"- Should have exactly: {list(expected.keys())}\n"
            msg += f"- Example: {{'key': 'value', 'key2': 'value2'}}\n"
            
            return msg
        
        elif issue == 'none_mismatch':
            if actual is None:
                return """❌ Function Returned Nothing (None)

💡 How to fix:
- Add a return statement: return result
- Make sure return is not just 'pass'
- Check indentation - return should be INSIDE the function
- Don't just print, you must RETURN:
  
  ❌ Wrong:
  def add(a, b):
      print(a + b)  # This prints but doesn't return!
  
  ✅ Right:
  def add(a, b):
      return a + b  # This returns the value
"""
            else:
                return f"""❌ Function Returned Something Unexpected

Expected: None (nothing)
Got: {actual}

💡 This test expects the function to NOT return anything
- Remove the return statement, or
- Check if you're in the right test case
"""
        
        else:
            # Generic helpful error with debugging steps
            return f"""❌ Output Doesn't Match

Expected: {expected}
Got: {actual}

💡 Debugging steps:
1. **Add print statements** to see what's happening:
   print(f"My result is: {{result}}")
   
2. **Check the instructions** - did you miss a requirement?

3. **Compare to hints** - are you using the right approach?

4. **Test manually** - try calling your function:
   print({function_name}({test_case.get('input')}))
   
5. **Check for typos** in variable names and operations

6. **Verify your logic** - step through mentally line by line
"""
    
    def _generate_function_not_found_error(self, function_name, user_code, namespace) -> str:
        """Generate helpful error when function is not found"""
        # Check what functions ARE defined
        defined_functions = [name for name in namespace if callable(namespace.get(name)) and not name.startswith('_')]
        
        has_def = 'def ' in user_code
        has_function_name = function_name in user_code
        
        msg = f"""❌ Function '{function_name}' Not Found

"""
        
        if not has_def:
            msg += """💡 You haven't defined any function yet!

How to define a function:
```python
def function_name():
    # Your code here
    return result
```

Steps:
1. Start with 'def' keyword
2. Add function name
3. Add parentheses ()
4. Add colon :
5. Indent the code inside (4 spaces or Tab)
"""
        elif not has_function_name:
            msg += f"""💡 Function name doesn't match!

You wrote: {defined_functions if defined_functions else 'no functions'}
Should be: {function_name}

Check for:
- Typos in the name
- Capitalization (Python is case-sensitive!)
- Extra/missing characters
"""
        else:
            msg += f"""💡 Function exists but isn't callable

Possible issues:
1. **Indentation error** - 'def' should start at column 0
2. **Syntax error** - check for missing colons ':'
3. **Not in the right scope** - function defined inside another function?

Your code has {len(user_code.split('def'))-1} 'def' keyword(s)
"""
        
        return msg
