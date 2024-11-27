from Produto import Produto

class Mercado:
    def __init__(self):
        self.produtos = []
        self.inicializar_produtos()

    def inicializar_produtos(self):
        # Adicionando 5 produtos de cada categoria
        alimentos = [
            Produto("001", "Arroz", 5.0, 30, 100, "Alimento"),
            Produto("002", "Feijão", 4.0, 30, 50, "Alimento"),
            Produto("003", "Macarrão", 3.0, 60, 80, "Alimento"),
            Produto("004", "Açúcar", 2.5, 180, 70, "Alimento"),
            Produto("005", "Sal", 1.0, 365, 90, "Alimento")
        ]
        utensilios = [
            Produto("101", "Prato", 10.0, 0, 30, "Utensílio"),
            Produto("102", "Copo", 5.0, 0, 50, "Utensílio"),
            Produto("103", "Garfo", 2.0, 0, 100, "Utensílio"),
            Produto("104", "Faca", 3.0, 0, 80, "Utensílio"),
            Produto("105", "Colher", 2.5, 0, 90, "Utensílio")
        ]
        eletrodomesticos = [
            Produto("201", "Liquidificador", 150.0, 0, 10, "Eletrodoméstico"),
            Produto("202", "Batedeira", 200.0, 0, 5, "Eletrodoméstico"),
            Produto("203", "Micro-ondas", 300.0, 0, 7, "Eletrodoméstico"),
            Produto("204", "Geladeira", 1200.0, 0, 3, "Eletrodoméstico"),
            Produto("205", "Fogão", 800.0, 0, 4, "Eletrodoméstico")
        ]
        self.produtos.extend(alimentos + utensilios + eletrodomesticos)

    def cadastrar_produto(self, produto):
        if self.verificar_codigo_unico(produto.codigo):
            self.produtos.append(produto)
            print(f"Produto {produto.nome} cadastrado com sucesso!")
        else:
            print("Erro: Código do produto já existe.")

    def verificar_codigo_unico(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return False
        return True

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def remover_produto(self, codigo):
        produto = self.buscar_produto(codigo)
        if produto:
            self.produtos.remove(produto)
            print(f"Produto {produto.nome} removido com sucesso!")
        else:
            print("Erro: Produto não encontrado.")

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)