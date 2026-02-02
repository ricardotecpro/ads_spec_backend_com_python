// Initialize Mermaid diagrams with error handling
document.addEventListener('DOMContentLoaded', function () {
    if (typeof mermaid !== 'undefined') {
        // Detect theme
        const isDark = document.body.getAttribute('data-md-color-scheme') === 'slate';

        // Configure Mermaid
        mermaid.initialize({
            startOnLoad: true,
            theme: isDark ? 'dark' : 'default',
            securityLevel: 'loose',
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'basis',
                padding: 15
            },
            themeVariables: {
                primaryColor: isDark ? '#82aaff' : '#1976d2',
                primaryTextColor: isDark ? '#fff' : '#000',
                primaryBorderColor: isDark ? '#82aaff' : '#1976d2',
                lineColor: isDark ? '#89ddff' : '#1976d2',
                secondaryColor: isDark ? '#c792ea' : '#ffc107',
                tertiaryColor: isDark ? '#ffcb6b' : '#4caf50'
            },
            logLevel: 'error' // Only show errors, not warnings
        });

        // Re-render on theme change
        const observer = new MutationObserver(function (mutations) {
            mutations.forEach(function (mutation) {
                if (mutation.attributeName === 'data-md-color-scheme') {
                    location.reload();
                }
            });
        });

        observer.observe(document.body, {
            attributes: true,
            attributeFilter: ['data-md-color-scheme']
        });

        console.log('✅ Mermaid initialized successfully');
    } else {
        console.error('❌ Mermaid library not loaded');
    }
});
