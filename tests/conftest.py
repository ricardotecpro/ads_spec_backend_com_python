"""
Configuração compartilhada para testes com Playwright
"""
import pytest
import subprocess
import requests
import os
from pathlib import Path
from time import sleep
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def base_url():
    """
    Inicia um servidor HTTP local para servir o site gerado (site/)
    e retorna a URL base.
    """
    site_dir = Path("site").absolute()
    
    # Verifica se o site foi gerado
    if not site_dir.exists() or not (site_dir / "index.html").exists():
        pytest.fail("Diretório 'site/' não encontrado ou inválido. Execute 'poetry run task build' antes dos testes.")

    # Porta fixa para teste
    port = "8766"
    base_url = f"http://localhost:{port}"
    
    # Start HTTP server in background
    server_process = subprocess.Popen(
        ["python", "-m", "http.server", port, "--directory", str(site_dir)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to be ready with retry
    max_retries = 10
    server_started = False
    
    for i in range(max_retries):
        try:
            response = requests.get(base_url, timeout=1)
            if response.status_code == 200:
                server_started = True
                break
        except requests.exceptions.RequestException:
            sleep(1)
            
    if not server_started:
        server_process.terminate()
        pytest.fail(f"Servidor HTTP falhou ao iniciar em {base_url}")
    
    yield base_url
    
    # Cleanup: terminate server
    server_process.terminate()
    server_process.wait()


@pytest.fixture
def page_with_base_url(page: Page, base_url: str):
    """Página do Playwright com URL base configurada"""
    page.set_default_timeout(10000)  # 10 segundos
    return page
