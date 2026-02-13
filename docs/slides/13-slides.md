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
# Aula 13
## Orientação a Objetos (Intro)

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Paradigma OO.
- Classes vs Objetos.
- Atributos (`self.variavel`).
- Métodos (`def funcao()`).
- O Construtor `__init__`.

---

## 🏗️ Classe vs Objeto

Imagine uma fábrica de carros.

- **Classe (Molde):** O desenho técnico do carro. Definições de motor, cor, rodas. Não dá para dirigir o desenho.
- **Objeto (Instância):** O carro real que saiu da fábrica. Dá para dirigir, abastecer e bater.

```python
class Carro: # Molde
    pass

meu_fusca = Carro() # Objeto
```

---

## 💾 Atributos (Dados)

São as variáveis que "vivem" dentro do objeto.
Usamos `self` para dizer "meu atributo".

```python
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

c1 = Carro("Azul", "Fusca")
print(c1.cor) # Azul
```

### `__init__`
Roda AUTOMATICAMENTE quando criamos o objeto. Serve para inicializar.

---

## ⚙️ Métodos (Ações)

São funções que o objeto sabe executar.
O primeiro parâmetro TEM QUE SER `self`.

```python
class Carro:
    # ... init ...

    def acelerar(self):
        print(f"O {self.modelo} está acelerando! Vrum!")

c1.acelerar()
```

---

## 🤳 O tal do `self`

Por que preciso declarar `self`?
O Python passa o objeto automaticamente como primeiro argumento.

Quando chamamos:
`c1.acelerar()`

O Python faz internamente:
`Carro.acelerar(c1)`

Isso é o `self`: o próprio objeto `c1`.

---

## 🏁 Resumo

1. **POO** modela o mundo real.
2. **Classes** definem a estrutura.
3. **Objetos** são criados a partir de classes.
4. **Atributos** guardam estado.
5. **Métodos** definem comportamento.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos criar nossos próprios objetos.
