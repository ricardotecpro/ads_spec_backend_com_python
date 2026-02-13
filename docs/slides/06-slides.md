---
layout: revealjs
---


<!-- _class: lead -->
# Aula 06
## Listas

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Criar e manipular Listas
- Indexação (`[0]`) e Fatiamento (`[:]`)
- Métodos: `append`, `insert`, `pop`, `remove`
- Funções: `len`, `max`, `min`

---

## 📝 O que é uma Lista?

Uma coleção ordenada de itens.
Pode guardar qualquer coisa (números, strings, booleanos, outras listas).

```python
vazia = []
frutas = ["Maçã", "Uva", "Banana"]
mista = [10, "Oi", True]
```

---

## 📍 Índices (Posição)

Começa sempre do **ZERO**!

```python
#          0        1        2
times = ["Fla", "Vasco", "Botafogo"]
```

- `times[0]` ➡ "Fla"
- `times[-1]` ➡ "Botafogo" (Último)

> **Erro Comum:** Tentar acessar um índice que não existe (`IndexError`).

---

## ✂️ Slicing (Fatiar)

Pegar pedaços da lista.
`[inicio : fim : passo]` (O fim não entra!)

```python
letras = ["A", "B", "C", "D", "E"]

print(letras[0:2]) # ['A', 'B']
print(letras[2:])  # ['C', 'D', 'E']
print(letras[::-1]) # Inverte a lista! ['E', 'D'...]
```

---

## ➕ Adicionar Itens

```python
lista = ["A"]

# No final (mais comum)
lista.append("B") 
# lista agora é ["A", "B"]

# Em posição específica
lista.insert(0, "C") 
# lista agora é ["C", "A", "B"]
```

---

## 🗑️ Remover Itens

```python
numeros = [10, 20, 30, 40]

# Pelo valor
numeros.remove(20) # [10, 30, 40]

# Pelo índice (e retorna o valor)
removido = numeros.pop(0) 
# removido = 10
# numeros = [30, 40]

# Último item
numeros.pop() # Remove 40
```

---

## 📏 Funções Úteis

```python
nums = [5, 1, 8, 3]

len(nums) # 4 (Tamanho)
sum(nums) # 17 (Soma)
max(nums) # 8 (Maior)
min(nums) # 1 (Menor)

sorted(nums) # [1, 3, 5, 8] (Ordena)
```

---

## 🏁 Resumo

1. Listas usam `[]`.
2. São mutáveis (podemos mudar itens).
3. Índices começam em 0.
4. `append` coloca no fim.
5. Slicing recorta a lista.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos para os exercícios.
