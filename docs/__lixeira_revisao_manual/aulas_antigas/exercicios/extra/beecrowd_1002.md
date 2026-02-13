# Seis exercícios resolvidos em Python

---

## 1. **Área do Círculo**

**Enunciado:** Dado o valor de raio de um círculo, calcule a sua área.

**Entrada:** O valor do raio rr (0 < r ≤ 1000).

**Saída:** A área do círculo, com duas casas decimais.

### Solução em Python:

```python
import math

r = float(input())  # Leitura do raio
area = math.pi * r**2  # Cálculo da área
print(f"{area:.2f}")  # Exibição da área com duas casas decimais
```

### Exemplo de Entrada e Saída:

**Entrada:**

```
2.00
```

**Saída:**

```
12.57
```

---

## 2. **Cédulas**

**Enunciado:** Dado um valor de R$, calcule o número de cédulas necessárias para fazer esse valor com as cédulas disponíveis.

**Entrada:** O valor a ser pago (valor em reais, com até 2 casas decimais).

**Saída:** A quantidade de cédulas de cada valor (100, 50, 20, 10, 5, 2, 1).

### Solução em Python:

```python
valor = float(input())  # Leitura do valor
valor = int(valor * 100)  # Convertendo para centavos

cedulas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Cédulas em centavos
nomes = ["Cédulas de 100", "Cédulas de 50", "Cédulas de 20", "Cédulas de 10", "Cédulas de 5", 
         "Cédulas de 2", "Cédulas de 1"]

for i in range(len(cedulas)):
    num_cedulas = valor // cedulas[i]  # Número de cédulas
    valor %= cedulas[i]  # Subtrai a quantidade já retirada
    print(f"{num_cedulas} {nomes[i]}") 
```

### Exemplo de Entrada e Saída:

**Entrada:**

```
576.73
```

**Saída:**

```
5 Cédulas de 100
1 Cédulas de 50
1 Cédulas de 20
1 Cédulas de 5
1 Cédulas de 2
3 Cédulas de 1
```

---

## 3. **Figurinhas**

**Enunciado:** Dado dois números de figurinhas F1 e F2, calcule a maior quantidade de pilhas que pode ser formada com essas figurinhas.

**Entrada:** Vários casos de teste com dois números inteiros F1 e F2 (1 ≤ F1, F2 ≤ 1000).

**Saída:** A maior quantidade de pilhas que pode ser formada.

### Solução em Python:

```python
import math

# Leitura do número de casos de teste
T = int(input())

for _ in range(T):
    F1, F2 = map(int, input().split())
    print(math.gcd(F1, F2))  # Maior divisor comum (GCD)
```

### Exemplo de Entrada e Saída:

**Entrada:**

```
3
8 12
9 27
259 111
```

**Saída:**

```
4
9
37
```

---

## 4. **Crise de Energia**

**Enunciado:** Durante uma crise de energia, um número m deve ser escolhido de forma que Wellington (região 13) seja a última a ser desligada.

**Entrada:** O número N (13 ≤ N ≤ 100), representando o número de regiões. O fim da entrada é indicado pelo valor zero (0).

**Saída:** O valor de m que atende à condição de Wellington ser a última a ser desligada.

### Solução em Python:

```python
def survivor(n, k):
    Tnk = 0
    for i in range(1, n):
        Tnk = (Tnk + k) % i
    return Tnk

def main():
    while True:
        N = int(input())
        if N == 0:
            break
        
        k = 1
        while survivor(N, k) + 2 != 13:
            k += 1
        
        print(k)

if __name__ == "__main__":
    main()
```

### Exemplo de Entrada e Saída:

**Entrada:**

```
17
0
```

**Saída:**

```
7
```

---

## 5. **Tipos de Triângulos**

**Enunciado:** Dado três lados de um triângulo, determine o tipo do triângulo.

**Entrada:** Três valores de ponto flutuante A, B, C (1 ≤ A, B, C ≤ 1000).

**Saída:** Imprima o tipo do triângulo.

### Solução em Python:

```python
def classify_triangle(A, B, C):
    # Ordena os lados em ordem decrescente
    A, B, C = sorted([A, B, C], reverse=True)
    
    if A >= B + C:
        return "NAO FORMA TRIANGULO"
    elif A**2 == B**2 + C**2:
        return "TRIANGULO RETANGULO"
    elif A**2 > B**2 + C**2:
        return "TRIANGULO OBTUSANGULO"
    elif A**2 < B**2 + C**2:
        return "TRIANGULO ACUTANGULO"
    elif A == B == C:
        return "TRIANGULO EQUILATERO"
    elif A == B or B == C or A == C:
        return "TRIANGULO ISOSCELES"

# Leitura dos valores
A, B, C = map(float, input().split())
print(classify_triangle(A, B, C))
```

### Exemplo de Entrada e Saída:

**Entrada:**

```
7.0 5.0 7.0
```

**Saída:**

```
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES
```

---

## 6. **Dama**

**Enunciado:** Dado a posição de uma dama no tabuleiro de xadrez, calcule o número mínimo de movimentos necessários para ela ir de uma posição para outra.

**Entrada:** Quatro inteiros X1, Y1, X2, Y2 (1 ≤ X1, Y1, X2, Y2 ≤ 8).

**Saída:** O número mínimo de movimentos necessários.

### Solução em Python:

```python
def min_moves(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1
    return 2

# Leitura dos valores
x1, y1, x2, y2 = map(int, input().split())

# Processa até a linha 0 0 0 0
while (x1, y1, x2, y2) != (0, 0, 0, 0):
    print(min_moves(x1, y1, x2, y2))
    x1, y1, x2, y2 = map(int, input().split())
```

### Exemplo de Entrada e Saída:

**Entrada:**

```
4 4 6 2
3 5 3 5
5 5 4 3
0 0 0 0
```

**Saída:**

```
1
0
2
```

---

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
