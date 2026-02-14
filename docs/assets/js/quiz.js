// Basic Quiz Interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log('Quiz JS loaded');
    const options = document.querySelectorAll('.quiz-option');

    options.forEach(option => {
        option.addEventListener('click', function () {
            // Remove selected from siblings
            const parent = this.parentElement;
            parent.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');

            // Check answer
            const isCorrect = this.getAttribute('data-correct') === 'true';
            const feedbackText = this.getAttribute('data-feedback');
            const feedbackEl = parent.querySelector('.quiz-feedback');

            if (feedbackEl) {
                feedbackEl.textContent = feedbackText || (isCorrect ? 'Correto!' : 'Incorreto.');
                feedbackEl.className = 'quiz-feedback ' + (isCorrect ? 'correct' : 'incorrect');
                feedbackEl.style.display = 'block';
            }
        });
    });
});
