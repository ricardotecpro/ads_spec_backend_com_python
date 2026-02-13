---
layout: revealjs
---


<!-- _class: lead -->
# Aula 10
## Módulos e Pacotes

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Reutilizar código com `import`
- Biblioteca Padrão (`stdlib`)
- Criar Módulos próprios (`.py`)
- Pacotes (Pastas)

---

## 📦 O que é um Módulo?

Arquivos `.py` contendo:
- Funções
- Classes
- Variáveis

**Vantagem:** Divide problemas grandes em partes pequenas e organizadas.

---

## 🔌 Importando ("Baterias Inclusas")

O Python já vem com muita coisa pronta.

**Exemplo `math`:**
```python
import math

print(math.pi) # 3.14159...
print(math.sqrt(16)) # 4.0
```

**Exemplo `random`:**
```python
import random

print(random.randint(1, 10)) # Sorteia de 1 a 10
```

---

## 🎯 Import Específico (`from ... import`)

Pega só o que precisa (mais limpo).

```python
from math import sqrt, pi

print(pi) # Não precisa do math.pi
print(sqrt(9))
```

---

## 🏷️ Apelidos (`as`)

Para nomes longos ou convenções.

```python
import datetime as dt
import pandas as pd # Convenção mundial

inicio = dt.datetime.now()
```

---

## 🔨 Seus Próprios Módulos

Crie `minha_lib.py`:
```python
def ola():
    print("Oi do módulo!")
```

Use em `main.py`:
```python
import minha_lib

minha_lib.ola()
```

---

## 📂 Pacotes

São **pastas** com arquivos Python.
Geralmente têm um `__init__.py` dentro.

`from meu_pacote import meu_modulo`

Exemplo de estrutura:
- `jogo/` (Pacote)
  - `__init__.py`
  - `graficos.py` (Módulo)
  - `som.py` (Módulo)

---

## 🏁 Resumo

1. `import modulo`: Traz o arquivo.
2. `from modulo import item`: Traz a função/classe.
3. `as apelido`: Renomeia.
4. Módulos organizam e evitam arquivos gigantes.
5. Biblioteca Padrão é poderosa (`os`, `sys`, `math`, `random`...).

---

<!-- _class: lead -->
# Prática! 🚀
Vamos modularizar o mundo.
