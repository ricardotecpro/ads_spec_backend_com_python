"""
Testes automatizados para navegação do site
"""
import pytest
from playwright.sync_api import Page, expect


class TestNavigation:
    """Testes para navegação do site"""

    def test_home_page_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página inicial carrega"""
        page = page_with_base_url
        page.goto(base_url)
        
        expect(page).to_have_title("Python Backend - Curso Completo")

    def test_curso_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Curso' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Procura pelo item de menu "Curso"
        curso_menu = page.get_by_text("Curso", exact=False)
        expect(curso_menu).to_be_visible()

    def test_material_complementar_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Material Complementar' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Procura pelo item de menu "Material Complementar"
        material_menu = page.get_by_text("Material Complementar", exact=False)
        expect(material_menu).to_be_visible()

    def test_print_version_link_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o link 'Versão para Impressão' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Procura pelo link de impressão
        print_link = page.get_by_text("Versão para Impressão", exact=False)
        expect(print_link).to_be_visible()

    def test_navigation_to_lesson_01(self, page_with_base_url: Page, base_url: str):
        """Verifica se é possível navegar para Aula 01"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Clica no menu Curso (se necessário expandir)
        curso_menu = page.get_by_text("Curso", exact=False).first
        if curso_menu.is_visible():
            curso_menu.click()
        
        # Procura e clica no link da Aula 01
        aula_01_link = page.get_by_text("Aula 01", exact=False).first
        aula_01_link.click()
        
        # Verifica se chegou na página correta
        expect(page).to_have_url(f"{base_url}/01/")
        expect(page.locator("h1")).to_contain_text("Aula 01")
