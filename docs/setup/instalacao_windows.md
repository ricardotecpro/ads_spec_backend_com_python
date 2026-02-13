# Configuração do Ambiente (Windows)

Este guia irá ajudá-lo a configurar o ambiente de desenvolvimento Python no Windows usando o Visual Studio Code (VSCode).

## 1. Instalando o Python

O Python é a linguagem que usaremos. O interpretador é o programa que lê seu código e diz ao computador o que fazer.

### Passo 1: Baixar
1. Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/).
2. Clique no botão amarelo **Download Python 3.x.x** (a versão mais recente).

### Passo 2: Instalar (MUITO IMPORTANTE!)
1. Execute o instalador baixado (`python-3.x.x-amd64.exe`).
2. **⚠️ ANTES DE CLICAR EM INSTALL, MARQUE A CAIXA:**
   **[x] Add Python 3.x to PATH**
   *(Se você esquecer isso, o Python não vai funcionar no terminal)*.
3. Clique em **Install Now**.
4. Aguarde o final e clique em **Close**.

### Passo 3: Testar
1. Abra o **Menu Iniciar** e digite `cmd` ou `PowerShell`. Abra-o.
2. Digite o comando:
   ```powershell
   python --version
   ```
3. Se aparecer algo como `Python 3.12.0`, parabéns! Está instalado.

---

## 2. Instalando o Visual Studio Code (VSCode)

O VSCode é o editor de texto onde escreveremos nosso código. Ele é leve, poderoso e gratuito.

1. Acesse: [code.visualstudio.com](https://code.visualstudio.com/).
2. Baixe a versão para **Windows**.
3. Instale com as opções padrão (Next, Next, Install).

---

## 3. Configurando o VSCode para Python

Para o VSCode entender Python e ajudar com cores e autocompletar, precisamos de uma extensão.

1. Abra o VSCode.
2. No menu lateral esquerdo, clique no ícone de quadrados (**Extensions**) ou aperte `Ctrl+Shift+X`.
3. Na barra de busca, digite `Python`.
4. Clique na primeira opção (criada pela **Microsoft**) e clique em **Install**.
5. Aguarde a instalação finalizar (pode pedir para recarregar).

---

## 4. Seu primeiro teste no VSCode

1. Crie uma pasta no seu computador para o curso (ex: `MeusEstudosPython`).
2. No VSCode, vá em **File > Open Folder** e abra essa pasta.
3. Crie um arquivo novo chamado `teste.py`.
4. Escreva:
   ```python
   print("Configuração concluída com sucesso!")
   ```
5. Para rodar, clique no botão de **Play ▷** no canto superior direito (ou aperte `F5`).
6. A mensagem deve aparecer no terminal na parte de baixo da tela.

---

🎉 **Pronto! Seu ambiente está configurado.**
