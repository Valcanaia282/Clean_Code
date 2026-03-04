#Calcule o salário de um funcionário baseado na quantidade de horas trabalhadas (a) e na taxa de pagamento (b).
class x:
    def y(self, a, b):
        return a * b

z = x()
print(z.y(40, 160))
#-------------------------#
class CalculadoraSalario:
    def calcular_salario(self, horas_trabalhadas, taxa_pagamento):
        return horas_trabalhadas * taxa_pagamento


calculadora = CalculadoraSalario()
salario = calculadora.calcular_salario(40, 160)

print(salario)