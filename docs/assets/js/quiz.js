// Basic Quiz Interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log('Quiz JS loaded');
    const options = document.querySelectorAll('.quiz-option');

    options.forEach(option => {
        option.addEventListener('click', function () {
            // Prevent multiple clicks if already answered
            // Allow changing answer: Remove state from siblings
            parent.querySelectorAll('.quiz-option').forEach(opt => {
                opt.classList.remove('selected', 'correct', 'incorrect');
                // We don't use 'disabled' anymore to allow switching
                opt.classList.remove('disabled');
            });

            this.classList.add('selected');

            // Check answer
            const isCorrect = this.getAttribute('data-correct') === 'true';
            const feedbackText = this.getAttribute('data-feedback');
            const feedbackEl = parent.querySelector('.quiz-feedback');

            // Apply visual state to the option
            this.classList.add(isCorrect ? 'correct' : 'incorrect');

            // Optional: You could disable *after* a correct answer if you wanted to lock it then,
            // but the request is to allow changing, so we keep it open or just visual.
            // parent.querySelectorAll('.quiz-option').forEach(opt => opt.classList.add('disabled'));

            if (feedbackEl) {
                feedbackEl.innerHTML = (isCorrect ? '<strong>Correto!</strong> ' : '<strong>Incorreto.</strong> ') + (feedbackText || '');
                feedbackEl.className = 'quiz-feedback ' + (isCorrect ? 'correct' : 'incorrect');
                feedbackEl.style.display = 'block';
            }
        });
    });
});
