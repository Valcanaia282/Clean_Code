#Encontre o maior número em uma lista de números.
def d(q):
    m = q[0]
    for i in q:
        if i > m:
            m = i
    return m

mx = d([3, 7, 2, 9, 4])
print("Maior número: ", mx)
#------------------------------#
def encontrar_maior_numero(lista_numeros):
    maior_numero = lista_numeros[0]

    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero


lista = [3, 7, 2, 9, 4]
maior = encontrar_maior_numero(lista)

print("Maior número:", maior)