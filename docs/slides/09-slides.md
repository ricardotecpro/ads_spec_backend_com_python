---
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Roboto', sans-serif;
  }
  h1, h2, h3 {
    color: #3776ab;
  }
  code {
    background: #f0f0f0;
    border-radius: 5px;
    padding: 2px 5px;
  }
---

<!-- _class: lead -->
# Aula 09
## Funções (Parte 1)

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- O que são Funções?
- Criação (`def`)
- Parâmetros (Entrada)
- Retorno (`return`) (Saída)
- Documentação (`docstrings`)

---

## 🏭 O conceito de Função

Uma "mini-máquina" dentro do seu código.

**Entrada** ➡ **Processamento** ➡ **Saída**

*(Ingredientes)* ➡ *(Receita)* ➡ *(Bolo)*

**Por que usar?**
- Evitar repetição (DRY).
- Organizar o código.
- Facilitar testes e correções.

---

## 🔨 Criando (`def`) e Chamando

```python
# Definição (Cria a receita)
def dar_oi():
    print("Olá, pessoal!")

# Chamada (Faz o bolo)
dar_oi()
dar_oi()
```

---

## 📥 Parâmetros (Entrada)

Informações que a função precisa para trabalhar.

```python
def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")

saudacao_personalizada("Maria") # Olá, Maria!
saudacao_personalizada("João")  # Olá, João!
```

---

## 📤 Retorno (Saída)

`print` mostra na tela. `return` devolve o valor para o programa.

```python
def quadrado(numero):
    return numero * numero

resultado = quadrado(5) 
# resultado agorá vale 25
print(resultado + 1) # 26
```

> **Atenção:** `return` finaliza a função. Nada abaixo dele é executado.

---

## 📄 Docstrings

Documente seu código! Use aspas triplas.

```python
def somar(a, b):
    """
    Retorna a soma de dois números.
    """
    return a + b
```

Ajuda no `help(somar)` e no IntelliSense do VSCode.

---

## 🧪 Introdução a Testes (Spoiler!)

Como saber se sua função funciona?

**Teste Manual (Visual):**
```python
print(somar(2, 3)) # Espero ver 5
```

**Teste Automatizado (Assert):**
```python
assert somar(2, 3) == 5 # Se der errado, grita erro!
```
Veremos mais no projeto de hoje!

---

## 🏁 Resumo

1. **`def`**: Define.
2. **`()`**: Chama.
3. **Parâmetros**: Entradas variáveis.
4. **`return`**: Saída de dados (não confunda com print!).
5. **Docstrings**: Documentação.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos modularizar nossos códigos.
