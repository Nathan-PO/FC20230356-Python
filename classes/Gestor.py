from Mercado import Mercado
from Caixa import Caixa
from Produto import Produto

class Gestor:
    def __init__(self, mercado):
        self.mercado = mercado

    def verificar_validade(self, dias):
        print(f"Produtos com validade menor que {dias} dias:")
        for produto in self.mercado.produtos:
            if produto.validade > 0 and produto.validade <= dias:
                print(produto)

    def controle_estoque(self):
        print("Controle de estoque:")
        self.mercado.listar_produtos()

def menu():
    mercado = Mercado()
    caixa = Caixa()
    gestor = Gestor(mercado)

    while True:
        print("\nMenu Principal")
        print("1. Abrir Caixa")
        print("2. Nova Venda")
        print("3. Fechar Caixa")
        print("4. Verificar Validade")
        print("5. Controle de Estoque")
        print("6. Cadastrar Novo Produto")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_inicial = float(input("Digite o valor inicial do caixa: "))
            caixa.abrir_caixa(valor_inicial)
        elif opcao == "2":
            caixa.nova_venda(mercado)
        elif opcao == "3":
            caixa.fechar_caixa()
        elif opcao == "4":
            dias = int(input("Digite a quantidade de dias para verificar a validade: "))
            gestor.verificar_validade(dias)
        elif opcao == "5":
            gestor.controle_estoque()
        elif opcao == "6":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            valor = float(input("Digite o valor por unidade: "))
            validade = int(input("Digite a validade (em dias, 0 se não aplicável): "))
            quantidade = int(input("Digite a quantidade: "))
            tipo = input("Digite o tipo (Alimento, Utensílio, Eletrodoméstico): ")
            novo_produto = Produto(codigo, nome, valor, validade, quantidade, tipo)
            mercado.cadastrar_produto(novo_produto)
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()