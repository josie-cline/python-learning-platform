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
                    
                    # Compare result
                    if actual == expected:
                        result['passed'] = True
                    else:
                        result['error'] = f"Expected {expected}, got {actual}"
                else:
                    result['error'] = f"Function '{function_name}' not found in code"
                
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
