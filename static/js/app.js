// PyQuest - Frontend JavaScript

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

// Confirmation before leaving page with unsaved code
let codeChanged = false;
const codeEditor = document.getElementById('codeEditor');

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

// Auto-save code to localStorage
if (codeEditor) {
    const challengeId = window.location.pathname;
    
    // Load saved code
    const savedCode = localStorage.getItem(`code_${challengeId}`);
    if (savedCode && confirm('Resume from saved code?')) {
        codeEditor.value = savedCode;
    }
    
    // Save code periodically
    setInterval(() => {
        if (codeEditor.value) {
            localStorage.setItem(`code_${challengeId}`, codeEditor.value);
        }
    }, 30000); // Every 30 seconds
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
