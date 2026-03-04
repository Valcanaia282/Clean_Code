#Encontre o maior número par em uma lista de números.
def find_smallest_odd_number(numbers):
    largest = None
    for num in numbers:
        if num % 2 == 0 and (largest is None or num > largest):
            largest = num
    return largest

print(find_smallest_odd_number([3, 10, 7, 8, 15]))
#-------------------------------------------------#
def encontrar_maior_numero_par(lista_numeros):
    maior_numero_par = None

    for numero in lista_numeros:
        if numero % 2 == 0 and (maior_numero_par is None or numero > maior_numero_par):
            maior_numero_par = numero

    return maior_numero_par


lista = [3, 10, 7, 8, 15]
maior_par = encontrar_maior_numero_par(lista)

print("Maior número par:", maior_par)