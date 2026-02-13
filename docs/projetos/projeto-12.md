# Projeto 12 - Calculadora Robusta com Testes

## 🎯 Objetivo
Criar uma calculadora que realiza as 4 operações básicas, mas que é "imune" a erros de digitação e divisão por zero.

## 📋 Requisitos
Crie um módulo `calculadora.py`:
1. Funções: `somar(a, b)`, `subtrair(a, b)`, `multiplicar(a, b)`, `dividir(a, b)`.
2. A função `dividir` deve lançar (`raise`) um `ValueError` se o divisor for zero (ou deixar o Python lançar `ZeroDivisionError`, mas vamos tratar no menu).
3. Função `ler_numero(mensagem)`: Faz um loop infinito pedindo input até o usuário digitar um número válido (`float`). Trata `ValueError` internamente.

Crie um `main.py` (ou bloco main):
- Usa `ler_numero` para obter os valores.
- Chama as operações.
- Trata erros de divisão por zero.

## 🧪 Testes Automatizados
Crie `test_calculadora.py`.
Vamos testar o caminho feliz (sucesso) e o caminho triste (erro).

```python
import pytest # Se tiver pytest instalado, senão use unittest ou try/except manual
from calculadora import dividir

# Vamos usar try/except manual para não depender de bibliotecas externas por enquanto
def testar_divisao():
    # Teste Sucesso
    assert dividir(10, 2) == 5.0
    print("Divisão correta: PASSOU")
    
    # Teste Erro (Divisão por Zero)
    try:
        dividir(10, 0)
        print("Divisão por zero: FALHOU (Deveria ter dado erro)")
    except ZeroDivisionError: # ou ValueError, dependendo da sua implementação
        print("Divisão por zero: PASSOU (Erro capturado corretamente)")

if __name__ == "__main__":
    testar_divisao()
```

## 👣 Passo a Passo
1. Crie `calculadora.py` com as funções matemáticas.
2. Implemente `ler_numero` usando `try/except ValueError` dentro de um `while True`.
3. No menu, envolva a chamada da divisão em um `try/except` para exibir mensagem bonita em vez de erro vermelho.
4. Crie o script de teste e valide se o erro é lançado quando deve.

## 🚀 Desafio Extra
Adicione uma função de Log que salva em arquivo `erros.log` toda vez que uma exceção acontecer, com data e hora.
