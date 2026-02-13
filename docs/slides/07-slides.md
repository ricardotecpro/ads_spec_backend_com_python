---
layout: revealjs
---


<!-- _class: lead -->
# Aula 07
## Tuplas e Sets

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Tuplas (Listas imutáveis)
- Desempacotamento
- Sets (Conjuntos únicos)
- União, Interseção e Diferença

---

## 🔒 Tuplas (Tuples)

Irmãs imutáveis das listas. Usam parênteses `()`.

```python
coordenadas = (10, 20)
dias = ("Seg", "Ter", "Qua")
```

**Por que usar?**
1. **Segurança:** Garante que dados não mudem.
2. **Performance:** Levemente mais rápidas.
3. **Sentido:** "Isto é um grupo fixo de dados".

---

## 🎁 Desempacotamento

Extrair valores de uma tupla para variáveis.

```python
ponto = (3, 4)

x, y = ponto
# x = 3
# y = 4
```

> Muito usado em funções que retornam múltiplos valores!

---

## 🦄 Sets (Conjuntos)

Coleções desordenadas de elementos **únicos**. Usam chaves `{}`.

```python
s = {1, 2, 3, 3, 3}
print(s) # {1, 2, 3} (Removeu duplicatas)
```

**Principais Usos:**
- Remover itens repetidos de uma lista.
- Testar pertinência (`if x in set`) de forma ultra rápida.

---

## 🧮 Matemática dos Conjuntos

Lembra da escola? Diagramas de Venn?

```python
A = {1, 2, 3}
B = {3, 4, 5}

# União (|) - Junta tudo
print(A | B) # {1, 2, 3, 4, 5}

# Interseção (&) - O que tem nos dois
print(A & B) # {3}

# Diferença (-) - O que tem só no A
print(A - B) # {1, 2}
```

---

## 🆚 Batalha das Estruturas

| Recurso | Lista | Tupla | Set |
| :--- | :---: | :---: | :---: |
| Sintaxe | `[]` | `()` | `{}` |
| Ordenada? | ✅ | ✅ | ❌ |
| Indexável? | ✅ | ✅ | ❌ |
| Imutável? | ❌ | ✅ | ❌ |
| Duplicatas? | ✅ | ✅ | ❌ |

---

## 🏁 Resumo

1. Use **Tuplas** para dados constantes.
2. Use **Sets** para garantir unicidade e operações matemáticas.
3. Converta listas em sets com `set(lista)` para limpar duplicatas.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos para os exercícios.
