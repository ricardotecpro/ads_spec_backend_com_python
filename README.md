# 🐍 Python Backend - Curso Completo

Curso completo de Python do zero ao avançado, com foco em desenvolvimento backend.

## 🎯 Sobre o Curso

Este curso oferece uma trilha completa de aprendizado em Python, desde os conceitos básicos até tópicos avançados de backend development.

### ✨ Destaques

- ✅ **Aulas Completas** - Material didático detalhado
- ✅ **Slides Profissionais** - Apresentações com Marp
- ✅ **Quizzes Interativos** - Teste seus conhecimentos
- ✅ **Exercícios Práticos** - Mão na massa
- ✅ **Projetos Reais** - Construa seu portfólio

## 🚀 Começando

### Pré-requisitos

- Python 3.11+
- Poetry
- Node.js (para Marp CLI)

### Instalação

```bash
# Clonar repositório
git clone https://github.com/ricardotecpro/ads_spec_backend_com_python.git
cd ads_spec_backend_com_python

# Instalar Poetry (se não tiver)
pip install poetry

# Instalar dependências
poetry install

# Instalar Marp CLI (opcional, para slides)
npm install -g @marp-team/marp-cli
```

## 📚 Comandos Disponíveis

### Com Poetry/Taskipy

```bash
# Servidor local
poetry run task serve

# Build do site
poetry run task build

# Gerar slides
poetry run task slides

# Executar testes
poetry run task test

# Deploy (com Mike)
poetry run task deploy
```

### Com Invoke

```bash
# Limpar arquivos gerados
invoke clean

# Build completo (slides + site)
invoke build-all

# Servidor local
invoke serve-all

# Atualizar dependências
invoke update-deps

# Ver todos os comandos
invoke help-tasks
```

## 📁 Estrutura do Projeto

```
ads_spec_backend_com_python/
├── aulas/                      # Conteúdo das aulas
│   ├── assets/                # Imagens, CSS, JS
│   ├── aulas/                 # Aulas (Python Básico, Avançado)
│   ├── quiz/                  # Quizzes interativos
│   ├── setup/                 # Guias de instalação
│   └── index.md               # Homepage
├── slides/                    # Slides Marp
│   ├── brutos/               # Slides fonte (.md)
│   │   ├── python-theme.css # Tema customizado
│   │   └── *.md             # Slides
│   └── html/                 # Slides gerados (.html)
├── hooks/                     # Hooks customizados MkDocs
│   ├── copy_slides.py        # Copia slides para site
│   └── quiz_hook.py          # Processa quizzes
├── .github/workflows/         # CI/CD
│   ├── deploy.yml            # Deploy automático
│   └── test.yml              # Testes automáticos
├── pyproject.toml            # Poetry + Taskipy
├── tasks.py                  # Invoke tasks
└── mkdocs.yml                # Configuração MkDocs
```

## 🎨 Tecnologias

### Documentação
- **MkDocs** - Gerador de sites estáticos
- **Material for MkDocs** - Tema moderno
- **Mike** - Versionamento de docs

### Slides
- **Marp** - Slides profissionais em Markdown
- **Tema Python** - Cores oficiais Python.org

### Automação
- **Poetry** - Gerenciamento de dependências
- **Taskipy** - Tasks simples
- **Invoke** - Tasks complexas

### Plugins
- **mkdocs-quiz** - Quizzes interativos
- **git-authors** - Autores por arquivo
- **git-revision-date** - Data de modificação
- **glightbox** - Lightbox para imagens
- **macros** - Variáveis e macros

### CI/CD
- **GitHub Actions** - Deploy e testes automáticos

## 🎓 Conteúdo

### Instalação
- Windows Setup
- VSCode Configuration

### Python Básico
- Sintaxe
- Tipos de dados
- Estruturas de controle
- Funções
- Módulos

### Python Avançado
- Ambientes virtuais
- Gerenciamento de pacotes (Poetry)
- POO avançada
- Decoradores
- Context managers

### Projetos
- API REST com FastAPI
- CRUD completo
- Autenticação
- Deploy

## 🧪 Testes

```bash
# Executar testes
poetry run task test

# Testar links
invoke test-links
```

## 🚀 Deploy

### GitHub Pages (Automático)

O deploy é automático via GitHub Actions quando você faz push para `main`.

### Manual

```bash
# Deploy com Mike
poetry run task deploy

# Ou
poetry run mike deploy estavel --push
```

## 🎨 Slides

### Gerar Slides

```bash
# Com Taskipy
poetry run task slides

# Com Marp diretamente
marp -I slides/brutos --html --theme slides/brutos/python-theme.css -o slides/html
```

### Visualizar Slides

Após gerar, abra os arquivos em `slides/html/` no navegador.

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Add nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Ricardo**

- GitHub: [@ricardotecpro](https://github.com/ricardotecpro)
- LinkedIn: [ricardotecpro](https://linkedin.com/in/ricardotecpro)

## 🙏 Agradecimentos

- [FastAPI do Zero](https://github.com/dunossauro/fastapi-do-zero) - Inspiração para estrutura e automação
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) - Tema incrível
- [Marp](https://marp.app/) - Slides profissionais
- Comunidade Python Brasil

---

⭐ Se este projeto te ajudou, considere dar uma estrela!
