// Custom Termynal Reload Script
// Adds a reload button to all .termynal containers

document.addEventListener("DOMContentLoaded", function () {
    // Wait a brief moment to ensure Termynal has initialized (if it's async)
    setTimeout(() => {
        const terminals = document.querySelectorAll(".termynal");

        // Safety check if Termynal library is available
        if (typeof Termynal === 'undefined') {
            console.warn("Termynal library not loaded or not globally available.");
            return;
        }

        terminals.forEach(term => {
            // Prevent duplicates
            if (term.querySelector('.termynal-reload-btn')) return;

            // Create button
            const btn = document.createElement("button");
            btn.innerHTML = "&#x21bb;"; // Clockwise Open Circle Arrow
            btn.className = "termynal-reload-btn";
            btn.setAttribute('aria-label', 'Reiniciar animação');
            btn.title = "Reiniciar";

            // Add button to terminal
            term.appendChild(btn);

            // Handle click
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                e.stopPropagation();

                // Remove the button temporarily so it isn't affected
                btn.remove();

                // Reset specific Termynal attributes/styles to force re-animation
                // Termynal usually adds styles to lines. We need to clear them.
                const lines = term.querySelectorAll('[data-ty]');
                lines.forEach(line => {
                    // Reset visibility and display styles
                    line.style.opacity = '';
                    line.style.visibility = '';
                    line.style.display = '';
                    // Remove any inline styles Termynal might have added
                    line.removeAttribute('style');

                    // Termynal might add data attributes for state, but usually it relies on 'data-ty'
                    // Standard Termynal.js uses 'data-ty-prompt' to add prompt. 
                    // If plugin added prompt via JS, we might have issues, but usually it's in HTML.
                });

                // Remove any dynamically added cursor elements if Termynal adds them
                const cursors = term.querySelectorAll('[data-ty-cursor]');
                cursors.forEach(c => c.remove());

                // Re-initialize
                try {
                    // Check if there are options stored in data attributes of the container
                    // Termynal constructor will pick up data-termynal, data-ty-typeDelay, etc.
                    new Termynal(term);
                } catch (err) {
                    console.error("Error restarting Termynal:", err);
                }

                // Add button back
                term.appendChild(btn);
            });
        });
    }, 500); // 500ms delay to be safe
});
