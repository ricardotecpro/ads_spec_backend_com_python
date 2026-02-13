# Projeto 10 - Jogo da Forca Modularizado

## 🎯 Objetivo
Criar o clássico Jogo da Forca, separando a lógica em módulos para ficar profissional.

## 📋 Requisitos

### Estrutura de Arquivos

Teremos 3 arquivos (módulos):

1.  `palavras.py`: Contém uma lista de palavras para o jogo.
2.  `forca.py`: Contém a lógica do jogo (funções).
3.  `main.py`: Onde o jogo começa (Menu).

### Detalhes de cada arquivo

**1. `palavras.py`**
- Deve ter uma lista: `LISTA_PALAVRAS = ["python", "computador", "programacao", "web"]`.
- Uma função `sortear_palavra()` que retorna uma palavra aleatória dessa lista.

**2. `forca.py`**
- Função `jogar()`: Controla o loop do jogo.
- Função `ocultar_palavra(palavra, letras_acertadas)`: Retorna a string com `_` e letras descobertas (Ex: `P _ T _ O N`).

**3. `main.py`**
- Importa `forca`.
- Pergunta se o usuário quer jogar.
- Chama `forca.jogar()`.

## 🧪 Testes Automatizados

Crie um arquivo `test_forca.py`.
Vamos testar a função `ocultar_palavra` (que é a lógica pura).

```python
from forca import ocultar_palavra

def testar():
    # Cenário 1: Nenhuma letra acertada
    assert ocultar_palavra("CASA", []) == "_ _ _ _"
    
    # Cenário 2: Algumas letras
    assert ocultar_palavra("CASA", ["A"]) == "_ A _ A"
    
    # Cenário 3: Todas as letras
    assert ocultar_palavra("CASA", ["C", "A", "S"]) == "C A S A"

    print("Testes do Jogo da Forca: PASSOU ✅")

if __name__ == "__main__":
    testar()
```

## 👣 Passo a Passo
1. Crie `palavras.py` com a lista e o `random.choice`.
2. Crie `forca.py` e implemente a lógica de substituir letras não encontradas por `_`.
3. Implemente o loop principal (chute letras, verifica se ganhou/perdeu).
4. Crie `main.py` para unir tudo.
5. Rode os testes para garantir a lógica visual.

## 🚀 Desafio Extra
Adicione um desenho de bonequinho usando ASCII Art em um módulo separado `desenhos.py` e mostre o membro sendo enforcado a cada erro!
