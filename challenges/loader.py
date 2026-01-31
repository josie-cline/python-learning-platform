"""
Challenge Loader
Loads and manages Python challenges from YAML files
"""

import yaml
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import os


class ChallengeLoader:
    """Loads and manages Python learning challenges"""
    
    def __init__(self, challenges_dir: str = None):
        if challenges_dir is None:
            challenges_dir = Path(__file__).parent / 'data'
        self.challenges_dir = Path(challenges_dir)
        self.challenges_cache = {}
        self._load_all_challenges()
    
    def _load_all_challenges(self):
        """Load all challenge files into cache"""
        for yaml_file in sorted(self.challenges_dir.glob('week_*.yaml')):
            week_num = int(yaml_file.stem.split('_')[1])
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                    self.challenges_cache[week_num] = data
            except Exception as e:
                print(f"Error loading {yaml_file}: {e}")
    
    def get_challenge(self, week: int, day: int) -> Optional[Dict]:
        """Get a specific challenge by week and day"""
        if week not in self.challenges_cache:
            return None
        
        week_data = self.challenges_cache[week]
        challenges = week_data.get('challenges', [])
        
        for challenge in challenges:
            if challenge.get('day') == day:
                challenge['week'] = week
                challenge['id'] = f"week{week:03d}_day{day}"
                return challenge
        
        return None
    
    def get_today_challenge(self) -> Optional[Dict]:
        """Get today's challenge based on start date"""
        # Calculate days since start (you started today!)
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Check if there's a saved start date
        progress_file = Path('user_progress.json')
        if progress_file.exists():
            import json
            with open(progress_file, 'r') as f:
                data = json.load(f)
                if 'start_date' in data:
                    start_date = datetime.fromisoformat(data['start_date'])
        
        days_since_start = (datetime.now() - start_date).days
        
        # Calculate week and day
        week = (days_since_start // 7) + 1
        day = (days_since_start % 7) + 1
        
        return self.get_challenge(week, day)
    
    def get_challenge_by_day(self, day_offset: int = 0) -> Optional[Dict]:
        """Get challenge by day offset (0 = today, 1 = tomorrow, -1 = yesterday)"""
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        progress_file = Path('user_progress.json')
        if progress_file.exists():
            import json
            with open(progress_file, 'r') as f:
                data = json.load(f)
                if 'start_date' in data:
                    start_date = datetime.fromisoformat(data['start_date'])
        
        target_date = datetime.now() + timedelta(days=day_offset)
        days_since_start = (target_date - start_date).days
        
        week = (days_since_start // 7) + 1
        day = (days_since_start % 7) + 1
        
        return self.get_challenge(week, day)
    
    def get_challenge_by_id(self, challenge_id: str) -> Optional[Dict]:
        """Get challenge by ID (e.g., 'week001_day1')"""
        try:
            parts = challenge_id.split('_')
            week = int(parts[0].replace('week', ''))
            day = int(parts[1].replace('day', ''))
            return self.get_challenge(week, day)
        except:
            return None
    
    def get_roadmap(self) -> List[Dict]:
        """Get the full learning roadmap"""
        roadmap = []
        for week_num in sorted(self.challenges_cache.keys()):
            week_data = self.challenges_cache[week_num]
            roadmap.append({
                'week': week_num,
                'title': week_data.get('title', f'Week {week_num}'),
                'description': week_data.get('description', ''),
                'topics': week_data.get('topics', []),
                'challenge_count': len(week_data.get('challenges', []))
            })
        return roadmap
    
    def get_week_data(self, week: int) -> Optional[Dict]:
        """Get all data for a specific week"""
        return self.challenges_cache.get(week)
