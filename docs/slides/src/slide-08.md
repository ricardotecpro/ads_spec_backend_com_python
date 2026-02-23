# Aula 08
## Dicionários

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Estrutura Chave-Valor (`key: value`)
- Acesso seguro com `.get()`
- Manipulação (Add, Edit, Remove)
- Loops em dicionários

---

## 📖 O que é um Dict?

Uma coleção onde cada item tem uma "etiqueta" (chave).
Análogo a um JSON ou uma linha de tabela.

```python
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
```

- Chaves (`keys`): "marca", "modelo", "ano"
- Valores (`values`): "Ford", "Mustang", 1964

---

## 🔑 Acessando Dados

Use a chave entre colchetes.

```python
print(carro["modelo"]) # Mustang
```

### O método `.get()`
Se a chave não existir, `[]` quebra o código. `get()` retorna `None` (seguro).

```python
print(carro.get("cor")) # None
print(carro.get("cor", "Preto")) # Valor padrão
```

---

## ✏️ Modificando

```python
# Alterar valor existente
carro["ano"] = 2020

# Criar nova chave
carro["cor"] = "Vermelho"

# Remover chave
del carro["modelo"]
# ou
cor = carro.pop("cor")
```

---

## 🔄 Loops e Dicts

Três formas principais:

```python
# 1. Pelas chaves (keys)
for k in carro.keys():
    print(k)

# 2. Pelos valores (values)
for v in carro.values():
    print(v)

# 3. Por ambos (items) - O MAIS USADO!
for k, v in carro.items():
    print(f"{k}: {v}")
```

---

## 🏗️ Lista de Dicionários

Estrutura muito poderosa para dados reais.

```python
clientes = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Beto"}
]

print(clientes[0]["nome"]) # Ana
```

---

## 🏁 Resumo

1. Dicionários mapeiam **chaves** para **valores**.
2. Sintaxe: `{chave: valor}`.
3. Chaves devem ser únicas.
4. Use `.items()` para iterar chave e valor juntos.
5. Base para APIs e manipulação de dados complexos.

---

# Prática! 🚀
Vamos para os exercícios.
