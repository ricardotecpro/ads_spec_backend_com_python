"""
Script para gerar automaticamente todos os slides HTML e quizzes interativos
Baseado nos formatos antigos que funcionavam
"""
import pathlib
from rich import print
from rich.progress import track


def generate_slide_html(lesson_number: int) -> str:
    """Gera HTML para um slide específico"""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula {lesson_number:02d} - Python Backend</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/theme/black.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/highlight/monokai.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="{lesson_number:02d}-slides.md"
                     data-separator="^\\n---\\n$"
                     data-separator-vertical="^\\n--\\n$">
            </section>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/highlight/highlight.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/notes/notes.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        }});
    </script>
</body>
</html>
'''


def clean_slide_markdown(md_path: pathlib.Path) -> None:
    """Remove frontmatter YAML dos slides markdown"""
    content = md_path.read_text(encoding='utf-8')
    
    # Remove frontmatter se existir
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # Remove tudo até o segundo ---
            content = parts[2].lstrip()
            
            # Remove comentários Marp
            lines = content.split('\n')
            cleaned_lines = [line for line in lines if not line.strip().startswith('<!-- _class:')]
            content = '\n'.join(cleaned_lines)
            
            md_path.write_text(content, encoding='utf-8')
            print(f"  [green]✓[/green] Limpou frontmatter de {md_path.name}")


def generate_all_slides():
    """Gera arquivos HTML para todos os 16 slides"""
    slides_dir = pathlib.Path('docs/slides')
    
    print("\n[bold cyan]📊 Gerando Slides HTML...[/bold cyan]")
    
    for i in track(range(1, 17), description="Processando slides..."):
        # Gerar HTML
        html_path = slides_dir / f"{i:02d}-slides.html"
        html_content = generate_slide_html(i)
        html_path.write_text(html_content, encoding='utf-8')
        
        # Limpar markdown
        md_path = slides_dir / f"{i:02d}-slides.md"
        if md_path.exists():
            clean_slide_markdown(md_path)
    
    print(f"[green]✓ {16} slides HTML gerados com sucesso![/green]")


def convert_quiz_to_html(quiz_number: int) -> str:
    """Lê quiz markdown e retorna versão HTML (placeholder - precisa ser implementado)"""
    # Por enquanto retorna template básico
    # Você precisará implementar a conversão real baseado no conteúdo
    return f'''# Quiz {quiz_number:02d}

--8<-- "assets/quiz.html"

<!-- Adicione as perguntas aqui no formato HTML -->
<div class="quiz-container">
  <div class="quiz-question">Pergunta de exemplo</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto!">Opção correta</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">Opção incorreta</div>
  <div class="quiz-feedback"></div>
</div>
'''


def main():
    """Função principal"""
    print("[bold]🚀 Automação de Slides e Quizzes[/bold]")
    print("=" * 50)
    
    generate_all_slides()
    
    print("\n[yellow]⚠ Nota:[/yellow] Quizzes precisam ser convertidos manualmente")
    print("  Use o template em docs/quizzes/quiz-01.md como referência")
    
    print("\n[green]✅ Automação concluída![/green]")


if __name__ == '__main__':
    main()
