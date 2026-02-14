# Configuração do Ambiente (Linux)

Este guia mostra como instalar e configurar o Python e PyCharm no Linux para desenvolvimento.

---

## 1. Instalando Python no Linux

A maioria das distribuições Linux já vem com Python instalado. Vamos verificar e atualizar se necessário.

### Verificar Versão Instalada

```bash
python3 --version
```

Se aparecer `Python 3.10` ou superior, você já tem Python! Caso contrário, instale:

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Fedora/RHEL

```bash
sudo dnf install python3 python3-pip
```

### Arch Linux

```bash
sudo pacman -S python python-pip
```

### Verificar Instalação

```bash
python3 --version
pip3 --version
```

---

## 2. Instalando e Configurando PyCharm

PyCharm é uma IDE profissional para Python desenvolvida pela JetBrains.

### Opção 1: Via Snap (Recomendado)

```bash
# Instalar PyCharm Community (Gratuito)
sudo snap install pycharm-community --classic

# OU PyCharm Professional (Pago, mas com trial)
sudo snap install pycharm-professional --classic
```

### Opção 2: Via Flatpak

```bash
# Adicionar repositório Flathub
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Instalar PyCharm Community
flatpak install flathub com.jetbrains.PyCharm-Community
```

### Opção 3: Download Manual

1. Acesse: [https://www.jetbrains.com/pycharm/download/#section=linux](https://www.jetbrains.com/pycharm/download/#section=linux)
2. Baixe a versão **Community** (gratuita) ou **Professional** (trial 30 dias)
3. Extraia o arquivo:

```bash
tar -xzf pycharm-community-*.tar.gz -C ~/
cd ~/pycharm-community-*/bin
./pycharm.sh
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
