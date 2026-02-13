---
layout: revealjs
---


<!-- _class: lead -->
# Aula 16
## Testes e TDD

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Qualidade de Software
- Pirâmide de Testes
- TDD (Test Driven Development)
- Pytest

---

## 🐞 Por que testar?

- **Confiança:** Posso mudar o código sem medo.
- **Documentação:** O teste mostra como usar o código.
- **Economia:** Achar bug na produção custa caro (R$). Achar no desenvolvimento é barato.

---

## 🔄 O Ciclo TDD

Não é só testar. É **desenhar** o software.

1. 🔴 **Red (Falha):** Escreva o teste para uma funcionalidade que não existe.
2. 🟢 **Green (Sucesso):** Faça o código mais simples para passar.
3. 🔵 **Refactor (Limpeza):** Melhore o código, remova duplicação.

---

## 🧪 O `pytest`

Ferramenta padrão da comunidade Python.

Instalação:
`pip install pytest`

Como escrever:
```python
def test_soma_simples():
    resultado = 2 + 2
    assert resultado == 4
```

Como rodar:
`pytest` (Ele acha sozinho os arquivos `test_*.py`)

---

## 🏗️ Estrutura AAA

1. **Arrange:** Prepara o cenário.
2. **Act:** Executa a ação.
3. **Assert:** Verifica o resultado.

```python
def test_login():
    # Arrange
    usuario = Usuario("admin", "123")
    
    # Act
    logado = usuario.login("123")
    
    # Assert
    assert logado == True
```

---

## 📁 Organização do Projeto

Separe código de produção dos testes.

- `src/`: Seu código Python.
- `tests/`: Seus arquivos de teste.

Isso é profissional e evita bagunça.

---

## 🏁 Resumo

1. Testes automatizados salvam vidas.
2. TDD ajuda a planejar o código.
3. Use `pytest`.
4. Mantenha testes simples e rápidos.

---

<!-- _class: lead -->
# Projeto Final 🚀
Gerenciador de Tarefas Profissional com TDD.
