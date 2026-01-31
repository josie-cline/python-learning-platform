"""
AI-Powered Challenge Generator
Generates unique practice challenges using OpenAI
"""

import os
import json
from typing import Dict, List, Optional
from openai import OpenAI


class ChallengeGenerator:
    """Generates practice challenges using AI"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            try:
                self.client = OpenAI(api_key=self.api_key)
                self.enabled = True
            except Exception as e:
                print(f"OpenAI initialization error: {e}")
                self.enabled = False
                self.client = None
        else:
            self.enabled = False
            self.client = None
    
    def is_enabled(self) -> bool:
        """Check if AI generation is available"""
        return self.enabled and self.client is not None
    
    def generate_challenge(self, topics: List[str], difficulty: str = "beginner") -> Optional[Dict]:
        """Generate a unique practice challenge"""
        
        if not self.is_enabled():
            return None
        
        # Build the prompt
        topic_str = ", ".join(topics) if topics else "general Python"
        
        prompt = f"""Generate a unique Python coding challenge for practice.

Difficulty: {difficulty}
Topics to cover: {topic_str}

Requirements:
1. Create a real-world coding problem (not from existing tutorials)
2. Make it different from common "Hello World" or basic examples
3. Challenge should be solvable in 10-20 minutes
4. Include clear instructions on what to build
5. Provide helpful hints (not the full solution)

Return JSON with this EXACT structure:
{{
    "title": "Short descriptive title",
    "topic": "One-line topic description",
    "difficulty": "{difficulty}",
    "time_estimate": "15-20 minutes",
    "description": "Introduction to the problem. What will they learn?",
    "instructions": "Clear description of what function to write and what it should do. Describe the PROBLEM, not the implementation.",
    "starter_code": "def function_name(params):\\n    # Your code here\\n    pass",
    "hints": [
        "First hint - general approach",
        "Second hint - specific method or syntax",
        "Third hint - more detailed guidance",
        "Fourth hint - nearly complete example"
    ],
    "sample_solution": "Complete working solution for reference"
}}

Make it creative and practical. Focus on {topic_str}. Difficulty: {difficulty}."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # More cost-effective
                messages=[
                    {"role": "system", "content": "You are a Python programming instructor creating practice challenges for students learning to code. Generate creative, practical challenges that teach real-world skills."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,  # More creative
                max_tokens=1500
            )
            
            # Parse the response
            content = response.choices[0].message.content
            
            # Extract JSON (handle markdown code blocks if present)
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            challenge_data = json.loads(content)
            
            # Add metadata
            challenge_data['week'] = 0  # Mark as practice challenge
            challenge_data['day'] = 0
            challenge_data['id'] = 'practice_generated'
            challenge_data['keywords'] = topics
            
            return challenge_data
            
        except Exception as e:
            print(f"Error generating challenge: {e}")
            return None
    
    def generate_with_fallback(self, topics: List[str], difficulty: str = "beginner") -> Dict:
        """Generate challenge or return helpful message if unavailable"""
        
        challenge = self.generate_challenge(topics, difficulty)
        
        if challenge:
            return challenge
        else:
            # Return a message explaining how to enable
            return {
                "error": "AI Challenge Generation Not Configured",
                "message": "To enable AI-generated practice challenges, add your OpenAI API key to the .env file.",
                "instructions": [
                    "1. Get an API key at https://platform.openai.com/api-keys",
                    "2. Add to .env file: OPENAI_API_KEY=your-key-here",
                    "3. Restart the server",
                    "4. Generate unlimited unique practice challenges!"
                ],
                "fallback": "For now, practice mode will use curriculum challenges."
            }
