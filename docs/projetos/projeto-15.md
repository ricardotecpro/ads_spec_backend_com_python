# Projeto 15 - Buscador de GitHub

## 🎯 Objetivo
Criar uma ferramenta que busca informações de um usuário do GitHub usando a API pública deles.

## 📋 Requisitos
1. Pergunte o nome do usuário do GitHub (ex: `torvalds`, `microsoft`).
2. Acesse a API: `https://api.github.com/users/{usuario}`.
3. Se o usuário existir (200 OK):
    - Mostre o Nome Completo.
    - Mostre a Bio.
    - Mostre o número de Seguidores.
    - Mostre o número de Repositórios Públicos.
4. Se não existir (404), diga "Usuário não encontrado".

## 💡 Dica
A API do GitHub é gratuita, mas tem limite de acessos por hora para anônimos. Se parar de funcionar, espere um pouco ou teste com outra API (como PokeAPI).

## 👣 Passo a Passo
1. Importe `requests`.
2. Pegue o input do usuário.
3. Monte a URL (f-string).
4. Faça o GET e verifique o `status_code`.
5. Se for 200, `dados = resposta.json()`.
6. Acesse as chaves `name`, `bio`, `followers`, `public_repos`.

## 🚀 Desafio Extra
Liste também os nomes dos 5 últimos repositórios do usuário.
(Dica: Explore a chave `repos_url` que vem no primeiro JSON, ou acesse `https://api.github.com/users/{usuario}/repos`).
