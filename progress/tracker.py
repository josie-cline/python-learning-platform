"""
Progress Tracker
Tracks user learning progress, streaks, and statistics
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict


class ProgressTracker:
    """Tracks and manages user learning progress"""
    
    def __init__(self, data_file: str = 'user_progress.json'):
        self.data_file = Path(data_file)
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load progress data from file"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return self._create_new_data()
        else:
            return self._create_new_data()
    
    def _create_new_data(self) -> Dict:
        """Create new progress data structure"""
        return {
            'start_date': datetime.now().isoformat(),
            'total_time_minutes': 0,
            'current_streak': 0,
            'longest_streak': 0,
            'last_activity_date': None,
            'completed_challenges': [],
            'skills': {},
            'daily_history': []
        }
    
    def _save_data(self):
        """Save progress data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def record_completion(self, challenge_id: str, code: str, time_spent: int):
        """Record a completed challenge"""
        today = datetime.now().date().isoformat()
        
        # Check if already completed
        if challenge_id in self.data['completed_challenges']:
            return
        
        # Add to completed list
        self.data['completed_challenges'].append(challenge_id)
        
        # Update time
        self.data['total_time_minutes'] += time_spent
        
        # Update streak
        self._update_streak(today)
        
        # Record in daily history
        self.data['daily_history'].append({
            'date': today,
            'challenge_id': challenge_id,
            'time_spent': time_spent,
            'timestamp': datetime.now().isoformat()
        })
        
        # Update last activity
        self.data['last_activity_date'] = today
        
        self._save_data()
    
    def _update_streak(self, today: str):
        """Update learning streak"""
        last_date = self.data.get('last_activity_date')
        
        if not last_date:
            # First completion
            self.data['current_streak'] = 1
            self.data['longest_streak'] = 1
        else:
            last = datetime.fromisoformat(last_date).date()
            current = datetime.fromisoformat(today).date()
            days_diff = (current - last).days
            
            if days_diff == 0:
                # Same day, no change
                pass
            elif days_diff == 1:
                # Consecutive day
                self.data['current_streak'] += 1
                self.data['longest_streak'] = max(
                    self.data['longest_streak'],
                    self.data['current_streak']
                )
            else:
                # Streak broken
                self.data['current_streak'] = 1
    
    def get_stats(self) -> Dict:
        """Get user statistics"""
        completed = len(self.data['completed_challenges'])
        
        # Calculate weeks since start
        start = datetime.fromisoformat(self.data['start_date'])
        weeks_elapsed = ((datetime.now() - start).days // 7) + 1
        expected_challenges = weeks_elapsed * 7
        
        # Calculate completion rate
        completion_rate = (completed / expected_challenges * 100) if expected_challenges > 0 else 0
        
        return {
            'total_challenges_completed': completed,
            'expected_challenges': expected_challenges,
            'completion_rate': round(completion_rate, 1),
            'current_streak': self.data['current_streak'],
            'longest_streak': self.data['longest_streak'],
            'total_time_hours': round(self.data['total_time_minutes'] / 60, 1),
            'avg_time_per_challenge': round(
                self.data['total_time_minutes'] / completed, 1
            ) if completed > 0 else 0,
            'days_since_start': (datetime.now() - start).days,
            'weeks_since_start': weeks_elapsed,
            'last_activity': self.data.get('last_activity_date')
        }
    
    def get_history(self, days: int = 30) -> List[Dict]:
        """Get recent activity history"""
        cutoff = datetime.now() - timedelta(days=days)
        
        history = []
        for entry in reversed(self.data['daily_history']):
            entry_date = datetime.fromisoformat(entry['timestamp'])
            if entry_date >= cutoff:
                history.append(entry)
        
        return history
    
    def is_completed(self, challenge_id: str) -> bool:
        """Check if a challenge has been completed"""
        return challenge_id in self.data['completed_challenges']
    
    def get_completed_ids(self) -> List[str]:
        """Get list of all completed challenge IDs"""
        return self.data['completed_challenges']
    
    def get_recent_completions(self, count: int = 10) -> List[Dict]:
        """Get most recent completions"""
        return list(reversed(self.data['daily_history'][-count:]))
    
    def get_weekly_summary(self) -> Dict:
        """Get summary for the current week"""
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        
        weekly_entries = [
            entry for entry in self.data['daily_history']
            if datetime.fromisoformat(entry['timestamp']) >= week_start
        ]
        
        return {
            'week_start': week_start.date().isoformat(),
            'challenges_completed': len(weekly_entries),
            'time_spent': sum(e['time_spent'] for e in weekly_entries),
            'days_active': len(set(e['date'] for e in weekly_entries))
        }
    
    def is_on_track(self) -> Dict:
        """Check if user is on track with their goals"""
        stats = self.get_stats()
        
        # Expected: 1 challenge per day
        on_track = stats['completion_rate'] >= 80
        
        # Expected: 30-60 min per day
        expected_time = stats['days_since_start'] * 45  # 45 min average
        time_ratio = (stats['total_time_hours'] * 60) / expected_time if expected_time > 0 else 0
        
        return {
            'on_track': on_track,
            'completion_status': 'on track' if on_track else 'behind',
            'time_status': 'good' if time_ratio >= 0.8 else 'low',
            'recommendation': self._get_recommendation(stats, time_ratio)
        }
    
    def _get_recommendation(self, stats: Dict, time_ratio: float) -> str:
        """Get personalized recommendation"""
        if stats['completion_rate'] < 50:
            return "Try to complete at least one challenge today to get back on track!"
        elif stats['current_streak'] == 0:
            return "Start a new streak today - consistency is key!"
        elif stats['current_streak'] >= 7:
            return f"Amazing! You're on a {stats['current_streak']}-day streak. Keep it up!"
        elif time_ratio < 0.5:
            return "Try to spend more time with each challenge - understanding is more important than speed."
        else:
            return "Great progress! Keep learning at your own pace."
