## Coleção de Problemas de Programação em Python

A seguir, apresentamos uma série de problemas de programação, comuns em plataformas de aprendizado e competição como URI (agora Beecrowd), juntamente com suas soluções em Python, explicações detalhadas e exemplos.

---

### Problema 1: Soma Simples (Atividade 1)

**Descrição:**
Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

* **Entrada:** A entrada contém 2 valores inteiros.
* **Saída:** Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade.

**Código Python:**
```python
# Leitura dos valores inteiros A e B
A = int(input())
B = int(input())

# Soma de A e B e atribuição à variável X
X = A + B

# Impressão do resultado no formato especificado
print(f"X = {X}")
```

**Explicação:**
1.  O programa lê dois números inteiros fornecidos pelo usuário e os armazena nas variáveis `A` e `B` utilizando a função `input()` convertida para `int()`.
2.  Calcula a soma de `A` e `B`, armazenando o resultado na variável `X`.
3.  Imprime o valor de `X` formatado conforme especificado: "X = " seguido do valor da soma. A f-string `f"X = {X}"` é usada para facilitar a formatação.

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    10
    9
    ```
  **Saída 1:**
    ```
    X = 19
    ```

* **Entrada 2:**
    ```
    -10
    4
    ```
  **Saída 2:**
    ```
    X = -6
    ```

* **Entrada 3:**
    ```
    15
    -7
    ```
  **Saída 3:**
    ```
    X = 8
    ```

---

### Problema 2: Média 1

**Descrição:**
Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

* **Entrada:** O arquivo de entrada contém 2 valores com uma casa decimal cada um.
* **Saída:** Imprima a mensagem "MEDIA = " e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade.

**Código Python:**
```python
# Leitura das notas A e B
A = float(input())
B = float(input())

# Cálculo da média ponderada
# Os pesos são 3.5 para A e 7.5 para B, somando 11
media = (A * 3.5 + B * 7.5) / 11

# Impressão da média com 5 casas decimais
print(f"MEDIA = {media:.5f}")
```

**Explicação:**
1.  O programa lê dois números de ponto flutuante, `A` e `B`, que representam as notas.
2.  A média ponderada é calculada usando a fórmula: $\text{MEDIA} = \frac{(A \times 3.5) + (B \times 7.5)}{3.5 + 7.5} = \frac{(A \times 3.5) + (B \times 7.5)}{11}$.
3.  O valor da média é impresso formatado com 5 casas decimais, utilizando a f-string `f"MEDIA = {media:.5f}"`.

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    5.0
    7.1
    ```
  **Saída 1:**
    ```
    MEDIA = 6.43182
    ```

* **Entrada 2:**
    ```
    0.0
    7.1
    ```
  **Saída 2:**
    ```
    MEDIA = 4.84091
    ```

---

### Problema 3: Salário

**Descrição:**
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

* **Entrada:** O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número do funcionário, quantidade de horas trabalhadas e o valor por hora, respectivamente.
* **Saída:** Imprima o número e o salário do funcionário, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o `$`.

**Código Python:**
```python
# Leitura dos dados de entrada
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Impressão do número do funcionário e o salário
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")
```

**Explicação:**
1.  O programa lê o número do funcionário (inteiro), o número de horas trabalhadas (inteiro) e o valor que ele recebe por hora (ponto flutuante).
2.  Calcula o salário multiplicando as `horas_trabalhadas` pelo `valor_por_hora`.
3.  Imprime o número do funcionário e o salário formatado com duas casas decimais, precedido de "U$ ".

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    25
    100
    5.50
    ```
  **Saída 1:**
    ```
    NUMBER = 25
    SALARY = U$ 550.00
    ```

---

### Problema 4: Salário com Bônus

**Descrição:**
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

* **Entrada:** O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo e o total de vendas.
* **Saída:** Imprima o total que o funcionário deverá receber.

**Código Python:**
```python
# Leitura dos dados de entrada
nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

# Cálculo da comissão (15% sobre as vendas)
comissao = total_vendas * 0.15

# Cálculo do total a receber
total_a_receber = salario_fixo + comissao

