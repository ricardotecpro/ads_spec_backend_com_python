# Projeto 07 - Sorteador de Loteria

## 🎯 Objetivo
Criar um gerador de palpites para a Mega Sena.

## 📋 Requisitos
Uma aposta da Mega Sena consiste em 6 números únicos entre 1 e 60.
1. O programa deve perguntar quantos jogos o usuário quer gerar.
2. Para cada jogo, gere 6 números aleatórios.
3. Use um `set` para garantir que não haja números repetidos dentro do mesmo jogo (se o `random` sortear repetido, o set ignora, mas você precisa garantir que o jogo tenha 6 números no final).
4. Mostre os jogos ordenados (ordem crescente).

## 💡 Dicas
- Use `while len(jogo) < 6:` para continuar sorteando até ter 6 números únicos.
- `random.randint(1, 60)` gera os números.
- Para ordenar visualmente, converta o set para lista e use `.sort()`.

## 👣 Passo a Passo
1. Importe `random`.
2. Pergunte a quantidade de jogos.
3. Crie um loop `for` para a quantidade de jogos.
4. Dentro do loop, crie um set vazio `jogo = set()`.
5. Crie um loop `while` que roda enquanto `len(jogo) < 6`.
6. Adicione o número aleatório.
7. Converta para lista, ordene e imprima.

## 🚀 Desafio Extra
Não permitir jogos repetidos! (Se o gerador criar 6 números que já foram gerados em um jogo anterior, descarte e gere outro).
