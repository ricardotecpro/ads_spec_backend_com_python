---
layout: revealjs
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
# Aula 03
## Operadores

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Operadores Aritméticos (Revisão e Aprofundamento)
- Operadores Relacionais (Comparação)
- Operadores Lógicos (`and`, `or`, `not`)
- Atribuição Simplificada (`+=`)

---

## 🧮 Aritméticos: Os Detalhes

Além do básico (`+`, `-`, `*`, `/`):

- **Divisão Inteira (`//`):** Corta a parte decimal.
  ```python
  7 // 2 # Resultado: 3 (e não 3.5)
  ```
- **Módulo (`%`):** O resto da divisão.
  ```python
  7 % 2 # Resultado: 1 (7 dividido por 2 dá 3 e sobra 1)
  ```
- **Potenciação (`**`):**
  ```python
  2 ** 3 # Resultado: 8 (2 ao cubo)
  ```

---

## ⚖️ Operadores Relacionais

Comparam dois valores e retornam `True` ou `False`.

| Op | Significado | Exemplo |
| :--: | :--- | :--- |
| `==` | Igual | `5 == 5` (True) |
| `!=` | Diferente | `5 != 3` (True) |
| `>` | Maior | `10 > 2` (True) |
| `<` | Menor | `1 < 5` (True) |
| `>=` | Maior/Igual | `5 >= 5` (True) |
| `<=` | Menor/Igual | `4 <= 3` (False) |

---

## 🧠 Operadores Lógicos

Para tomar decisões complexas.

1. **`and` (E):** Tudo tem que ser verdade.
   - `True and True` ➡ `True`
   - `True and False` ➡ `False`

2. **`or` (OU):** Basta um ser verdade.
   - `True or False` ➡ `True`
   - `False or False` ➡ `False`

3. **`not` (NÃO):** Inverte.
   - `not True` ➡ `False`

---

## ⚡ Atribuição Simplificada

Preguiça produtiva!

```python
x = 10

x += 5  # Igual a: x = x + 5 (x agora é 15)
x -= 2  # Igual a: x = x - 2 (x agora é 13)
x *= 2  # Igual a: x = x * 2 (x agora é 26)
```

---

## 👑 Precedência (Ordem)

Quem ganha a briga?

1. `()` Parênteses (O Chefe)
2. `**`
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `==`, `>`, etc
6. `not`
7. `and`
8. `or`

**Na dúvida, use parênteses!**

---

## 📝 Exemplo Prático

```python
idade = 25
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira

print(pode_dirigir) # True
```

---

## 🏁 Resumo

1. **Módulo (`%`)** é útil para par/ímpar.
2. **Relacionais** retornam Booleanos.
3. **Lógicos** combinam condições.
4. **Parênteses** controlam a ordem.

---

<!-- _class: lead -->
# Hora de Codar! 🚀
Bora para os exercícios.
