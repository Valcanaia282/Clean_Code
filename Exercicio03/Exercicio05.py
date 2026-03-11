class Jogo:
    def __init__(self, vida_jogador, vida_inimigo):
        self.vida_jogador = vida_jogador
        self.vida_inimigo = vida_inimigo

    def _aplicar_dano(self, vida_atual, dano, nome_personagem):
        vida_atual -= dano

        if vida_atual <= 0:
            print(f"{nome_personagem} perdeu!")
            return 0
        else:
            print(f"Vida do {nome_personagem}: {vida_atual}")
            return vida_atual

    def atacar_jogador(self, dano):
        self.vida_jogador = self._aplicar_dano(self.vida_jogador, dano, "Jogador")

    def atacar_inimigo(self, dano):
        self.vida_inimigo = self._aplicar_dano(self.vida_inimigo, dano, "Inimigo")

    def get_vida_jogador(self):
        return self.vida_jogador

    def get_vida_inimigo(self):
        return self.vida_inimigo


def main():
    jogo = Jogo(100, 80)

    jogo.atacar_inimigo(20)
    jogo.atacar_jogador(30)


if __name__ == "__main__":
    main()