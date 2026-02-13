document.addEventListener("DOMContentLoaded", function () {
    const quizzes = document.querySelectorAll(".quiz-container");

    quizzes.forEach((quiz) => {
        const options = quiz.querySelectorAll(".quiz-option");
        const feedback = quiz.querySelector(".quiz-feedback");

        options.forEach((option) => {
            option.addEventListener("click", function () {
                // Reset state
                options.forEach((opt) => {
                    opt.classList.remove("selected", "correct", "incorrect");
                    opt.style.pointerEvents = "none"; // Disable further clicks
                });

                this.classList.add("selected");

                const isCorrect = this.getAttribute("data-correct") === "true";

                if (isCorrect) {
                    this.classList.add("correct");
                    feedback.textContent = "✅ Correto! " + (this.getAttribute("data-feedback") || "");
                    feedback.className = "quiz-feedback correct";
                } else {
                    this.classList.add("incorrect");
                    feedback.textContent = "❌ Incorreto. " + (this.getAttribute("data-feedback") || "");
                    feedback.className = "quiz-feedback incorrect";
                    
                    // Highlight the correct answer
                    options.forEach(opt => {
                        if (opt.getAttribute("data-correct") === "true") {
                            opt.classList.add("correct");
                        }
                    });
                }
                
                feedback.style.display = "block";
            });
        });
    });
});
