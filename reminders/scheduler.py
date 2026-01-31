"""
Reminder Scheduler
Handles daily reminders and weekly progress reports
"""

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, time
import os
from dotenv import load_dotenv
from .notifier import EmailNotifier, SlackNotifier

load_dotenv()


class ReminderScheduler:
    """Schedules and manages reminders and reports"""
    
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.email_notifier = EmailNotifier()
        self.slack_notifier = SlackNotifier()
        
        # Get config from environment
        self.daily_time = os.getenv('DAILY_REMINDER_TIME', '09:00')
        self.weekly_day = int(os.getenv('WEEKLY_REPORT_DAY', '0'))  # Monday
        self.weekly_time = os.getenv('WEEKLY_REPORT_TIME', '10:00')
        
        self._setup_jobs()
    
    def _setup_jobs(self):
        """Set up scheduled jobs"""
        # Daily reminder
        hour, minute = map(int, self.daily_time.split(':'))
        self.scheduler.add_job(
            self.send_daily_reminder,
            'cron',
            hour=hour,
            minute=minute,
            id='daily_reminder'
        )
        
        # Weekly report
        hour, minute = map(int, self.weekly_time.split(':'))
        self.scheduler.add_job(
            self.send_weekly_report,
            'cron',
            day_of_week=self.weekly_day,
            hour=hour,
            minute=minute,
            id='weekly_report'
        )
    
    def start(self):
        """Start the scheduler"""
        if not self.scheduler.running:
            self.scheduler.start()
            print("✅ Reminder scheduler started")
    
    def stop(self):
        """Stop the scheduler"""
        if self.scheduler.running:
            self.scheduler.shutdown()
    
    def send_daily_reminder(self):
        """Send daily learning reminder"""
        from progress.tracker import ProgressTracker
        from challenges.loader import ChallengeLoader
        
        tracker = ProgressTracker()
        loader = ChallengeLoader()
        
        stats = tracker.get_stats()
        today_challenge = loader.get_today_challenge()
        
        if not today_challenge:
            return
        
        message = f"""
🐍 PyQuest Daily Reminder

Good morning! Time for today's Python challenge:

📚 {today_challenge['title']}
⏱️ Estimated time: {today_challenge.get('time_estimate', '30-45')} minutes
🎯 Topic: {today_challenge.get('topic', 'Python fundamentals')}

Your Stats:
✅ Challenges completed: {stats['total_challenges_completed']}
🔥 Current streak: {stats['current_streak']} days
📈 Completion rate: {stats['completion_rate']}%

Ready to learn? Open: http://localhost:5000

Keep up the great work! 🚀
        """
        
        # Send via email
        user_email = os.getenv('USER_EMAIL')
        if user_email and self.email_notifier.is_configured():
            self.email_notifier.send(
                to=user_email,
                subject="🐍 Time for your daily Python challenge!",
                body=message
            )
        
        # Send via Slack
        if self.slack_notifier.is_configured():
            self.slack_notifier.send(message)
    
    def send_weekly_report(self):
        """Send weekly progress report"""
        from progress.tracker import ProgressTracker
        
        tracker = ProgressTracker()
        stats = tracker.get_stats()
        weekly = tracker.get_weekly_summary()
        status = tracker.is_on_track()
        
        message = f"""
📊 PyQuest Weekly Progress Report

Week of {weekly['week_start']}

This Week:
✅ Challenges completed: {weekly['challenges_completed']}/7
⏱️ Time invested: {weekly['time_spent']} minutes
📅 Active days: {weekly['days_active']}/7

Overall Progress:
🎯 Total challenges: {stats['total_challenges_completed']}
📈 Completion rate: {stats['completion_rate']}%
🔥 Current streak: {stats['current_streak']} days
⭐ Longest streak: {stats['longest_streak']} days
⏰ Total learning time: {stats['total_time_hours']} hours

Status: {status['completion_status'].upper()}
{status['recommendation']}

Keep learning! 🚀
View your dashboard: http://localhost:5000
        """
        
        # Send via email
        user_email = os.getenv('REPORT_EMAIL') or os.getenv('USER_EMAIL')
        if user_email and self.email_notifier.is_configured():
            self.email_notifier.send(
                to=user_email,
                subject="📊 Your Weekly PyQuest Progress Report",
                body=message
            )
        
        # Send via Slack
        if self.slack_notifier.is_configured():
            self.slack_notifier.send(message)
    
    def send_test_notification(self):
        """Send a test notification"""
        message = "🧪 Test notification from PyQuest! Your reminders are working correctly."
        
        user_email = os.getenv('USER_EMAIL')
        if user_email and self.email_notifier.is_configured():
            self.email_notifier.send(
                to=user_email,
                subject="🧪 PyQuest Test Notification",
                body=message
            )
        
        if self.slack_notifier.is_configured():
            self.slack_notifier.send(message)
