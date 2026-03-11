class FilmeService:

    def listar_filmes_disponiveis(self):
        print("Listando apenas filmes disponíveis para locação...")

    def listar_todos_filmes(self):
        print("Listando todos os filmes do catálogo...")

    def marcar_filme_disponivel(self, titulo):
        print(f'O filme "{titulo}" agora está disponível para locação.')

    def marcar_filme_indisponivel(self, titulo):
        print(f'O filme "{titulo}" foi marcado como indisponível.')


def main():
    service = FilmeService()

    service.listar_filmes_disponiveis()
    service.listar_todos_filmes()

    service.marcar_filme_disponivel("Inception")
    service.marcar_filme_indisponivel("Matrix")


if __name__ == "__main__":
    main()