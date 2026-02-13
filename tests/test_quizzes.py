"""
Testes automatizados para verificar interatividade de quizzes
"""
import pytest
from playwright.sync_api import Page, expect


class TestQuizzes:
    """Testes para quizzes interativos"""

    def test_quiz_index_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página de índice de quizzes carrega"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/")
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")
        expect(page.locator("h1")).to_contain_text("Quiz")

    @pytest.mark.parametrize("quiz_number", range(1, 17))
    def test_quiz_page_loads(self, page_with_base_url: Page, base_url: str, quiz_number: int):
        """Verifica se cada página de quiz carrega sem erro 404"""
        page = page_with_base_url
        quiz_url = f"{base_url}/quizzes/quiz-{quiz_number:02d}/"
        
        page.goto(quiz_url)
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")

    def test_quiz_has_interactive_elements(self, page_with_base_url: Page, base_url: str):
        """Verifica se o quiz 01 tem elementos interativos"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/quiz-01/")
        
        # Procura por inputs de radio ou checkbox
        # O plugin mkdocs-quiz pode usar diferentes estruturas
        inputs = page.locator("input[type='radio'], input[type='checkbox']")
        
        # Deve haver pelo menos um input (5 perguntas com múltiplas opções)
        expect(inputs.first).to_be_visible()

    def test_quiz_questions_visible(self, page_with_base_url: Page, base_url: str):
        """Verifica se as perguntas do quiz estão visíveis"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/quiz-01/")
        
        # Verifica se há texto de pergunta
        # Procura pela primeira pergunta conhecida
        question_text = page.get_by_text("O que é um algoritmo?")
        expect(question_text).to_be_visible()

    def test_quiz_can_select_answer(self, page_with_base_url: Page, base_url: str):
        """Verifica se é possível selecionar uma resposta"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/quiz-01/")
        
        # Tenta encontrar e clicar em um input
        first_input = page.locator("input[type='radio'], input[type='checkbox']").first
        
        if first_input.is_visible():
            # Clica no input
            first_input.click()
            
            # Verifica se foi selecionado
            expect(first_input).to_be_checked()

    def test_quiz_has_multiple_questions(self, page_with_base_url: Page, base_url: str):
        """Verifica se o quiz tem múltiplas perguntas (pelo menos 5)"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/quiz-01/")
        
        # Procura por marcadores de lista numerada (perguntas)
        # As perguntas são formatadas como "1. ", "2. ", etc.
        questions = page.locator("text=/^\\d+\\.\\s+/")
        
        # Deve haver pelo menos 5 perguntas
        expect(questions).to_have_count(5, timeout=5000)
