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
    
    # Get next uncompleted challenge (progress-based, not calendar-based)
    completed_ids = progress_tracker.get_completed_ids()
    next_challenge = challenge_loader.get_next_uncompleted_challenge(completed_ids)
    
    # Fallback to today's challenge if all completed
    if not next_challenge:
        next_challenge = challenge_loader.get_today_challenge()
    
    # Create clean preview (text before ## LESSON section)
    if next_challenge and next_challenge.get('description'):
        desc = next_challenge['description']
        # Get text before first ## heading
        if '##' in desc:
            preview = desc.split('##')[0].strip()
        else:
            preview = desc
        next_challenge['preview'] = preview[:200] + '...' if len(preview) > 200 else preview
    
    return render_template('index.html', 
                         stats=stats, 
                         today_challenge=next_challenge,
                         user_name=os.getenv('USER_NAME', 'Learner'))


@app.route('/challenge')
def challenge():
    """Challenge page - shows next uncompleted or specific challenge"""
    day_offset = request.args.get('day', 0, type=int)
    week = request.args.get('week', type=int)
    day = request.args.get('day_num', type=int)
    
    # If specific week/day requested
    if week is not None and day is not None:
        challenge_data = challenge_loader.get_challenge(week, day)
    elif day_offset != 0:
        # Use day offset from today
        challenge_data = challenge_loader.get_challenge_by_day(day_offset)
    else:
        # No parameters - show next uncompleted challenge
        completed_ids = progress_tracker.get_completed_ids()
        challenge_data = challenge_loader.get_next_uncompleted_challenge(completed_ids)
        
        # Fallback to today's challenge if all completed
        if not challenge_data:
            challenge_data = challenge_loader.get_today_challenge()
    
    if not challenge_data:
        return render_template('error.html', 
                             message="No challenge available for this day")
    
    # Get previous and next challenge info
    current_week = challenge_data.get('week')
    current_day = challenge_data.get('day')
    
    # Calculate previous
    prev_week, prev_day = current_week, current_day - 1
    if prev_day < 1:
        prev_week -= 1
        prev_day = 7
    
    # Calculate next
    next_week, next_day = current_week, current_day + 1
    if next_day > 7:
        next_week += 1
        next_day = 1
    
    # Check if prev/next exist
    has_prev = challenge_loader.get_challenge(prev_week, prev_day) is not None
    has_next = challenge_loader.get_challenge(next_week, next_day) is not None
    
    return render_template('challenge.html', 
                         challenge=challenge_data,
                         has_prev=has_prev,
                         has_next=has_next,
                         prev_week=prev_week,
                         prev_day=prev_day,
                         next_week=next_week,
                         next_day=next_day)


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
    
    # Enhance completions with challenge titles
    for completion in recent_completions:
        challenge = challenge_loader.get_challenge_by_id(completion['challenge_id'])
        if challenge:
            completion['title'] = challenge.get('title', 'Unknown Challenge')
            completion['week'] = challenge.get('week', 0)
            completion['day'] = challenge.get('day', 0)
        else:
            completion['title'] = completion['challenge_id']
    
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


@app.route('/browse')
def browse_challenges():
    """Browse all available challenges"""
    roadmap = challenge_loader.get_roadmap()
    
    # Get all challenges organized by week
    all_challenges = {}
    for week_info in roadmap:
        week_num = week_info['week']
        week_data = challenge_loader.get_week_data(week_num)
        if week_data:
            all_challenges[week_num] = {
                'title': week_info['title'],
                'description': week_info['description'],
                'challenges': week_data.get('challenges', [])
            }
    
    return render_template('browse.html', weeks=all_challenges)


@app.route('/practice')
def practice():
    """Practice sandbox with random challenges"""
    return render_template('practice.html')


@app.route('/api/random-challenge')
def random_challenge():
    """Get a random challenge based on filters"""
    topics = request.args.getlist('topics')
    difficulty = request.args.get('difficulty')
    
    # Get all available challenges
    all_challenges = []
    roadmap = challenge_loader.get_roadmap()
    
    for week_info in roadmap:
        week_num = week_info['week']
        week_data = challenge_loader.get_week_data(week_num)
        if week_data:
            for ch in week_data.get('challenges', []):
                ch['week'] = week_num
                ch['id'] = f"week{week_num:03d}_day{ch.get('day')}"
                all_challenges.append(ch)
    
    # Filter by difficulty if specified
    if difficulty:
        all_challenges = [ch for ch in all_challenges if ch.get('difficulty') == difficulty]
    
    # Filter by topics if specified
    if topics:
        filtered = []
        for ch in all_challenges:
            # Check both 'keywords' field and 'topic' field
            keywords = ch.get('keywords', [])
            topic = ch.get('topic', '').lower()
            
            # If challenge has any of the requested topics in keywords or topic
            if any(t.lower() in keywords or t.lower() in topic for t in topics):
                filtered.append(ch)
        all_challenges = filtered
    
    # Return random challenge
    import random
    if all_challenges:
        challenge = random.choice(all_challenges)
        
        # Convert markdown to HTML for display
        # Reset markdown converter to clear state
        md.reset()
        if challenge.get('description'):
            challenge['description'] = md.convert(challenge['description'])
            md.reset()
        if challenge.get('instructions'):
            challenge['instructions'] = md.convert(challenge['instructions'])
            md.reset()
        
        return jsonify(challenge)
    else:
        return jsonify({'error': 'No challenges match your filters'}), 404


@app.route('/tools')
def tools_learning():
    """Learning paths for development tools"""
    return render_template('tools.html')


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
