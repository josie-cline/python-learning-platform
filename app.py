"""
PyQuest - Python Learning Platform
Main web application server
"""

from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import json
from pathlib import Path
import markdown

# Load environment variables
load_dotenv()

# Import our modules
from challenges.loader import ChallengeLoader
from grader.test_runner import TestRunner
from reminders.scheduler import ReminderScheduler
from progress.tracker import ProgressTracker

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
CORS(app)

# Initialize Markdown converter
md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])

# Add custom filter for markdown
@app.template_filter('markdown')
def markdown_filter(text):
    """Convert markdown to HTML"""
    if text:
        return markdown.markdown(text, extensions=['fenced_code', 'tables', 'nl2br'])
    return ''

# Initialize components
challenge_loader = ChallengeLoader()
test_runner = TestRunner()
progress_tracker = ProgressTracker()
reminder_scheduler = ReminderScheduler()

# Start reminder scheduler in background
reminder_scheduler.start()


@app.route('/')
def index():
    """Homepage - Dashboard with progress overview"""
    stats = progress_tracker.get_stats()
    today_challenge = challenge_loader.get_today_challenge()
    
    return render_template('index.html', 
                         stats=stats, 
                         today_challenge=today_challenge,
                         user_name=os.getenv('USER_NAME', 'Learner'))


@app.route('/challenge')
def challenge():
    """Today's challenge page"""
    day_offset = request.args.get('day', 0, type=int)
    challenge_data = challenge_loader.get_challenge_by_day(day_offset)
    
    if not challenge_data:
        return render_template('error.html', 
                             message="No challenge available for this day")
    
    return render_template('challenge.html', challenge=challenge_data)


@app.route('/challenge/<int:week>/<int:day>')
def specific_challenge(week, day):
    """Get a specific challenge by week and day"""
    challenge_data = challenge_loader.get_challenge(week, day)
    
    if not challenge_data:
        return render_template('error.html', 
                             message=f"Challenge not found: Week {week}, Day {day}")
    
    return render_template('challenge.html', challenge=challenge_data)


@app.route('/api/submit', methods=['POST'])
def submit_solution():
    """Submit and grade a solution"""
    data = request.json
    
    challenge_id = data.get('challenge_id')
    code = data.get('code', '')
    
    # Get challenge details
    challenge = challenge_loader.get_challenge_by_id(challenge_id)
    if not challenge:
        return jsonify({'error': 'Challenge not found'}), 404
    
    # Run tests
    result = test_runner.run_tests(code, challenge['tests'])
    
    # If passed, record progress
    if result['passed']:
        progress_tracker.record_completion(
            challenge_id=challenge_id,
            code=code,
            time_spent=data.get('time_spent', 0)
        )
    
    return jsonify(result)


@app.route('/api/progress')
def get_progress():
    """Get user progress data"""
    stats = progress_tracker.get_stats()
    history = progress_tracker.get_history(days=30)
    
    return jsonify({
        'stats': stats,
        'history': history
    })


@app.route('/progress')
def progress_page():
    """Progress tracking page"""
    stats = progress_tracker.get_stats()
    recent_completions = progress_tracker.get_recent_completions(10)
    weekly_summary = progress_tracker.get_weekly_summary()
    
    return render_template('progress.html',
                         stats=stats,
                         recent_completions=recent_completions,
                         weekly_summary=weekly_summary)


@app.route('/api/hint/<challenge_id>')
def get_hint(challenge_id):
    """Get a hint for a challenge"""
    challenge = challenge_loader.get_challenge_by_id(challenge_id)
    
    if not challenge:
        return jsonify({'error': 'Challenge not found'}), 404
    
    hints = challenge.get('hints', [])
    hint_level = request.args.get('level', 0, type=int)
    
    if hint_level < len(hints):
        return jsonify({'hint': hints[hint_level]})
    else:
        return jsonify({'hint': 'No more hints available'})


@app.route('/curriculum')
def curriculum():
    """View full curriculum and roadmap"""
    roadmap = challenge_loader.get_roadmap()
    return render_template('curriculum.html', roadmap=roadmap)


@app.route('/resources')
def resources():
    """Learning resources and references"""
    return render_template('resources.html')


@app.route('/api/test-reminder', methods=['POST'])
def test_reminder():
    """Test reminder system (for debugging)"""
    reminder_scheduler.send_test_notification()
    return jsonify({'status': 'Reminder sent'})


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('error.html', message="Page not found"), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('error.html', 
                         message="Something went wrong. Please try again."), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'true').lower() == 'true'
    
    print(f"""
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║          🐍 PyQuest Learning Platform 🐍          ║
    ║                                                   ║
    ║   Your journey to Python mastery starts now!     ║
    ║                                                   ║
    ║   📍 Open your browser to:                        ║
    ║      http://localhost:{port}                         ║
    ║                                                   ║
    ║   Press Ctrl+C to stop the server                ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
