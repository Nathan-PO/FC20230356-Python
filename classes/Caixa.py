class Caixa:
    def __init__(self):
        self.valor_inicial = 0
        self.valor_final = 0
        self.vendas = []

    def abrir_caixa(self, valor_inicial):
        self.valor_inicial = valor_inicial
        self.valor_final = valor_inicial
        print(f"O caixa está iniciando com R$ {valor_inicial:.2f}.")

    def nova_venda(self, mercado):
        carrinho = []
        while True:
            codigo = input("Digite o código do produto (ou 'fim' para encerrar, 'remover' para remover item): ")
            if codigo == 'fim':
                break
            elif codigo == 'remover':
                codigo_remover = input("Digite o código do produto a ser removido do carrinho: ")
                carrinho = [item for item in carrinho if item[0].codigo != codigo_remover]
                print(f"Produto com código {codigo_remover} removido do carrinho.")
            else:
                produto = mercado.buscar_produto(codigo)
                if produto:
                    quantidade = int(input(f"Digite a quantidade de {produto.nome}: "))
                    if quantidade <= produto.quantidade:
                        carrinho.append((produto, quantidade))
                        produto.quantidade -= quantidade
                        print(f"{quantidade}x {produto.nome} adicionado ao carrinho.")
                    else:
                        print("Quantidade insuficiente em estoque.")
                else:
                    print("Produto não encontrado.")

        if carrinho:
            self.finalizar_venda(carrinho)

    def finalizar_venda(self, carrinho):
        total = 0
        print("Resumo da venda:")
        for item in carrinho:
            produto, quantidade = item
            subtotal = produto.valor * quantidade
            total += subtotal
            print(f"{produto.nome} {quantidade} un = Total R$ {subtotal:.2f}")
        self.valor_final += total
        self.vendas.append(total)
        print(f"Total da venda: R$ {total:.2f}")

    def fechar_caixa(self):
        total_vendas = sum(self.vendas)
        print(f"Valor inicial do caixa: R$ {self.valor_inicial:.2f}")
        print(f"Total de vendas: R$ {total_vendas:.2f}")
        print(f"Valor final do caixa: R$ {self.valor_final:.2f}")