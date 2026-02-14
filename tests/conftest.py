"""
Configuração compartilhada para testes com Playwright
"""
import pytest
from playwright.sync_api import Page, expect


# @pytest.fixture(scope="session")
# def base_url():
#     """URL base do servidor local MkDocs"""
#     return "http://127.0.0.1:8000"


@pytest.fixture
def page_with_base_url(page: Page, base_url: str):
    """Página do Playwright com URL base configurada"""
    page.set_default_timeout(10000)  # 10 segundos
    return page
