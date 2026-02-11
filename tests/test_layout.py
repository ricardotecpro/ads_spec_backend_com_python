import pytest
import os
import subprocess
import requests
from pathlib import Path
from playwright.sync_api import Page, expect

# Fixture to start a local HTTP server for testing
@pytest.fixture(scope="session")
def http_server():
    """Start a local HTTP server to serve the built site."""
    from time import sleep
    
    site_dir = Path("site").absolute()
    
    # Start HTTP server in background
    server_process = subprocess.Popen(
        ["python", "-m", "http.server", "8765", "--directory", str(site_dir)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to be ready with retry
    base_url = "http://localhost:8765"
    max_retries = 10
    for i in range(max_retries):
        try:
            response = requests.get(base_url, timeout=1)
            if response.status_code == 200:
                break
        except requests.exceptions.RequestException:
            if i == max_retries - 1:
                server_process.terminate()
                raise Exception("HTTP server failed to start")
            sleep(1)
    
    yield base_url
    
    # Cleanup: terminate server
    server_process.terminate()
    server_process.wait()

# Test 1: Verify build output files exist
def test_build_output_exists():
    """Verify that all expected build output files exist."""
    assert os.path.exists("site/index.html"), "Main index.html not found"
    assert os.path.exists("site/aulas/python_basico/index.html"), "Python básico page not found"
    assert os.path.exists("site/aulas/python_avancado/index.html"), "Python avançado page not found"
    assert os.path.exists("site/slides/index.html"), "Slides index not found"
    assert os.path.exists("site/assets/images/python_ecosystem.png"), "Python ecosystem image not found"
    assert os.path.exists("site/assets/images/virtual_env.png"), "Virtual env image not found"
    assert os.path.exists("site/assets/js/quiz.js"), "Quiz JS not found"
    assert os.path.exists("site/assets/css/quiz.css"), "Quiz CSS not found"

# Test 2: Homepage structure and content
def test_homepage_structure(page: Page, http_server):
    """Test that the homepage loads and has correct structure."""
    page.goto(http_server)
    
    # Check title
    expect(page).to_have_title("Home - Curso de Python")
    
    # Check main heading
    heading = page.locator("h1")
    expect(heading).to_contain_text("Curso de Python")
    
    # Check navigation cards exist
    cards = page.locator(".grid.cards")
    expect(cards).to_be_visible()

# Test 3: Navigation to Python Básico
def test_python_basico_page(page: Page, http_server):
    """Test Python Básico page loads and has correct content."""
    page.goto(f"{http_server}/aulas/python_basico/")
    
    # Check title
    expect(page).to_have_title("🐍 Python: A Linguagem Versátil e Poderosa - Curso de Python")
    
    # Check main heading
    heading = page.locator("h1")
    expect(heading).to_contain_text("Python: A Linguagem Versátil e Poderosa")
    
    # Check that images are loaded
    ecosystem_img = page.locator("img[alt='Ecossistema Python']")
    expect(ecosystem_img).to_be_visible()
    
    # Check quiz containers exist
    quiz_containers = page.locator(".quiz-container")
    expect(quiz_containers).to_have_count(3)

# Test 4: Quiz interactivity
def test_quiz_functionality(page: Page, http_server):
    """Test that quiz JavaScript works correctly."""
    page.goto(f"{http_server}/aulas/python_basico/")
    
    # Wait for quiz to be visible
    first_quiz = page.locator(".quiz-container").first
    expect(first_quiz).to_be_visible()
    
    # Click on the correct answer (first option in first quiz)
    correct_option = first_quiz.locator(".quiz-option[data-correct='true']")
    correct_option.click()
    
    # Check that feedback is displayed
    feedback = first_quiz.locator(".quiz-feedback")
    expect(feedback).to_be_visible()
    expect(feedback).to_contain_text("Correto")

# Test 5: Slides generation
def test_slides_structure(page: Page, http_server):
    """Test that slides are generated correctly."""
    page.goto(f"{http_server}/slides/")
    
    # Check title contains "Slides"
    title = page.title()
    assert "Slides" in title, f"Expected 'Slides' in title, got: {title}"
    
    # Check navigation exists
    navbar = page.locator(".navbar")
    expect(navbar).to_be_visible()
    
    # Check content is present
    content = page.locator(".col-md-9")
    expect(content).to_be_visible()

# Test 6: Python Avançado page
def test_python_avancado_page(page: Page, http_server):
    """Test Python Avançado page loads correctly."""
    page.goto(f"{http_server}/aulas/python_avancado/")
    
    # Check title
    expect(page).to_have_title("Python: Do Básico ao Avançado 🐍 - Curso de Python")
    
    # Check virtual env image
    venv_img = page.locator("img[alt='Ambientes Virtuais']")
    expect(venv_img).to_be_visible()
    
    # Check quiz containers
    quiz_containers = page.locator(".quiz-container")
    expect(quiz_containers).to_have_count(3)

# Test 7: Mermaid diagram rendering (if enabled)
def test_mermaid_diagram(page: Page, http_server):
    """Test that Mermaid diagrams are present in the content."""
    page.goto(f"{http_server}/aulas/python_basico/")
    
    # Check for mermaid code block
    mermaid_code = page.locator("code.language-mermaid")
    expect(mermaid_code).to_be_visible()

# Test 8: Assets loading
def test_assets_load(page: Page, http_server):
    """Test that CSS and JS assets load correctly."""
    page.goto(f"{http_server}/aulas/python_basico/")
    
    # Check that quiz.js is loaded
    quiz_script = page.locator("script[src*='quiz.js']")
    expect(quiz_script).to_be_attached()
    
    # Check that quiz.css is loaded
    # Note: CSS is loaded via link tag, we can check if styles are applied
    quiz_container = page.locator(".quiz-container").first
    expect(quiz_container).to_have_css("border-radius", "8px")
