class Pedido:
    def __init__(self, valor_total, tipo_cliente):
        self.valor_total = valor_total
        self.tipo_cliente = tipo_cliente  # "COMUM", "VIP" ou "FUNCIONARIO"

    def calcular_desconto(self):
        desconto = self.obter_percentual_desconto()
        return self.valor_total * (1 - desconto)

    def obter_percentual_desconto(self):
        if self.tipo_cliente == "COMUM":
            return 0.05
        if self.tipo_cliente == "VIP":
            return 0.10
        if self.tipo_cliente == "FUNCIONARIO":
            return 0.20
        return 0.0

    def exibir_resumo(self):
        print("Tipo de Cliente:", self.tipo_cliente)
        print("Valor Original: R$", self.valor_total)
        print("Valor com Desconto: R$", self.calcular_desconto())


def main():
    pedido1 = Pedido(100.0, "VIP")
    pedido1.exibir_resumo()


if __name__ == "__main__":
    main()