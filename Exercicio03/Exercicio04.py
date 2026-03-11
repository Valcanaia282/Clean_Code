class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def aplicar_desconto(self, desconto):
        novo_preco = self._preco - desconto
        return Produto(self._nome, novo_preco)


class CarrinhoDeCompras:
    def __init__(self, produto):
        self.produto = produto

    def adicionar_produto_ao_carrinho(self, novo_produto):
        self.produto = novo_produto

    def finalizar_compra(self):
        self.produto = self.produto.aplicar_desconto(10.0)

    def mostrar_detalhes(self):
        print("Produto:", self.produto.nome)
        print("Preço:", self.produto.preco)


def main():
    produto1 = Produto("Laptop", 1500.00)
    carrinho = CarrinhoDeCompras(produto1)

    produto2 = Produto("Smartphone", 1200.00)
    carrinho.adicionar_produto_ao_carrinho(produto2)

    carrinho.finalizar_compra()
    carrinho.mostrar_detalhes()


if __name__ == "__main__":
    main()