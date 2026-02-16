# Configuração do Ambiente (Linux Ubuntu)

Este guia mostra como instalar e configurar o Python e PyCharm no **Ubuntu** para desenvolvimento.

---

## 1. Instalando Python no Ubuntu

O Ubuntu já vem com Python instalado. Vamos verificar e atualizar se necessário.

### Verificar Versão Instalada

```bash
python3 --version
```

Se aparecer `Python 3.10` ou superior, você já tem Python! Caso contrário, instale:

### Instalar Python e Ferramentas

```bash
# Atualizar repositórios
sudo apt update

# Instalar Python 3 e ferramentas essenciais
sudo apt install python3 python3-pip python3-venv -y

# Verificar instalação
python3 --version
pip3 --version
```

**Saída esperada:**
```
Python 3.12.x
pip 24.x.x
```

---

## 2. Instalando e Configurando PyCharm no Ubuntu

PyCharm é a melhor IDE para Python, desenvolvida pela JetBrains.

### Método Recomendado: Via Snap

O Snap já vem instalado no Ubuntu. Use este método para instalação fácil:

```bash
# PyCharm Community (Gratuito e Open Source)
sudo snap install pycharm-community --classic

# OU PyCharm Professional (Pago, mas com 30 dias de trial)
sudo snap install pycharm-professional --classic
```

### Método Alternativo: Via Ubuntu Software

1. Abra **Ubuntu Software** (ícone de sacola de compras)
2. Busque por "PyCharm"
3. Clique em **Install**

### Abrir PyCharm

```bash
# Via terminal
pycharm-community

# OU via menu de aplicativos
# Pressione Super (tecla Windows) e digite "PyCharm"
```

---

## 3. Configuração Inicial do PyCharm

### Primeira Execução

1. **Aceite os Termos de Uso**
2. **Escolha o Tema:**
   - Light (Claro)
   - Darcula (Escuro) - Recomendado

3. **Criar Novo Projeto:**
   - Clique em **New Project**
   - Escolha o local: `~/PycharmProjects/MeuPrimeiroProjeto`
   - **Interpreter:** Selecione Python 3.x detectado automaticamente
   - Clique em **Create**

### Configurar Interpretador Python

Se o PyCharm não detectar automaticamente:

1. **File → Settings** (ou `Ctrl+Alt+S`)
2. **Project → Python Interpreter**
3. Clique no ícone de engrenagem → **Add**
4. Selecione **System Interpreter**
5. Escolha `/usr/bin/python3`

---

## 4. Criando Seu Primeiro Programa

1. **Criar arquivo:** Clique com botão direito no projeto → **New → Python File**
2. Nome: `hello.py`
3. Digite:

```python
print("Olá, Linux!")
print("Python está funcionando!")
```

4. **Executar:** Clique com botão direito no arquivo → **Run 'hello'**
   - Ou use o atalho: `Shift+F10`

---

## 5. Instalando Bibliotecas (pip)

### Via Terminal do PyCharm

1. **View → Tool Windows → Terminal** (ou `Alt+F12`)
2. Instalar biblioteca:

```bash
pip3 install requests
```

### Criar Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar
source venv/bin/activate

# Instalar bibliotecas
pip install requests flask pandas

# Desativar quando terminar
deactivate
```

---

## 6. Atalhos Úteis do PyCharm (Linux)

| Atalho | Ação |
|--------|------|
| `Ctrl+Space` | Auto-completar código |
| `Shift+F10` | Executar programa |
| `Ctrl+/` | Comentar/descomentar linha |
| `Ctrl+D` | Duplicar linha |
| `Ctrl+Y` | Deletar linha |
| `Ctrl+Alt+L` | Formatar código |
| `Alt+F12` | Abrir terminal |

---

## 7. Dicas Importantes

### Permissões de Execução

Se encontrar erro de permissão ao executar scripts:

```bash
chmod +x seu_script.py
```

### Atualizar pip

```bash
pip3 install --upgrade pip
```

### Verificar Pacotes Instalados

```bash
pip3 list
```

---

## 8. Solução de Problemas Comuns

### Erro: "python: command not found"

Use `python3` em vez de `python`:

```bash
python3 seu_script.py
```

### PyCharm não abre

```bash
# Via Snap
snap run pycharm-community

# Via Flatpak
flatpak run com.jetbrains.PyCharm-Community
```

### Conflito de versões Python

```bash
# Verificar todas as versões instaladas
ls /usr/bin/python*

# Usar versão específica
python3.10 --version
```

---

## 9. Recursos Adicionais

- **Documentação Python:** [https://docs.python.org/pt-br/3/](https://docs.python.org/pt-br/3/)
- **PyCharm Docs:** [https://www.jetbrains.com/help/pycharm/](https://www.jetbrains.com/help/pycharm/)
- **Python Package Index (PyPI):** [https://pypi.org/](https://pypi.org/)

---

## ✅ Pronto!

Agora você tem um ambiente Python completo no Linux! 🐧🐍

**Próximos passos:**
- Explore os tutoriais integrados do PyCharm
- Pratique com exercícios Python
- Comece a desenvolver seus projetos!