# Impressão do total a receber com 2 casas decimais
print(f"TOTAL = R$ {total_a_receber:.2f}")
```

**Explicação:**
1.  O programa lê o nome do vendedor (string), seu salário fixo (ponto flutuante) e o total de vendas no mês (ponto flutuante).
2.  Calcula a comissão como 15% (ou 0.15) do `total_vendas`.
3.  Soma o `salario_fixo` com a `comissao` para obter o `total_a_receber`.
4.  Imprime o `total_a_receber` formatado com duas casas decimais, precedido de "R$ ".

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    JOAO
    500.00
    1230.30
    ```
  **Saída 1:**
    ```
    TOTAL = R$ 684.54
    ```

---

### Problema 5: Esfera

**Descrição:**
Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: $(4/3) \times \pi \times R^3$. Considere (atribua) para pi o valor 3.14159.

* **Entrada:** O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.
* **Saída:** A saída deverá ser uma mensagem "VOLUME = " com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

**Código Python:**
```python
# Leitura do valor do raio
R = float(input())

# Valor de pi
pi = 3.14159

# Cálculo do volume da esfera
# Usar (4.0/3) ou (4/3.0) para garantir a divisão de ponto flutuante em algumas linguagens.
# Em Python 3, 4/3 já resulta em float.
volume = (4.0/3.0) * pi * (R ** 3)

# Impressão do volume com 3 casas decimais
print(f"VOLUME = {volume:.3f}")
```

**Explicação:**
1.  O programa lê o valor do raio `R` da esfera (ponto flutuante).
2.  Define o valor de `pi` como 3.14159.
3.  Calcula o volume da esfera usando a fórmula $V = \frac{4}{3} \pi R^3$. A expressão `R ** 3` calcula $R^3$.
4.  Imprime o `volume` formatado com três casas decimais.

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    3
    ```
  **Saída 1:**
    ```
    VOLUME = 113.097
    ```

---

### Problema 6: Área

**Descrição:**
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

* **Entrada:** O arquivo de entrada contém três valores com um dígito após o ponto decimal.
* **Saída:** O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor (ex: "TRIANGULO: valor"). O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

**Código Python:**
```python
# Leitura dos valores A, B e C em uma única linha, separados por espaço
A, B, C = map(float, input().split())

# Valor de pi
pi = 3.14159

# a) Área do triângulo retângulo (base A, altura C)
area_triangulo = (A * C) / 2.0

# b) Área do círculo (raio C)
area_circulo = pi * (C ** 2)

# c) Área do trapézio (bases A e B, altura C)
area_trapezio = ((A + B) * C) / 2.0

# d) Área do quadrado (lado B)
area_quadrado = B ** 2

# e) Área do retângulo (lados A e B)
area_retangulo = A * B

# Impressão das áreas com 3 casas decimais e formatação específica
print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")
```

**Explicação:**
1.  O programa lê três valores de ponto flutuante `A`, `B`, e `C` de uma única linha de entrada. A função `input().split()` divide a string de entrada por espaços, e `map(float, ...)` converte cada parte para `float`.
2.  Define o valor de `pi`.
3.  Calcula as seguintes áreas:
   * Triângulo retângulo: $\text{Área}_{\text{triângulo}} = \frac{\text{base} \times \text{altura}}{2} = \frac{A \times C}{2}$
   * Círculo: $\text{Área}_{\text{círculo}} = \pi \times \text{raio}^2 = \pi \times C^2$
   * Trapézio: $\text{Área}_{\text{trapézio}} = \frac{(\text{base}_1 + \text{base}_2) \times \text{altura}}{2} = \frac{(A + B) \times C}{2}$
   * Quadrado: $\text{Área}_{\text{quadrado}} = \text{lado}^2 = B^2$
   * Retângulo: $\text{Área}_{\text{retângulo}} = \text{lado}_1 \times \text{lado}_2 = A \times B$
4.  Imprime cada área calculada em uma nova linha, formatada com três casas decimais e com o rótulo seguido de dois pontos e um espaço (ex: "TRIANGULO: ").

**Exemplos de Entrada e Saída:**

* **Entrada:**
    ```
    3.0 4.0 5.2
    ```
  **Saída:**
    ```
    TRIANGULO: 7.800
    CIRCULO: 84.949
    TRAPEZIO: 18.200  
    QUADRADO: 16.000
    RETANGULO: 12.000
    ```
  *(Nota: O exemplo de saída para o TRAPEZIO no prompt original era 18.600. Com A=3.0, B=4.0, C=5.2, a área do trapézio é ((3.0+4.0)*5.2)/2 = (7.0*5.2)/2 = 36.4/2 = 18.200. Se a intenção era outra, os valores de A, B ou C seriam diferentes ou a fórmula aplicada no exemplo do prompt estava ligeiramente diferente.)*
  Para a entrada `3.0 4.0 5.2` e considerando as bases como A e B, e altura C:
  Área do Trapézio = $((A + B) \times C) / 2 = ((3.0 + 4.0) \times 5.2) / 2 = (7.0 \times 5.2) / 2 = 36.4 / 2 = 18.200$.

---

### Problema 7: O Maior

**Descrição:**
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

* **Entrada:** O arquivo de entrada contém três valores inteiros.
* **Saída:** Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

**Código Python:**
```python
# Leitura dos três valores inteiros em uma única linha
valores_str = input().split()
a = int(valores_str[0])
b = int(valores_str[1])
c = int(valores_str[2])

