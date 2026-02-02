"""
Hook para copiar slides HTML gerados para o site após build
"""
import shutil
import pathlib
from rich import print


def copy_slides(config, **kwargs):
    """
    Copia slides HTML do diretório slides/html/ para site/slides/
    após o build do MkDocs
    
    Args:
        config: Configuração do MkDocs
        **kwargs: Argumentos adicionais
    """
    site_dir = config['site_dir']
    slides_path = pathlib.Path(site_dir) / 'slides'
    slides_path.mkdir(exist_ok=True)
    
    # Verificar se existem slides para copiar
    slides_source = pathlib.Path('slides/html')
    if not slides_source.exists():
        print("[yellow]⚠ Pasta slides/html/ não encontrada[/yellow]")
        return
    
    # Copiar todos os slides HTML
    slides_copied = 0
    for slide in slides_source.glob('*.html'):
        shutil.copy(slide.resolve(), slides_path.resolve())
        slides_copied += 1
    
    if slides_copied > 0:
        print(f"[green]✓ {slides_copied} slide(s) copiado(s) para {slides_path}[/green]")
    else:
        print("[yellow]⚠ Nenhum slide HTML encontrado em slides/html/[/yellow]")
