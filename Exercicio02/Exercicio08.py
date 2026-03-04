#Calcule se um estudante passou de ano de acordo com a média
def calcula(notas):
    return sum(grades) / len(grades)

def CalculaMais(notas):
    return value(grades) >= 60

Notas = [70, 80, 50]
MediaDasNotas = value(Notas)
print(CalculaMais(MediaDasNotas))
#--------------------------------#
def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    return media >= 60


notas_estudante = [70, 80, 50]

media = calcular_media(notas_estudante)
aprovado = verificar_aprovacao(media)

print(aprovado)