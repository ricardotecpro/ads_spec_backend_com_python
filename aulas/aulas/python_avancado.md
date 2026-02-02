# Python: Do Básico ao Avançado 🐍

Esta trilha foi desenhada para guiar você desde a instalação do Python até as boas práticas de desenvolvimento usadas por profissionais, cobrindo o gerenciamento de ambientes, dependências e o uso de ferramentas interativas.

-----

### **Seção 1: Fundamentos e Instalação 🛠️**

O primeiro passo é garantir que o Python esteja instalado em seu sistema. Você pode baixá-lo diretamente do [site oficial python.org](https://www.python.org/downloads/). Durante a instalação no Windows, é **altamente recomendado** marcar a opção "Add Python to PATH" para facilitar o uso do terminal.

-----

### **Seção 2: Ambientes Virtuais (`virtualenv`) 🌳**

![Ambientes Virtuais](../assets/images/virtual_env.png)

Ambientes virtuais são pastas isoladas que contêm uma instalação específica do Python e todas as bibliotecas necessárias para um único projeto. Usá-los é uma prática essencial para evitar conflitos de versão entre projetos.

**🤔 Por que usar?**
Imagine que o Projeto A precisa da biblioteca `pandas` versão 1.5, mas o Projeto B precisa da versão 2.0. Sem um ambiente virtual, você teria um conflito. Com ambientes virtuais, cada projeto tem seu próprio "mundo" de bibliotecas.

#### **1. Instalação do `virtualenv`**

Abra seu terminal (CMD ou PowerShell no Windows, Terminal no Linux/macOS) e execute:

```bash
pip install virtualenv
```

#### **2. Criação de um Ambiente Virtual**

Navegue até a pasta do seu projeto e crie o ambiente. O nome `venv` é uma convenção comum.

  * **Para Windows 💻 (CMD / PowerShell):**

    ```bash
    # Dentro da pasta do seu projeto
    virtualenv venv
    ```

  * **Para Linux e macOS 🐧 (Bash / Zsh):**

    ```bash
    # Dentro da pasta do seu projeto
    virtualenv venv
    ```

Isso criará uma pasta chamada `venv` dentro do diretório do seu projeto.

#### **3. Ativação do Ambiente Virtual ▶️**

Para começar a usar o ambiente, você precisa "ativá-lo".

  * **Para Windows 💻 (CMD / PowerShell):**

    ```bash
    # Executar o script de ativação
    .\venv\Scripts\activate
    ```

    Seu prompt do terminal mudará, mostrando `(venv)` no início.

  * **Para Linux e macOS 🐧 (Bash / Zsh):**

    ```bash
    # Executar o script de ativação
    source venv/bin/activate
    ```

    Seu prompt do terminal também mudará para indicar `(venv)`.

#### **4. Desativação do Ambiente ⏹️**

Quando terminar de trabalhar no projeto, basta digitar no terminal:

```bash
deactivate
```

**💡 Dica Profissional:** Sempre adicione a pasta do seu ambiente virtual (ex: `venv/`) ao seu arquivo `.gitignore` para não versionar as bibliotecas baixadas.

-----

### **Seção 3: Gerenciamento de Dependências (`requirements.txt`) 📦**

À medida que você instala bibliotecas em seu projeto (com o ambiente virtual ativado), é crucial registrar essas "dependências" para que outros desenvolvedores (ou você mesmo, em outro computador) possam recriar o ambiente facilmente.

#### **1. Instalando Pacotes ➕**

Com o ambiente ativado, use o `pip` para instalar pacotes.

```bash
# Exemplo: instalando a biblioteca pandas
pip install pandas
```

#### **2. Criando o `requirements.txt` ✍️**

Este arquivo é uma "lista de compras" de todas as bibliotecas que seu projeto utiliza. Para gerá-lo automaticamente, execute:

```bash
pip freeze > requirements.txt
```

Isso criará um arquivo `requirements.txt` na pasta do seu projeto com o conteúdo similar a:

```
pandas==2.2.0
numpy==1.26.4
...
```

#### **3. Instalando a partir de um `requirements.txt` 📥**

Quando outra pessoa (ou você) clona o projeto, basta criar e ativar um novo ambiente virtual e executar o seguinte comando para instalar todas as dependências de uma vez:

```bash
pip install -r requirements.txt
```

-----

### **Seção 4: Desenvolvimento Interativo (Jupyter Notebook) 📓**

Jupyter Notebooks são ideais para ciência de dados, análise, prototipagem e aprendizado, pois permitem executar blocos de código de forma interativa e visualizar os resultados imediatamente.

#### **1. Instalação do Jupyter 🚀**

Com seu ambiente virtual ativado, instale o Jupyter:

```bash
pip install jupyterlab
```

*`jupyterlab` é a versão mais moderna e recomendada, mas você também pode usar `pip install notebook` para a versão clássica.*

#### **2. Iniciando o JupyterLab**

No terminal, com o ambiente ativado e na pasta do seu projeto, execute:

```bash
jupyter lab
```

Isso abrirá uma nova aba em seu navegador com a interface do JupyterLab.

#### **3. Usando o Jupyter Notebook 🖱️**

  * Na interface do JupyterLab, você pode criar um novo "Notebook" (.ipynb).
  * Um notebook é composto por **células**. Você pode escrever código Python em uma célula.
  * Para executar o código em uma célula, pressione **`Shift + Enter`**. O resultado será exibido logo abaixo da célula.
  * Você também pode criar células de texto usando a formatação **Markdown** para documentar seu trabalho.

É uma ferramenta poderosa para testar ideias e apresentar análises de forma clara e organizada. Boa exploração\! 🎉

---

## 🎯 Teste Seus Conhecimentos

Agora que você domina os conceitos avançados, que tal testar seus conhecimentos?

<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #FFD43B 0%, #FFA500 100%); border-radius: 10px; margin: 2rem 0;">
  <h3 style="color: white; margin-bottom: 1rem;">🧠 Quiz de Fixação</h3>
  <p style="color: white; margin-bottom: 1.5rem;">
    Teste seus conhecimentos sobre Python Avançado com questões interativas!
  </p>
  <a href="/ads_spec_backend_com_python/quiz/python_avancado/" style="display: inline-block; background: white; color: #306998; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: bold; transition: transform 0.2s;">
    Fazer Quiz Agora →
  </a>
</div>

---

## 📚 Próximos Passos

Parabéns por completar a aula de Python Avançado! Continue sua jornada:

- 💪 **Praticar**: [Exercícios](../exercicios/index.md)
- 🎯 **Aplicar**: [Projetos](../projetos/index.md)
- 📖 **Revisar**: [Python Básico](python_basico.md)

