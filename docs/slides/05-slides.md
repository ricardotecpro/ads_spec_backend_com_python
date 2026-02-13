---
layout: revealjs
---


<!-- _class: lead -->
# Aula 05
## Estruturas de Repetição (Loops)

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Automatizar tarefas repetitivas
- Loop `for` (com `range`)
- Loop `while`
- Controles: `break` e `continue`

---

## 🔄 Por que usar Loops?

D.R.Y. (Don't Repeat Yourself) - Não se repita!

**Sem Loop:**
```python
print(1)
print(2)
print(3)
...
```

**Com Loop:**
```python
for i in range(1, 101):
    print(i)
```

---

## 🔢 O Loop `for`

Para quando sabemos o limite.

```python
for item in sequencia:
    # faça algo
```

### A função `range()`
Gera números.
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (passo)

---

## ⏳ O Loop `while`

Para quando não sabemos quando vai parar (depende de condição).

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1 # Importante incrementar!
```

> **Cuidado:** Se esquecer de atualizar a variável de controle, cria um **Loop Infinito** (trava o programa).

---

## 🛑 Break e Continue

Comandos de controle.

**`break`**: "Sair agora!"
```python
while True:
    msg = input("Digite 'sair': ")
    if msg == "sair":
        break
```

**`continue`**: "Pula essa, vai pra próxima!"
```python
for i in range(10):
    if i % 2 == 0:
        continue # Ignora números pares
    print(i) # Só imprime ímpares
```

---

## 🥊 for vs while

Use `for` para coleções e contagens fixas.
- "Para cada aluno na turma..."
- "Repita 10 vezes..."

Use `while` para eventos incertos.
- "Enquanto o jogador não morrer..."
- "Enquanto não digitar a senha correta..."

---

## 🏁 Resumo

1. Loops economizam código.
2. `range(start, stop)` gera sequências numéricas.
3. `for` itera sobre sequências.
4. `while` repete enquanto for Verdade.
5. `break` e `continue` dão superpoderes aos loops.

---

<!-- _class: lead -->
# Let's Loop! 🚀
Prática com repetições.
