# Exercícios - Aula 16

## 1. Instalando Pytest
Instale o pytest (`pip install pytest`) se ainda não tiver.
Crie um arquivo `test_exemplo.py` com um teste simples que passa (`assert 1 + 1 == 2`) e outro que falha (`assert 1 + 1 == 3`).
Rode `pytest` no terminal e veja a saída colorida.

## 2. Testando Funções Puras
Crie um arquivo `matematica.py` com funções `soma`, `subtracao`, `multiplicacao`.
Crie um arquivo `test_matematica.py` e escreva pelo menos um teste para cada função.

## 3. Testando Exceções
Crie uma função `divisao(a, b)` que lança `ValueError` se `b == 0`.
No teste, use `pytest.raises(ValueError)` (pesquise como usar) para garantir que o erro é lançado corretamente.

## 4. TDD: Palíndromo
Escreva PRIMEIRO o teste para uma função `eh_palindromo(texto)`.
- "ana" -> True
- "caio" -> False
- "Arara" -> True (deve ignorar maiúsculas)
Depois, implemente a função até os testes passarem.

## 5. TDD: Validador de Email Simples
Escreva testes para `validar_email(email)`:
- Deve ter "@"
- Deve ter "." depois do "@"
- Não pode ter espaços
Implemente a função para passar nos testes.
