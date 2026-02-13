# Projeto 11 - To-Do List Persistente

## 🎯 Objetivo
Melhorar nosso Gerenciador de Tarefas (da Aula 06) para que ele SALVE os dados em um arquivo. Assim, quando fecharmos e abrirmos o programa, as tarefas ainda estarão lá!

## 📋 Requisitos
1. Ao iniciar, o programa deve **carregar** as tarefas do arquivo `tarefas.txt` (se existir).
2. Ao adicionar uma tarefa, ela deve ser salva no arquivo.
3. Ao remover uma tarefa, o arquivo deve ser atualizado (reescrito).
4. O arquivo deve armazenar uma tarefa por linha.

## 💡 Lógica de Persistência
Temos duas estratégias principais:
- **Estratégia A (Simples):** Carrega tudo na memória (lista) ao iniciar. O usuário mexe na lista. Ao sair (ou a cada alteração), sobrescreve o arquivo inteiro com a lista atualizada.
- **Estratégia B (Incremental):** Adicionar usa `append` no arquivo. Remover exige reescrever.

*Vamos usar a Estratégia A para facilitar a remoção.*

## 👣 Passo a Passo
1. Crie uma função `carregar_tarefas()`: Tenta abrir o arquivo, lê as linhas, remove os `\n` e retorna uma lista. Se der erro (arquivo não existe), retorna lista vazia.
2. Crie uma função `salvar_tarefas(lista)`: Abre o arquivo em modo `'w'` e escreve cada item da lista seguido de `\n`.
3. No loop principal, use essas funções para manter a lista de memória e o arquivo sincronizados.

## 🧪 Testes Automatizados
Crie `test_todo.py`.
Vamos testar a persistência (Salvar e Carregar).

```python
import os
from todo import salvar_tarefas, carregar_tarefas

def testar_persistencia():
    arquivo_teste = "tarefas_teste.txt"
    lista_original = ["Comprar pão", "Estudar Python"]
    
    # 1. Salvar
    # (Adapte suas funções para aceitar o nome do arquivo como parâmetro opcional,
    # ou mude temporariamente a variável global do nome do arquivo)
    salvar_tarefas(lista_original, nome_arquivo=arquivo_teste)
    
    # 2. Verificar se arquivo existe
    assert os.path.exists(arquivo_teste)
    
    # 3. Carregar
    lista_recuperada = carregar_tarefas(nome_arquivo=arquivo_teste)
    
    # 4. Comparar
    assert lista_recuperada == lista_original
    
    # Limpeza (apagar arquivo de teste)
    os.remove(arquivo_teste)
    
    print("Teste de Persistência: PASSOU ✅")

if __name__ == "__main__":
    testar_persistencia()
```
*Obs: Para o teste funcionar, suas funções `salvar` e `carregar` precisam aceitar o nome do arquivo como argumento.*

## 🚀 Desafio Extra
Adicione suporte a status da tarefa (Concluída/Pendente) usando um formato específico no arquivo, ex: `[x] Estudar` ou `[ ] Dormir`.
