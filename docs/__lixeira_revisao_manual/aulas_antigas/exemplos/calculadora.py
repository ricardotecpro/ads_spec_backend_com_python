class Calculadora:
    def multiplicar(self, a, b):
        return a * b

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b


# Programa principal
if __name__ == "__main__":
    calc = Calculadora()

    resultado_multiplicacao = calc.multiplicar(5, 3)
    resultado_soma = calc.somar(15, 13)
    resultado_subtrair = calc.subtrair(20, 8)

    print("Resultado da multiplicação:", resultado_multiplicacao)
    print("Resultado da soma:", resultado_soma)
    print("Resultado da subtração:", resultado_subtrair)
