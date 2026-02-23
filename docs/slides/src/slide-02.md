# Aula 02
## Variáveis e Tipos de Dados

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Entender Variáveis e Tipos (`int`, `float`, `str`, `bool`)
- Usar `input()` para interagir com o usuário
- Converter tipos (Casting)
- Fazer contas básicas (Operadores)

---

## 📦 O que são Variáveis?

Etiquetas para guardar dados na memória.

```python
nome = "Batman"
idade = 35
rico = True
```

**Regras de Ouro (PEP 8):**
- Use `snake_case` (tudo minúsculo, separado por `_`).
- Nomes descritivos (`salario` é melhor que `s`).
- Case Sensitive: `nome` ≠ `Nome`.

---

## 🔢 Tipos Primitivos

| Tipo | Descrição | Exemplos |
| :--- | :--- | :--- |
| **int** | Inteiros | `10`, `-5`, `0` |
| **float** | Reais (Ponto) | `1.99`, `-0.5`, `3.14` |
| **str** | Texto | `"Oi"`, `'Python'` |
| **bool** | Lógicos | `True`, `False` |

Use `type(dado)` para descobrir o tipo.

---

## ⌨️ Entrada de Dados: `input()`

Pausa o programa e espera o usuário digitar.

```python
nome = input("Qual seu nome? ")
print("Oi", nome)
```

**⚠️ PERIGO:** O `input` SEMPRE retorna `str` (texto)!

```python
idade = input("Idade: ") # Usuário digita 20
# idade + 1 -> ERRO! "20" + 1
```

---

## 🔄 Conversão (Casting)

Para fazer contas com o que o usuário digitou, converta!

- `int("10")` -> `10` (Vira número inteiro)
- `float("5.5")` -> `5.5` (Vira número real)
- `str(10)` -> `"10"` (Vira texto)

**Exemplo Correto:**
```python
idade = int(input("Idade: ")) # Converte na hora
print(idade + 1) # Agora funciona!
```

---

## 🧮 Operadores Básicos

| Símbolo | Operação | Resultado `10 ? 3` |
| :---: | :--- | :--- |
| `+` | Soma | `13` |
| `-` | Subtração | `7` |
| `*` | Multiplicação | `30` |
| `/` | Divisão | `3.333...` |
| `//` | Divisão Inteira | `3` (ignora decimal) |
| `%` | Resto (Módulo) | `1` (sobra) |
| `**` | Potência | `1000` ($10^3$) |

---

## 📝 f-strings (Formatação)

O jeito moderno de misturar texto e variáveis.
Coloque um `f` antes das aspas e variáveis entre `{}`.

```python
nome = "Ana"
idade = 22

print(f"A {nome} tem {idade} anos.")
# A Ana tem 22 anos.
```

---

## 🏁 Resumo

1. Variáveis guardam valores.
2. `input()` lê texto do usuário.
3. Converta com `int()` ou `float()` para calcular.
4. Use f-strings (`f"{var}"`) para exibir.

---

# Vamos Praticar! 🚀
Exercícios e Projeto
