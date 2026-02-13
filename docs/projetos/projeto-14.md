# Projeto 14 - Sistema de RPG Simples

## 🎯 Objetivo
Criar um sistema de batalha de RPG usando classes, herança e polimorfismo.

## 📋 Requisitos
1. Classe Base `Personagem`:
    - Atributos: `nome`, `vida`, `forca`.
    - Método `atacar(inimigo)`: Tira vida do inimigo baseado na força.
    - Método `esta_vivo()`: Retorna True se vida > 0.

2. Classes Filhas:
    - `Guerreiro`: Força alta, vida alta.
    - `Mago`: Força média, mas tem método `lancar_magia(inimigo)` (dano extra, gasta mana).
    - `Monstro`: Personagem genérico para bater.

## 👣 Passo a Passo
1. Crie a classe `Personagem`.
2. Crie `Guerreiro` herdando de `Personagem`. Personalize o `__init__`.
3. Crie `Mago` herdando de `Personagem`. Adicione atributo `mana`.
4. Simule uma batalha:
    - Instancie um Guerreiro e um Monstro.
    - Faça um loop onde eles se atacam até um morrer.
    - Exiba o log da batalha ("Guerreiro atacou Monstro: -10 HP").

## 🚀 Desafio Extra
Crie uma classe `Arqueiro` que tem chance de "Crítico" (dano dobrado) quando ataca. Use o módulo `random` para calcular essa chance.
