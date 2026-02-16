# Exercícios - Aula 12

## 1. Divisão Segura
Peça dois números ao usuário e faça a divisão.
Trate os erros:
- `ValueError` (se não digitar números).
- `ZeroDivisionError` (se dividir por zero).
Mostre o resultado ou a mensagem de erro apropriada.

## 2. Lista Segura
Crie uma lista com 3 nomes: `lista = ["Ana", "Bia", "Carol"]`.
Peça ao usuário um índice (número inteiro).
Imprima o nome correspondente.
Trate os erros:
- `ValueError` (se não digitar inteiro).
- `IndexError` (se o índice não existir na lista).

## 3. Dicionário Seguro
Crie um dicionário com alguns produtos e preços.
Peça ao usuário o nome de um produto.
Tente imprimir o preço.
Se o produto não existir (`KeyError`), avise o usuário e mostre os produtos disponíveis.

## 4. Validador de Senha
Crie uma função `verificar_senha(senha)` que:
- Lance uma exceção `ValueError` se a senha tiver menos de 6 caracteres.
- Lance uma exceção `ValueError` se a senha for apenas números (`.isdigit()`).
Use `try/except` para testar sua função com senhas válidas e inválidas.

## 5. Arquivo Fantasma
Tente abrir um arquivo chamado `nao_existe.txt` para leitura.
Capture o erro `FileNotFoundError` e imprima "Arquivo não encontrado, criando um novo...".
No bloco `except`, crie o arquivo vazio.
