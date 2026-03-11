class EstatisticasTime:
    def __init__(self, nome, gols, posse_bola, chutes, faltas, cartoes_amarelos, cartoes_vermelhos):
        self.nome = nome
        self.gols = gols
        self.posse_bola = posse_bola
        self.chutes = chutes
        self.faltas = faltas
        self.cartoes_amarelos = cartoes_amarelos
        self.cartoes_vermelhos = cartoes_vermelhos


class Partida:
    def __init__(self, time_casa, time_visitante):
        self.time_casa = time_casa
        self.time_visitante = time_visitante


class GerenciadorPartida:

    def registrar_partida(self, partida):
        casa = partida.time_casa
        visitante = partida.time_visitante

        print("Partida Registrada:")
        print(f"{casa.nome} {casa.gols} x {visitante.gols} {visitante.nome}")
        print(f"Posse de Bola: {casa.posse_bola}% - {visitante.posse_bola}%")
        print(f"Chutes: {casa.chutes} - {visitante.chutes}")
        print(f"Faltas: {casa.faltas} - {visitante.faltas}")
        print(f"Cartões Amarelos: {casa.cartoes_amarelos} - {visitante.cartoes_amarelos}")
        print(f"Cartões Vermelhos: {casa.cartoes_vermelhos} - {visitante.cartoes_vermelhos}")

    def gerar_relatorio(self, partida):
        casa = partida.time_casa
        visitante = partida.time_visitante

        if casa.gols > visitante.gols:
            vencedor = casa.nome
        elif visitante.gols > casa.gols:
            vencedor = visitante.nome
        else:
            vencedor = "Empate"

        print("=== Relatório da Partida ===")
        print("Vencedor:", vencedor)
        print(f"Posse de Bola: {casa.posse_bola}% - {visitante.posse_bola}%")
        print("Total de Chutes:", casa.chutes + visitante.chutes)
        print("Total de Faltas:", casa.faltas + visitante.faltas)
        print("Total de Cartões:",
              (casa.cartoes_amarelos + visitante.cartoes_amarelos) +
              (casa.cartoes_vermelhos + visitante.cartoes_vermelhos))


def main():
    time_casa = EstatisticasTime("Time A", 2, 55, 10, 15, 3, 1)
    time_visitante = EstatisticasTime("Time B", 1, 45, 8, 12, 2, 0)

    partida = Partida(time_casa, time_visitante)

    gerenciador = GerenciadorPartida()
    gerenciador.registrar_partida(partida)
    gerenciador.gerar_relatorio(partida)


if __name__ == "__main__":
    main()