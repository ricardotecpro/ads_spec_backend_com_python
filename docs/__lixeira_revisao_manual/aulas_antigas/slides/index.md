---
hide:
  - navigation
  - toc
---

<style>
.slides-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.slides-hero {
  text-align: center;
  padding: 3rem 0;
  background: linear-gradient(135deg, #306998 0%, #FFD43B 100%);
  border-radius: 15px;
  margin-bottom: 3rem;
  color: white;
}

.slides-hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.slides-hero p {
  font-size: 1.3rem;
  opacity: 0.95;
}

.slides-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.slide-card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  border-left: 5px solid #306998;
}

.slide-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.slide-card h3 {
  color: #306998;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.slide-card p {
  color: #666;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.slide-link {
  display: inline-block;
  background: linear-gradient(135deg, #306998 0%, #4a7ba7 100%);
  color: white !important;
  padding: 0.8rem 1.5rem;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 600;
  transition: transform 0.2s, box-shadow 0.2s;
}

.slide-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(48, 105, 152, 0.3);
}

.instructions {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 2rem;
  margin: 3rem 0;
  border-left: 5px solid #FFD43B;
}

.instructions h2 {
  color: #306998;
  margin-bottom: 1rem;
}

.instructions ul {
  margin-left: 2rem;
}

.instructions li {
  margin: 0.5rem 0;
  line-height: 1.6;
}

.instructions code {
  background: rgba(48, 105, 152, 0.1);
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  color: #306998;
}

@media (prefers-color-scheme: dark) {
  .slide-card {
    background: #1e1e1e;
    color: #e0e0e0;
  }
  
  .slide-card h3 {
    color: #FFD43B;
  }
  
  .slide-card p {
    color: #b0b0b0;
  }
  
  .instructions {
    background: #2a2a2a;
    color: #e0e0e0;
  }
  
  .instructions h2 {
    color: #FFD43B;
  }
}
</style>

<div class="slides-container">

<div class="slides-hero">
  <h1>📊 Slides do Curso</h1>
  <p>Apresentações profissionais criadas com Marp</p>
</div>

## 🎯 Slides Disponíveis

<div class="slides-grid">

<div class="slide-card">
  <h3>🐍 Introdução ao Python</h3>
  <p>Apresentação completa sobre o curso, objetivos, metodologia e por que aprender Python.</p>
  <a href="../slides/00-introducao.html" class="slide-link" target="_blank">Ver Slide →</a>
</div>

<!-- Adicione mais cards aqui conforme criar novos slides -->

<div class="slide-card">
  <h3>⚡ Demonstração Reveal.js</h3>
  <p>Exemplo de slides com animações avançadas, fragmentos e transições.</p>
  <a href="../slides/revealjs/" class="slide-link" target="_blank">Ver Demo →</a>
</div>

</div>

<div class="instructions">

## 📖 Como Usar os Slides

### Navegação

- **Setas ← →** - Navegar entre slides
- **F11** - Modo tela cheia
- **ESC** - Sair do modo tela cheia
- **Home** - Primeiro slide
- **End** - Último slide

### Gerar Novos Slides

Para criar novos slides:

1. **Criar arquivo** em `slides/brutos/` (ex: `01-instalacao.md`)
2. **Usar formato Marp:**
   ```markdown
   ---
   marp: true
   theme: python
   paginate: true
   ---
   
   # Título do Slide
   
   Conteúdo aqui
   
   ---
   
   # Próximo Slide
   ```

3. **Gerar HTML:**
   ```bash
   poetry run task slides
   ```

4. **Adicionar link** nesta página

### Tema Python

Todos os slides usam o tema customizado `python-theme.css` com as cores oficiais do Python.org:

- 🔵 **Azul Python:** `#306998`
- 🟡 **Amarelo Python:** `#FFD43B`
- 🟠 **Laranja:** `#FFA500`

</div>

## 🔗 Recursos Adicionais

<div class="slides-grid">

<div class="slide-card">
  <h3>📚 Aulas Completas</h3>
  <p>Material didático detalhado com exemplos e explicações.</p>
  <a href="../aulas/python_basico/" class="slide-link">Ver Aulas →</a>
</div>

<div class="slide-card">
  <h3>🧠 Quizzes</h3>
  <p>Teste seus conhecimentos com quizzes interativos.</p>
  <a href="../quiz/" class="slide-link">Fazer Quizzes →</a>
</div>

<div class="slide-card">
  <h3>💻 Exercícios</h3>
  <p>Pratique com exercícios hands-on.</p>
  <a href="../exercicios/" class="slide-link">Ver Exercícios →</a>
</div>

</div>

</div>
