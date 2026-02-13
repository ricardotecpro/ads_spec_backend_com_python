# Projeto 03 - Calculadora de Gorjeta

## 🎯 Objetivo
Criar um programa que ajude a dividir a conta de um restaurante, calculando a gorjeta e o valor por pessoa.

## 📋 Requisitos
1. Solicitar o valor total da conta.
2. Solicitar a porcentagem da gorjeta que o usuário quer dar (ex: 10, 12, 15).
3. Solicitar quantas pessoas vão dividir a conta.
4. Calcular:
    - Valor da gorjeta.
    - Valor total (conta + gorjeta).
    - Valor para cada pessoa.
5. Exibir os resultados formatados (com 2 casas decimais).

## 💡 Saída Esperada
```text
Bem-vindo à Calculadora de Gorjeta!
-----------------------------------
Valor total da conta: R$ 150.00
Porcentagem da gorjeta: 10
Quantas pessoas: 3

Gorjeta: R$ 15.00
Total com gorjeta: R$ 165.00
Cada um paga: R$ 55.00
```

## 👣 Passo a Passo
1. `input()` para ler valor, porcentagem e pessoas.
2. Converter inputs (`float` para dinheiro, `int` para pessoas).
3. Cálculos:
    - `valor_gorjeta = total * (porcentagem / 100)`
    - `total_final = total + valor_gorjeta`
    - `por_pessoa = total_final / pessoas`
4. `print()` com f-strings e formatação `:.2f`.

## 🚀 Desafio Extra
Garanta que, mesmo que a conta dê um número quebrado na divisão (ex: 33.33333), o valor exibido seja amigável (arredondado).
