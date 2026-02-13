---
layout: revealjs
---


<!-- _class: lead -->
# Aula 12
## Tratamento de Erros e Exceções

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Impedir que o programa quebre ("Crash").
- Blocos `try`, `except`, `else`, `finally`.
- Tipos comuns de erros.
- Lançar exceções (`raise`).

---

## 💥 O Problema

O mundo real é caótico. Usuários digitam errado, arquivos somem, a internet cai.

```python
x = int(input("Número: "))
# Se digitar "oi", o programa FECHA com erro vermelho.
```

Precisamos lidar com isso elegantemente.

---

## 🛡️ A Estrutura Básica

```python
try:
    # Tente fazer isso...
    x = int(input("Número: "))
    print(10 / x)

except ValueError:
    # Se der erro de valor (texto em vez de num)
    print("Digite apenas números!")

except ZeroDivisionError:
    # Se tentar dividir por zero
    print("Não pode dividir por 0!")

except Exception as e:
    # Qualquer outro erro
    print(f"Erro desconhecido: {e}")
```

---

## ☀️ Else e Finally

```python
try:
    arquivo = open("dados.txt", "r")
except FileNotFoundError:
    print("Erro ao abrir.")
else:
    # Só executa se o TRY deu certo
    print("Arquivo aberto com sucesso!")
    conteudo = arquivo.read()
finally:
    # Executa SEMPRE (dando erro ou não)
    print("Finalizando operação...")
```

---

## 🤚 Raise (Levantar erro)

Você pode criar suas próprias regras.

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente!")
    
    return saldo - valor

try:
    sacar(100, 500)
except ValueError as e:
    print(f"Falha no saque: {e}")
```

---

## 🏁 Resumo

1. Use `try/except` para código perigoso (I/O, Conversão).
2. Capture erros específicos (`ValueError` é melhor que `Exception`).
3. O programa não para se o erro for tratado.
4. `finally` é ótimo para fechar recursos.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos blindar nossos códigos.
