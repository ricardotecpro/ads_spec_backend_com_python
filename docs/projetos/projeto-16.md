# Projeto Final - Gerenciador de Tarefas (Task Manager) com TDD

## 🎯 Objetivo
Desenvolver o "núcleo" (backend) de um gerenciador de tarefas profissional usando TDD. Você não fará a interface (menu), apenas as classes e a lógica, garantidas por testes.

## 📋 Requisitos do Sistema

1. **Classe `Tarefa`:**
    - Atributos: `titulo`, `descricao`, `concluida` (bool, default False).
    - Método `concluir()`: Marca como True.
    - Método `pendente()`: Marca como False.

2. **Classe `GerenciadorTarefas`:**
    - Atributos: `tarefas` (lista).
    - Método `adicionar(titulo, descricao)`: Cria e adiciona tarefa. Retorna a tarefa criada.
    - Método `listar()`: Retorna lista de tarefas.
    - Método `listar_concluidas()`: Retorna apenas as True.
    - Método `remover(indice)`: Remove tarefa. Lança `IndexError` se inválido.

## 👣 Passo a Passo (Modo TDD)

Siga estritamente esta ordem. Não pule!

### Ciclo 1: Criar Tarefa
1. **Red:** Crie `test_tarefa.py`. Teste se ao instanciar `Tarefa("Estudar", "Python")`, os atributos estão certos e `concluida` é `False`.
2. **Green:** Crie a classe `Tarefa` em `tarefas.py`.
3. **Refactor:** Está limpo?

### Ciclo 2: Concluir Tarefa
1. **Red:** Adicione teste em `test_tarefa.py` chamando `.concluir()` e verificando se virou `True`.
2. **Green:** Implemente o método `concluir`.

### Ciclo 3: Gerenciador (Adicionar)
1. **Red:** Crie `test_gerenciador.py`. Teste `adicionar`. Verifique se a lista `tarefas` aumentou.
2. **Green:** Crie a classe `GerenciadorTarefas` e o método.

### Ciclo 4: Remover (Com erro)
1. **Red:** Teste `remover(0)` com lista vazia. Deve lançar exceção. (Use `pytest.raises`).
2. **Green:** Implemente a validação no `remover`.

## 🚀 Entrega
Seu projeto final deve ter:
- `src/tarefas.py` (O código)
- `tests/test_tarefa.py` (Testes da unidade Tarefa)
- `tests/test_gerenciador.py` (Testes da unidade Gerenciador)

Rode `pytest` e veja tudo verde. 🟢 Parabéns, você é um programador Python profissional!
