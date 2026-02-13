# Projeto 13 - Sistema de Biblioteca

## 🎯 Objetivo
Criar um sistema básico para gerenciar livros usando Classes e Objetos.

## 📋 Requisitos

### Classe 1: `Livro`
- Atributos: `titulo`, `autor`, `disponivel` (booleano, começa True).
- Métodos:
    - `emprestar()`: Muda `disponivel` para False. Se já emprestado, avisa que não pode.
    - `devolver()`: Muda `disponivel` para True.

### Classe 2: `Biblioteca` (Opcional/Desafio)
- Atributos: `catalogo` (uma lista de objetos Livro).
- Métodos:
    - `adicionar_livro(livro)`: Recebe um objeto Livro e põe na lista.
    - `listar_livros()`: Mostra os títulos e se estão disponíveis.

## 💡 Dica
Você pode criar objetos dentro de objetos! A Biblioteca TEM livros.

## 👣 Passo a Passo
1. Crie a classe `Livro` e teste unitariamente (crie um livro, empreste, tente emprestar de novo, devolva).
2. (Se for fazer o desafio) Crie a `Biblioteca`, adicione livros e liste.
3. Faça um menu interativo simples.

## 🚀 Desafio Extra
Adicione um atributo `ano_publicacao` no Livro e crie um método na Biblioteca para `buscar_por_ano(ano)`.
