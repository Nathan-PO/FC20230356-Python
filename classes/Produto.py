class Produto:
    def __init__(self, codigo, nome, valor, validade, quantidade, tipo):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.validade = validade
        self.quantidade = quantidade
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} (Código: {self.codigo}) - {self.quantidade} unidades - R$ {self.valor:.2f} cada"