# Encontrar o maior valor entre os três usando a função max()
maior_valor = max(a, b, c)

# Imprimir o maior valor seguido da mensagem
print(f"{maior_valor} eh o maior")
```

**Explicação:**
1.  O programa lê uma linha de entrada que contém três números inteiros separados por espaços. `input().split()` cria uma lista de strings.
2.  Cada string da lista é convertida para inteiro e atribuída às variáveis `a`, `b`, e `c`.
3.  A função `max(a, b, c)` é utilizada para determinar o maior valor entre os três.
4.  O maior valor é impresso, seguido pela mensagem " eh o maior".

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    7 14 106
    ```
  **Saída 1:**
    ```
    106 eh o maior
    ```

---

### Problema 8: Idade em Dias

**Descrição:**
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias. Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.

* **Entrada:** O arquivo de entrada contém um valor inteiro.
* **Saída:** Imprima a saída conforme exemplo fornecido (X ano(s), Y mes(es), Z dia(s)).

**Código Python:**
```python
# Leitura do valor de idade em dias
total_dias = int(input())

# Cálculo dos anos
anos = total_dias // 365
dias_restantes_apos_anos = total_dias % 365

# Cálculo dos meses
meses = dias_restantes_apos_anos // 30
dias_finais = dias_restantes_apos_anos % 30

# Impressão do resultado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias_finais} dia(s)")
```

**Explicação:**
1.  O programa lê um valor inteiro que representa a idade de uma pessoa em `total_dias`.
2.  Calcula o número de `anos` completos usando a divisão inteira (`//`) por 365.
3.  O `dias_restantes_apos_anos` é obtido com o operador módulo (`%`) por 365.
4.  Calcula o número de `meses` completos a partir dos `dias_restantes_apos_anos` usando a divisão inteira por 30.
5.  Os `dias_finais` são o restante da divisão dos `dias_restantes_apos_anos` por 30.
6.  Imprime a idade decomposta em anos, meses e dias, cada um em uma nova linha com a formatação especificada.

**Exemplos de Entrada e Saída:**

* **Entrada 1:**
    ```
    400
    ```
  **Saída 1:**
    ```
    1 ano(s)
    1 mes(es)
    5 dia(s)
    ```

* **Entrada 2:**
    ```
    800
    ```
  **Saída 2:**
    ```
    2 ano(s)
    2 mes(es)
    10 dia(s)
    ```

---

### Considerações Finais e Boas Práticas:

* **Leitura de Entrada:** Utilize `input()` para ler strings. Converta para `int()` ou `float()` conforme necessário. Para múltiplas entradas na mesma linha, `input().split()` é útil, combinado com `map()` para conversão.
* **Precisão de Ponto Flutuante:** Ao lidar com `float`, esteja ciente de problemas de precisão. Para saída, formate o número de casas decimais usando f-strings (ex: `{variavel:.3f}`).
* **Fórmulas Matemáticas:** Implemente as fórmulas cuidadosamente. Use parênteses para garantir a ordem correta das operações.
* **Clareza do Código:** Use nomes de variáveis descritivos. Adicione comentários para explicar partes complexas ou a lógica geral.
* **Conformidade com a Saída:** Problemas de juízes online são muito estritos quanto ao formato da saída. Preste atenção a espaços, quebras de linha e mensagens exatas.
* **Funções:** Para problemas mais complexos, dividir o código em funções pode melhorar a organização e a legibilidade, mas para esses exemplos simples, um script linear é aceitável.

Esta organização visa apresentar os problemas e suas soluções de forma clara, didática e padronizada.


---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
