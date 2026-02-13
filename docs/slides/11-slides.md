---
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Roboto', sans-serif;
  }
  h1, h2, h3 {
    color: #3776ab;
  }
  code {
    background: #f0f0f0;
    border-radius: 5px;
    padding: 2px 5px;
  }
---

<!-- _class: lead -->
# Aula 11
## Manipulação de Arquivos

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## 🎯 Objetivos

- Persistência de dados (salvar para não perder).
- Função `open()`.
- Modos de leitura e escrita (`r`, `w`, `a`).
- O bloco `with` (Segurança).

---

## 📂 Abrindo Arquivos

```python
arquivo = open("exemplo.txt", "r")
# ... faz coisas ...
arquivo.close()
```

Problema: Se der erro no meio, o arquivo fica aberto (travado).

---

## 🛡️ O Bloco `with` (Context Manager)

A forma Pythonica e segura.

```python
with open("exemplo.txt", "w") as f:
    f.write("Olá!")
    
# Aqui o arquivo JÁ ESTÁ FECHADO automaticamente.
```

---

## 📝 Modos de Abertura

| Modo | Nome | Descrição |
| :---: | :--- | :--- |
| `'r'` | Read | Apenas leitura. Erro se não existir. |
| `'w'` | Write | Escrita. **Apaga** o conteúdo anterior! |
| `'a'` | Append | Adiciona no final. Mantém o anterior. |
| `'x'` | Create | Cria novo. Erro se já existir. |

---

## ✍️ Escrevendo

O `.write()` espera uma **string**.

```python
with open("nomes.txt", "w", encoding="utf-8") as f:
    f.write("Ana\n")
    f.write("Carlos\n")
```

> **Dica:** Use `encoding="utf-8"` para salvar acentos (ç, ã, é) corretamente.

---

## 📖 Lendo

```python
with open("nomes.txt", "r") as f:
    # Opção 1: Ler tudo de uma vez
    texto = f.read()

    # Opção 2: Ler linha a linha (Iterar)
    # f.seek(0) # Volta para o início se já leu
    for linha in f:
        print(linha.strip()) # strip remove o \n
```

---

## 🏁 Resumo

1. Arquivos permitem salvar dados.
2. Sempre use `with open(...)`.
3. Cuidado com o modo `'w'` (ele apaga tudo!).
4. Use `'a'` para Logs e listas crescentes.
5. `encoding="utf-8"` é seu amigo.

---

<!-- _class: lead -->
# Prática! 🚀
Vamos salvar nossos dados.
