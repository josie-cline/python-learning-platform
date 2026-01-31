"""
Notification Handlers
Send notifications via email and Slack
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class EmailNotifier:
    """Send email notifications"""
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.username = os.getenv('SMTP_USERNAME')
        self.password = os.getenv('SMTP_PASSWORD')
    
    def is_configured(self) -> bool:
        """Check if email is properly configured"""
        return bool(self.username and self.password)
    
    def send(self, to: str, subject: str, body: str) -> bool:
        """Send an email"""
        if not self.is_configured():
            print("⚠️  Email not configured - skipping email notification")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
            
            print(f"✅ Email sent to {to}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False


class SlackNotifier:
    """Send Slack notifications"""
    
    def __init__(self):
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    
    def is_configured(self) -> bool:
        """Check if Slack is properly configured"""
        return bool(self.webhook_url)
    
    def send(self, message: str) -> bool:
        """Send a Slack message"""
        if not self.is_configured():
            print("⚠️  Slack not configured - skipping Slack notification")
            return False
        
        try:
            payload = {
                'text': message,
                'username': 'PyQuest Bot',
                'icon_emoji': ':snake:'
            }
            
            response = requests.post(self.webhook_url, json=payload)
            
            if response.status_code == 200:
                print("✅ Slack notification sent")
                return True
            else:
                print(f"❌ Slack notification failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Failed to send Slack notification: {e}")
            return False
