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
# Aula 14
## POO Avançada

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Herança ("É um...")
- Polimorfismo (Comportamentos diferentes)
- Encapsulamento (`__privado`)
- Sobrescrita de métodos

---

## 🧬 Herança (Inheritance)

Evita copiar código.
Se `Animal` tem `comer()`, `Cachorro` também tem.

```python
class Animal:
    def comer(self):
        print("Comendo...")

class Cachorro(Animal): # Cachorro herda de Animal
    def latir(self):
        print("Au!")
```

Cachorro faz DUAS coisas: come e late.

---

## 🎭 Polimorfismo

O mesmo método, várias formas.

```python
class Gato(Animal):
    def fazer_som(self):
        print("Miau")

class Pato(Animal):
    def fazer_som(self):
        print("Quack")
```

Se eu chamar `fazer_som()`, cada um reage do seu jeito.

---

## 🦸‍♂️ O poder do `super()`

Chama a classe pai. Essencial no `__init__`.

```python
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Gerente(Funcionario):
    def __init__(self, nome, senha):
        super().__init__(nome) # Pai cuida do nome
        self.senha = senha     # Eu cuido da senha
```

---

## 🔒 Encapsulamento

Protegendo seus atributos.

- Público: `self.nome` (Acesso livre)
- Protegido: `self._saldo` (Só subclasses deviam mexer - Convenção)
- Privado: `self.__senha` (O Python "esconde" o nome)

Para acessar privados, usamos métodos **Getters e Setters** (`get_senha`, `set_senha`).

---

## 🏁 Resumo

1. **Herança** cria hierarquias.
2. **Polimorfismo** traz flexibilidade.
3. **`super()`** reaproveita construtores.
4. **Encapsulamento** traz segurança.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos evoluir nossos objetos.
