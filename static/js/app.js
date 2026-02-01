// PyQuest - Frontend JavaScript

// Dismiss beginner banner
function dismissBeginnerBanner() {
    const banner = document.getElementById('beginnerBanner');
    if (banner) {
        banner.style.display = 'none';
        localStorage.setItem('beginner_banner_dismissed', 'true');
    }
}

// Check if banner should be hidden
(function() {
    const dismissed = localStorage.getItem('beginner_banner_dismissed');
    if (dismissed === 'true') {
        const banner = document.getElementById('beginnerBanner');
        if (banner) {
            banner.style.display = 'none';
        }
    }
})();

// Theme Toggle
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Update icon and text
    updateThemeButton(newTheme);
}

// Update theme button icon and text
function updateThemeButton(theme) {
    const icon = document.querySelector('.theme-toggle-icon');
    const text = document.querySelector('.theme-toggle-text');
    
    if (theme === 'dark') {
        if (icon) icon.textContent = '☀️';
        if (text) text.textContent = 'Light Mode';
    } else {
        if (icon) icon.textContent = '🌓';
        if (text) text.textContent = 'Dark Mode';
    }
}

// Load saved theme on page load
(function() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    // Update button to match saved theme
    updateThemeButton(savedTheme);
})();

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Add fade-in animation on page load
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.3s';
        document.body.style.opacity = '1';
    }, 10);
});

// Code editor reference (CodeMirror will replace this)
const codeEditor = document.getElementById('codeEditor');

// Confirmation before leaving page with unsaved code
let codeChanged = false;

if (codeEditor) {
    const originalCode = codeEditor.value;
    
    codeEditor.addEventListener('input', () => {
        codeChanged = codeEditor.value !== originalCode;
    });
    
    window.addEventListener('beforeunload', (e) => {
        if (codeChanged) {
            e.preventDefault();
            e.returnValue = '';
        }
    });
}

// Auto-save code to localStorage (works with CodeMirror)
if (codeEditor) {
    const challengeId = window.location.pathname;
    
    // Helper to get code (works with both textarea and CodeMirror)
    window.getEditorCode = () => {
        return window.codeMirrorEditor ? window.codeMirrorEditor.getValue() : codeEditor.value;
    };
    
    // Helper to set code
    window.setEditorCode = (code) => {
        if (window.codeMirrorEditor) {
            window.codeMirrorEditor.setValue(code);
        } else {
            codeEditor.value = code;
        }
    };
    
    // Auto-save function
    window.autoSaveEditor = () => {
        const code = window.getEditorCode();
        if (code && code.trim() !== '') {
            localStorage.setItem(`code_${challengeId}`, code);
        }
    };
    
    // Load saved code (wait for CodeMirror to initialize)
    setTimeout(() => {
        const savedCode = localStorage.getItem(`code_${challengeId}`);
        const starterCode = window.getEditorCode();
        
        // Only prompt if saved code exists and is different from starter code
        if (savedCode && savedCode !== starterCode && savedCode.trim() !== '') {
            const autoResumeDisabled = localStorage.getItem('disable_auto_resume_prompt') === 'true';
            
            if (!autoResumeDisabled) {
                const resumeDiv = document.createElement('div');
                resumeDiv.className = 'auto-save-notification';
                resumeDiv.innerHTML = `
                    <div class="notification-content">
                        <span>💾 You have saved code from a previous session.</span>
                        <div class="notification-actions">
                            <button onclick="resumeSavedCode('${challengeId}')" class="btn btn-small btn-primary">Resume</button>
                            <button onclick="dismissResume()" class="btn btn-small btn-secondary">Start Fresh</button>
                            <button onclick="neverAskResume()" class="btn btn-small btn-text">Don't ask again</button>
                        </div>
                    </div>
                `;
                const workspace = document.querySelector('.challenge-workspace');
                if (workspace) workspace.insertBefore(resumeDiv, workspace.firstChild);
            }
        }
    }, 500);  // Wait for CodeMirror to initialize
    
    // Save code periodically
    setInterval(() => {
        window.autoSaveEditor();
    }, 30000); // Every 30 seconds
}

// Resume saved code function
function resumeSavedCode(challengeId) {
    const savedCode = localStorage.getItem(`code_${challengeId}`);
    if (savedCode) {
        window.setEditorCode(savedCode);
    }
    dismissResume();
}

// Dismiss resume notification
function dismissResume() {
    const notification = document.querySelector('.auto-save-notification');
    if (notification) {
        notification.remove();
    }
}

// Never ask to resume again
function neverAskResume() {
    localStorage.setItem('disable_auto_resume_prompt', 'true');
    dismissResume();
    
    // Show feedback
    const feedback = document.createElement('div');
    feedback.className = 'feedback-message';
    feedback.textContent = '✓ Auto-resume prompts disabled. You can re-enable in Settings.';
    document.querySelector('.challenge-editor').prepend(feedback);
    setTimeout(() => feedback.remove(), 3000);
}

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + Enter to run tests
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter' && codeEditor) {
        e.preventDefault();
        if (typeof runTests === 'function') {
            runTests();
        }
    }
    
    // Ctrl/Cmd + S to save (prevent default browser save)
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        if (codeEditor) {
            localStorage.setItem(`code_${window.location.pathname}`, codeEditor.value);
            showNotification('Code saved!', 'success');
        }
    }
});

// Show notification helper
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 5rem;
        right: 2rem;
        padding: 1rem 2rem;
        background: ${type === 'success' ? '#10b981' : '#3b82f6'};
        color: white;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

console.log('🐍 PyQuest loaded successfully!');
