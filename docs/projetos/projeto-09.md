# Projeto 09 - Conversor de Temperaturas (Com Testes)

## 🎯 Objetivo
Criar funções para conversão de temperaturas (Celsius, Fahrenheit, Kelvin) e introduzir o conceito de **testes automatizados simples**.

## 📋 Requisitos

### Parte 1: As Funções
Crie um arquivo `conversor.py` com as seguintes funções. Todas devem **retornar** o valor (float), não imprimir.
1. `celsius_para_fahrenheit(c)`
    - Fórmula: $(C \times 9/5) + 32$
2. `fahrenheit_para_celsius(f)`
    - Fórmula: $(F - 32) \times 5/9$
3. `celsius_para_kelvin(c)`
    - Fórmula: $C + 273.15$
4. `kelvin_para_celsius(k)`
    - Fórmula: $K - 273.15$

### Parte 2: O Programa Principal (Manual)
No final do arquivo, crie um **menu** para o usuário escolher a conversão, digitar o valor e ver o resultado.

### Parte 3: Testes Automatizados (A Novidade!)
Vamos criar um pequeno script de teste para garantir que nossas funções estão corretas sem precisar rodar o menu toda hora.

Crie um arquivo `test_conversor.py`:

```python
from conversor import celsius_para_fahrenheit, celsius_para_kelvin

def teste_automatico():
    # Teste 1: 0°C deve ser 32°F
    assert celsius_para_fahrenheit(0) == 32
    print("Teste 1 (0C -> 32F): PASSOU")

    # Teste 2: 100°C deve ser 212°F
    assert celsius_para_fahrenheit(100) == 212
    print("Teste 2 (100C -> 212F): PASSOU")

    # Teste 3: 0°C deve ser 273.15K
    assert celsius_para_kelvin(0) == 273.15
    print("Teste 3 (0C -> 273.15K): PASSOU")

if __name__ == "__main__":
    try:
        teste_automatico()
        print("\nTodos os testes passaram! 🚀")
    except AssertionError:
        print("\nALERTA: Algum teste falhou! ❌")
```

## 👣 Passo a Passo
1. Defina as funções matemáticas (use Return!).
2. Implemente o menu dentro de um `if __name__ == "__main__":` no `conversor.py` (para que o menu não rode quando importarmos o arquivo no teste).
3. Crie o arquivo de teste e execute-o. Se nada explodir e aparecer "PASSOU", seu código está correto!

## 🚀 Por que isso é importante?
Imagine que você mudou a fórmula sem querer. O teste automático vai te avisar imediatamente (o `assert` vai falhar). Isso é **Garantia de Qualidade**!
