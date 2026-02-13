---
layout: revealjs
---


<!-- _class: lead -->
# Aula 15
## APIs e JSON

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- O que é uma API?
- O que é JSON?
- Consumindo dados da Web (`requests`)
- Status Codes HTTP (200, 404, 500)

---

## 🌐 API (Interface de Programação)

É como programas conversam entre si.
Em vez de clicar num site, seu código manda uma mensagem:
*"Ei, me dá a cotação do Dólar!"*

E a API responde com dados.

---

## 📦 JSON (JavaScript Object Notation)

É a língua universal da Web.
Muito parecido com Dicionários Python!

```json
{
  "nome": "Mario",
  "vidas": 3,
  "poderes": ["pulo", "fogo"]
}
```

Python converte isso para `dict` facilmente.

---

## 📡 Fazendo Requisições

Usamos a biblioteca `requests` (tem que instalar: `pip install requests`).

```python
import requests

url = "https://api.exemplo.com/dados"
resposta = requests.get(url)

print(resposta.status_code) # 200 = Sucesso
print(resposta.json()) # O dicionário com os dados
```

---

## 🚦 Códigos HTTP

O servidor diz se deu certo ou errado.

- **200 OK:** Deu certo! 👍
- **404 Not Found:** Não achei. 🔍
- **500 Internal Server Error:** O servidor quebrou. 🔥

---

## 🔎 Exemplo Real: ViaCEP

`https://viacep.com.br/ws/01001000/json/`

Retorna:
```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP"
}
```

---

## 🏁 Resumo

1. **APIs** conectam o mundo.
2. **JSON** é o formato de dados.
3. **`requests.get()`** busca os dados.
4. **`.json()`** transforma em dicionário.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos conectar na Matrix.
