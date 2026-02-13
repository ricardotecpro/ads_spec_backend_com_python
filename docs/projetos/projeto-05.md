# Projeto 05 - Jogo da Adivinhação

## 🎯 Objetivo
Um jogo clássico onde o computador "pensa" em um número e o usuário tenta adivinhar.

## 📋 Requisitos
1. O computador sorteia um número entre 1 e 100 (use `random.randint`).
2. O usuário chuta um número.
3. O programa diz se o chute foi **Maior** ou **Menor** que o número secreto.
4. O jogo continua (`while`) até o usuário acertar.
5. No final, mostre quantas tentativas foram necessárias.

## 💡 Dicas
Vai precisar importar `random`:
```python
import random
secreto = random.randint(1, 100)
```

## 👣 Passo a Passo
1. Gere o número secreto.
2. Crie uma variável `tentativas = 0`.
3. Crie um loop `while True`.
4. Dentro do loop:
    - Peça o chute.
    - Aumente `tentativas`.
    - Se chute == secreto: `break`.
    - Se chute > secreto: "Menos...".
    - Se chute < secreto: "Mais...".
5. Fora do loop, parabenize e mostre o total de tentativas.

## 🚀 Desafio Extra
Limite o número de tentativas! Se o usuário não acertar em 10 chances, ele perde (Game Over) e o loop para.
