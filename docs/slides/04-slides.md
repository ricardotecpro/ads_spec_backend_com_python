---
layout: revealjs
---


<!-- _class: lead -->
# Aula 04
## Estruturas Condicionais (if/elif/else)

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Controlar o fluxo do programa
- `if` (Se)
- `else` (Senão)
- `elif` (Senão Se)
- Importância da **Indentação**

---

## 🤔 Tomando Decisões

Até agora nossos códigos eram lineares.
Mas precisamos fazer escolhas!

![width:600px](https://mermaid.ink/img/pako:eNpFj0ELgkAQhf_KMGcT9Ch0CiK6RB06eAizq6u4a-q6EaL_3l0TIzrN9968GcYKE0oCA3qVvF5hYgYlWx0N9FbaAdpaQ1aWcNk0vS707q5l_8i80WjO_44p-5scd1K8iR9iE73F3vWRLkY_xS66iXW0iU30T2wX2XT7f5I2R_oD6c4vVA)

---

## 🔹 A Estrutura `if`

Se a condição for `True`, executa o bloco.

```python
idade = 20

if idade >= 18:
    print("Pode entrar.")
    print("Bem-vindo!")
    
print("Fim")
```

👉 **INDENTAÇÃO:** Os espeços no início da linha (TAB ou 4 espaços) definem o que está "dentro" do `if`.

---

## 🔹 A Estrutura `else`

O caminho alternativo. Se o `if` falhar, o `else` assume.

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

---

## 🔹 A Estrutura `elif`

Para testar várias opções.

```python
cor = "vermelho"

if cor == "verde":
    print("Siga")
elif cor == "amarelo":
    print("Atenção")
elif cor == "vermelho":
    print("Pare")
else:
    print("Cor desconhecida")
```

---

## ⚠️ Erros Comuns

1. Esquecer os dois pontos (`:`) no final.
2. Errar a indentação (usar espaços e tabs misturados).
3. Usar `=` (atribuição) em vez de `==` (comparação).

```python
if x = 10: # ERRO!
    print("X é 10")
```

---

## 🧩 Combinando Lógica

Use `and`, `or`, `not` para condições complexas.

```python
# Entra se for sócio OU se pagar ingresso
if socio or pagou_ingresso:
    print("Entra")

# Entra se for maior de idade E tiver carteira
if idade >= 18 and tem_carteira:
    print("Dirige")
```

---

## 🏁 Resumo

1. **`if`**: Início da decisão.
2. **`elif`**: Outras opções (opcional).
3. **`else`**: Opção final/padrão (opcional).
4. **Indentação**: Obrigatória para definir os blocos.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos resolver problemas reais.
