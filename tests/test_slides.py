"""
Testes automatizados para verificar renderização de slides com RevealJS
"""
import pytest
from playwright.sync_api import Page, expect


class TestSlides:
    """Testes para slides RevealJS"""

    def test_slides_index_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página de índice de slides carrega"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/")
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")
        expect(page.locator("h1")).to_contain_text("Slides")

    @pytest.mark.parametrize("lesson_number", range(1, 17))
    def test_slide_page_loads(self, page_with_base_url: Page, base_url: str, lesson_number: int):
        """Verifica se cada página de slide carrega sem erro 404"""
        page = page_with_base_url
        slide_url = f"{base_url}/slides/{lesson_number:02d}-slides/"
        
        page.goto(slide_url)
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")

    def test_revealjs_present_on_slide_01(self, page_with_base_url: Page, base_url: str):
        """Verifica se RevealJS está presente no slide 01"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/01-slides/")
        
        # Verifica se a estrutura RevealJS existe
        # RevealJS usa a classe .reveal como container principal
        reveal_container = page.locator(".reveal")
        
        # Se RevealJS estiver funcionando, deve haver um container .reveal
        expect(reveal_container).to_be_visible()

    def test_slide_navigation_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se controles de navegação de slides existem"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/01-slides/")
        
        # RevealJS adiciona controles de navegação
        # Procura por elementos típicos de navegação
        controls = page.locator(".navigate-right, .navigate-left, .navigate-up, .navigate-down")
        
        # Deve haver pelo menos um controle de navegação
        expect(controls.first).to_be_visible()

    def test_slide_content_visible(self, page_with_base_url: Page, base_url: str):
        """Verifica se o conteúdo do slide está visível"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/01-slides/")
        
        # Verifica se há conteúdo de slide visível
        # RevealJS usa .slides como container de slides
        slides_container = page.locator(".slides")
        expect(slides_container).to_be_visible()
        
        # Verifica se há pelo menos um slide
        slide = page.locator(".slides section").first
        expect(slide).to_be_visible()
