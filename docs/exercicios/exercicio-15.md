# Exercícios - Aula 15

## 1. Instalando Requests
*(Exercício de configuração)*
Abra seu terminal e execute: `pip install requests` (ou verifique se já está instalado).
Crie um arquivo `.py` e faça `import requests` para ver se não dá erro.

## 2. Consumindo uma API Pública
Use a URL `https://jsonplaceholder.typicode.com/todos/1`.
Faça um GET e imprima o título (`title`) da tarefa que retornou.

## 3. Lista de Usuários
Use a URL `https://jsonplaceholder.typicode.com/users`.
Isso retorna uma LISTA de dicionários.
Faça um loop e imprima o `name` e o `email` de cada usuário.

## 4. Cotação de Moedas
A API `https://awesomeapi.com.br/last/USD-BRL` retorna a cotação do Dólar.
Faça um programa que acessa essa API e diz quanto está valendo 1 Dólar em Reais (`bid` ou `ask`).

## 5. Tratamento de Erro
Tente acessar uma URL que não existe (ex: `https://google.com/naoexiste`).
Use `try/except` para capturar o erro e imprimir "Página não encontrada" em vez de deixar o programa explodir.
