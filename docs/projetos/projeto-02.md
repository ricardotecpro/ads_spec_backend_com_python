# Projeto 02 - Calculadora de IMC

## 🎯 Objetivo
Criar um programa que peça as informações físicas do usuário e calcule seu Índice de Massa Corporal (IMC).

## 📋 Requisitos

O programa deve solicitar:
1. O nome do usuário.
2. O peso (em kg). Permita números quebrados (ex: 70.5).
3. A altura (em metros). Permita números quebrados (ex: 1.75).

O cálculo do IMC é:
$$
IMC = \frac{Peso}{Altura^2}
$$

## 💡 Saída Esperada

O programa deve exibir uma mensagem amigável com o resultado arredondado (opcional: pesquise sobre `round()`).

Exemplo:
```text
Calculadora de IMC
------------------
Qual seu nome? Carlos
Qual seu peso (kg)? 80
Qual sua altura (m)? 1.80

Olá, Carlos!
Seu IMC é: 24.69
```

## 👣 Passo a Passo

1. Use `input()` para ler os dados.
2. Converta (`float()`) os dados de peso e altura imediatamente.
3. Aplique a fórmula matemática. Lembre-se que "ao quadrado" é `** 2`.
4. Use `print()` com f-strings para mostrar o resultado formatado.
5. (Extra) Tente formatar o número para mostrar apenas 2 casas decimais: `{imc:.2f}`.

## 🚀 Desafio Extra
Pesquise como usar a tabela de classificação do IMC e exiba (apenas visualmente no print, sem condicionais ainda) a tabela para o usuário comparar o resultado dele.
