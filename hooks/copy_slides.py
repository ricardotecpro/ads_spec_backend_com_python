"""
Hook para copiar slides HTML gerados para o site após build
"""
import shutil
import pathlib
from rich import print


def copy_slides(config, **kwargs):
    """
    Copia slides HTML e Markdown do diretório docs/slides/ para site/slides/
    após o build do MkDocs
    
    Args:
        config: Configuração do MkDocs
        **kwargs: Argumentos adicionais
    """
    site_dir = config['site_dir']
    slides_dest = pathlib.Path(site_dir) / 'slides'
    slides_dest.mkdir(exist_ok=True)
    
    # Diretório fonte dos slides
    slides_source = pathlib.Path('docs/slides')
    if not slides_source.exists():
        print("[yellow]⚠ Pasta docs/slides/ não encontrada[/yellow]")
        return
    
    # Copiar todos os slides HTML e Markdown
    html_copied = 0
    md_copied = 0
    
    # Copiar HTML
    for slide in slides_source.glob('*.html'):
        shutil.copy(slide.resolve(), slides_dest.resolve())
        html_copied += 1
    
    # Copiar Markdown
    for slide in slides_source.glob('*-slides.md'):
        shutil.copy(slide.resolve(), slides_dest.resolve())
        md_copied += 1
    
    if html_copied > 0:
        print(f"[green]✓ {html_copied} slide(s) HTML copiado(s) para {slides_dest}[/green]")
    if md_copied > 0:
        print(f"[green]✓ {md_copied} slide(s) Markdown copiado(s) para {slides_dest}[/green]")
    
    if html_copied == 0 and md_copied == 0:
        print("[yellow]⚠ Nenhum slide encontrado em docs/slides/[/yellow]")


def on_post_build(config):
    """Hook chamado após o build do MkDocs"""
    copy_slides(config)
