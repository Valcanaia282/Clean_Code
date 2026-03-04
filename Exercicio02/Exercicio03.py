#Converta temperatura celsius para fahrenheit.
def t(x):
    return (x * 9/5) + 32

temp = t(25)
print("Temperatura em Fahrenheit: ", temp)
#-------------------------------------------#
def converter_celsius_para_fahrenheit(temperatura_celsius):
    return (temperatura_celsius * 9 / 5) + 32


temperatura_celsius = 25
temperatura_fahrenheit = converter_celsius_para_fahrenheit(temperatura_celsius)

print("Temperatura em Fahrenheit:", temperatura_fahrenheit)