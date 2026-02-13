# Projeto 06 - Gerenciador de Tarefas (To-Do List)

## 🎯 Objetivo
Criar um aplicativo de linha de comando para gerenciar uma lista de tarefas.

## 📋 Requisitos
O programa deve ter um menu com as opções:
1. **Adicionar Tarefa:** Pede o nome da tarefa e adiciona na lista.
2. **Listar Tarefas:** Mostra todas as tarefas numeradas (1. Estudar Python, 2. Ir na academia...).
3. **Concluir Tarefa:** Pede o número da tarefa e a remove da lista.
4. **Sair:** Encerra o programa.

## 💡 Dicas
- Use um loop `while True` para o menu.
- Para listar numerado, use `enumerate()` no `for`:
  ```python
  for i, tarefa in enumerate(tarefas):
      print(f"{i+1}. {tarefa}")
  ```
- Lembre-se que o usuário vê o número 1, mas o índice interno é 0. Você precisará subtrair 1 quando ele escolher qual remover.
- Trate o erro caso o usuário tente remover uma tarefa que não existe (índice inválido).

## 👣 Passo a Passo
1. Crie uma lista vazia `tarefas = []`.
2. Imprima o menu.
3. Leia a opção.
4. Implemente cada opção (`if/elif/else`).
5. No "Listar", verifique se a lista não está vazia.

## 🚀 Desafio Extra
Adicione uma funcionalidade de "Editar Tarefa", onde o usuário escolhe o número e digita o novo nome.
