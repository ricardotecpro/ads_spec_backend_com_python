# Projeto 04 - Pedra, Papel e Tesoura 👊✋✌️

## 🎯 Objetivo
Criar o clássico jogo "Jokenpô" (Pedra, Papel e Tesoura) para jogar contra o computador.

## 📋 Requisitos
1. O usuário escolhe sua jogada (Pedra, Papel ou Tesoura).
2. O computador escolhe aleatoriamente (vamos ensinar como fazer isso).
3. O programa compara as escolhas e declara o vencedor.

Regras:
- Pedra ganha de Tesoura
- Tesoura ganha de Papel
- Papel ganha de Pedra
- Iguais = Empate

## 💡 Como o computador escolhe?
Você vai precisar importar a biblioteca `random`.

```python
import random

opcoes = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(opcoes) # Escolhe um aleatório da lista
```

## 👣 Passo a Passo
1. Importe `random`.
2. Peça a jogada do usuário (`input`). Dica: Converta para letra minúscula ou tratada para facilitar.
3. Gere a jogada do computador.
4. Use `if/elif/else` para comparar:
    - Se forem iguais -> Empate.
    - Se usuário == Pedra e computador == Tesoura -> Usuário ganha.
    - (...) Liste todas as vitórias.
    - Se não for empate e usuário não ganhou -> Computador ganha.
5. Mostre as duas jogadas e o resultado final.

## 🚀 Desafio Extra
Faça o programa aceitar inputs como "p", "pedra", "PEDRA" da mesma forma (tratamento de string).
