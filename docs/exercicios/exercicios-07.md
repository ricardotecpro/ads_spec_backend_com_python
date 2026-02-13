# Exercícios - Aula 07

## 1. Dias da Semana
Crie uma TUPLA com os dias da semana ("Domingo", "Segunda", ...).
Peça ao usuário um número de 1 a 7 e imprima o dia correspondente.
(Lembre-se que o índice começa em 0, então 1 deve ser domingo).

## 2. Pódio Olímpico
Crie uma tupla com os 3 primeiros colocados de uma corrida: `podio = ("Ana", "Bia", "Carol")`.
Faça o desempacotamento dessas variáveis para `primeiro`, `segundo` e `terceiro`.
Imprima:
- Ouro: Ana
- Prata: Bia
- Bronze: Carol

## 3. Convidados Únicos
O usuário vai digitar nomes de convidados para uma festa.
Armazene em um SET para evitar nomes repetidos.
O programa para de pedir quando digitar "fim".
No final, mostre quantos convidados únicos (tamanho do set) e a lista de nomes.

## 4. Compras em Comum
Temos duas listas de compras:
`lista1 = {"Arroz", "Feijão", "Carne", "Macarrão"}`
`lista2 = {"Carne", "Cerveja", "Carvão", "Arroz"}`
Use operações de conjunto para descobrir:
1. Itens que estão nas duas listas (Interseção).
2. Itens que estão apenas na lista 1 (Diferença).
3. A lista de compras completa sem repetições (União).

## 5. Análise de Texto
Peça uma frase ao usuário.
Converta a frase em um set de caracteres para descobrir quantas letras **diferentes** foram usadas.
Exemplo: "banana" -> {'b', 'a', 'n'} -> 3 letras únicas.
