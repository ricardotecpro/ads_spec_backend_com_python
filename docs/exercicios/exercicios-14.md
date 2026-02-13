# Exercícios - Aula 14

## 1. Animais
Crie uma classe `Animal` com método `falar()` que imprime "Som genérico".
Crie classes `Cachorro` e `Gato` que herdam de Animal e sobrescrevem `falar()` para "Au au" e "Miau".
Crie uma lista com um cachorro e um gato, percorra a lista e faça-os falar.

## 2. Formas Geométricas (Polimorfismo)
Crie uma classe `Forma` com método `area()` que retorna 0.
Crie `Quadrado(Forma)` com atributo `lado` e `area` que retorna `lado * lado`.
Crie `Circulo(Forma)` com atributo `raio` e `area` que retorna `3.14 * raio * raio`.
Teste calculando a área de ambos.

## 3. Funcionários (Herança + Super)
Classe `Funcionario` tem `nome` e `salario`.
Classe `Gerente` herda de Funcionario e tem atributo extra `senha`.
Use `super().__init__` para inicializar o Gerente.
Sobrescreva um método `calcular_bonus()`:
- Funcionario ganha 10% do salário.
- Gerente ganha 20% do salário.

## 4. Conta Privada
Crie uma classe `Cofre` com atributo privado `__segredo` (string).
Tente acessar `cofre.__segredo` diretamente e veja o erro.
Crie um método público `abrir_cofre(senha)` que, se a senha for "1234", retorna o segredo.

## 5. Veículos
Classe `Veiculo` (marca, modelo).
`Carro` herda de Veiculo e tem `portas`.
`Moto` herda de Veiculo e tem `cilindradas`.
Crie um método `detalhes()` em cada uma que aproveita o `detalhes()` do pai (com `super`) e adiciona a informação extra.
