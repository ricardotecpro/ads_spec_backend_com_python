// Basic Quiz Interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log('Quiz JS loaded');
    const options = document.querySelectorAll('.quiz-option');

    options.forEach(option => {
        option.addEventListener('click', function () {
            // Prevent multiple clicks if already answered
            const parent = this.parentElement;
            if (parent.querySelector('.quiz-option.correct') || parent.querySelector('.quiz-option.incorrect')) {
                return;
            }

            // Remove selected from siblings
            parent.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');

            // Check answer
            const isCorrect = this.getAttribute('data-correct') === 'true';
            const feedbackText = this.getAttribute('data-feedback');
            const feedbackEl = parent.querySelector('.quiz-feedback');

            // Apply visual state to the option
            this.classList.add(isCorrect ? 'correct' : 'incorrect');

            // Disable other options visually
            parent.querySelectorAll('.quiz-option').forEach(opt => opt.classList.add('disabled'));

            if (feedbackEl) {
                feedbackEl.innerHTML = (isCorrect ? '<strong>Correto!</strong> ' : '<strong>Incorreto.</strong> ') + (feedbackText || '');
                feedbackEl.className = 'quiz-feedback ' + (isCorrect ? 'correct' : 'incorrect');
                feedbackEl.style.display = 'block';
            }
        });
    });
});
