#Converte temperatura celsius para fahrenheit e vice versa
def convert_temp(temp):
    return (temp * 9/5) + 32

def transform_temp(temp):
    return (temp - 32) * 5/9

intTemp = 25
intTemp2 = 77

print(convert_temp(intTemp))
print(transform_temp(intTemp2))
#------------------------------#
def converter_celsius_para_fahrenheit(temperatura_celsius):
    return (temperatura_celsius * 9 / 5) + 32


def converter_fahrenheit_para_celsius(temperatura_fahrenheit):
    return (temperatura_fahrenheit - 32) * 5 / 9


temperatura_celsius = 25
temperatura_fahrenheit = 77

print(converter_celsius_para_fahrenheit(temperatura_celsius))
print(converter_fahrenheit_para_celsius(temperatura_fahrenheit))