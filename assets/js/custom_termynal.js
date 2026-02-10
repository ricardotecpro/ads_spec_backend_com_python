// Custom Termynal Reload Script
// Adds a reload button to all .termynal containers

document.addEventListener("DOMContentLoaded", function () {
    // Wait a brief moment to ensure Termynal has initialized (if it's async)
    setTimeout(() => {
        const terminals = document.querySelectorAll(".termynal");

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

                // Check if Termynal is available
                if (typeof Termynal === 'undefined') {
                    console.error("Termynal library not loaded.");
                    return;
                }

                // Remove the button temporarily so it isn't affected (optional, but safe)
                btn.remove();

                // Re-initialize
                // We create a new instance on the same container.
                // Termynal's constructor resets the lines' styles (visibilty/opacity).
                try {
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
