
# Sistema de Gerenciamento de Mercado

Este é um sistema simples de gerenciamento de mercado desenvolvido em Python. O sistema permite o cadastro de produtos, gerenciamento de estoque, operações de caixa e funcionalidades de gestão.

## Funcionalidades

1. **Cadastro de Produtos**
   - Permite o cadastro de três tipos de produtos: Alimentos, Utensílios e Eletrodomésticos.
   - Verificação de segurança para garantir que novos produtos não sejam cadastrados com códigos já existentes.

2. **Busca e Remoção de Produtos**
   - Mecanismo de busca para localizar produtos cadastrados.
   - Permite a remoção de produtos através do código do produto.

3. **Operação do Caixa**
   - Abertura do Caixa: Inserir valor inicial e exibir mensagem.
   - Nova Venda: Adicionar produtos ao carrinho, mostrar subtotal, somar produtos iguais, fechar carrinho e finalizar compra.
   - Remoção de Itens do Carrinho: Permite remover itens do carrinho durante a venda.
   - Encerramento da Compra: Perguntar se deseja encerrar, exibir resumo da venda, retornar ao menu de vendas se necessário.

4. **Atualização de Estoque**
   - Debitar a quantidade de produtos do estoque ao finalizar uma venda.

5. **Fechamento de Caixa**
   - Somar todas as vendas finalizadas e exibir o valor inicial e final do caixa.

6. **Aba do Gestor**
   - Verificação de Validade: Permite verificar a validade dos produtos conforme a quantidade de dias desejada.
   - Controle de Estoque: Consultar a quantidade de unidades em estoque.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python instalado.
3. Execute o script `main.py` para iniciar o sistema.

```bash
python main.py
```

## Menu Principal

- **1. Abrir Caixa**: Inicia o caixa com um valor inicial.
- **2. Nova Venda**: Permite adicionar produtos ao carrinho e finalizar a venda.
- **3. Fechar Caixa**: Exibe o valor inicial, total de vendas e valor final do caixa.
- **4. Verificar Validade**: Verifica a validade dos produtos conforme a quantidade de dias informada.
- **5. Controle de Estoque**: Exibe a lista de produtos em estoque.
- **6. Cadastrar Novo Produto**: Permite cadastrar novos produtos no sistema.
- **7. Sair**: Encerra o sistema.

## Código

```python
class Produto:
    def __init__(self, codigo, nome, valor, validade, quantidade, tipo):
        """
        Inicializa um novo produto.

        :param codigo: Código do produto
        :param nome: Nome do produto
        :param valor: Valor por unidade
        :param validade: Validade em dias (0 se não aplicável)
        :param quantidade: Quantidade em estoque
        :param tipo: Tipo do produto (Alimento, Utensílio, Eletrodoméstico)
        """
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.validade = validade
        self.quantidade = quantidade
        self.tipo = tipo

    def __str__(self):
        """
        Retorna uma representação em string do produto.
        """
        return f"{self.nome} (Código: {self.codigo}) - {self.quantidade} unidades - R$ {self.valor:.2f} cada"

class Mercado:
    def __init__(self):
        """
        Inicializa o mercado com uma lista de produtos.
        """
        self.produtos = []
        self.inicializar_produtos()

    def inicializar_produtos(self):
        """
        Adiciona produtos iniciais ao mercado.
        """
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
        """
        Cadastra um novo produto no mercado.

        :param produto: Instância da classe Produto
        """
        if self.verificar_codigo_unico(produto.codigo):
            self.produtos.append(produto)
            print(f"Produto {produto.nome} cadastrado com sucesso!")
        else:
            print("Erro: Código do produto já existe.")

    def verificar_codigo_unico(self, codigo):
        """
        Verifica se o código do produto é único.

        :param codigo: Código do produto
        :return: True se o código for único, False caso contrário
        """
        for produto in self.produtos:
            if produto.codigo == codigo:
                return False
        return True

    def buscar_produto(self, codigo):
        """
        Busca um produto pelo código.

        :param codigo: Código do produto
        :return: Instância da classe Produto se encontrado, None caso contrário
        """
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def remover_produto(self, codigo):
        """
        Remove um produto pelo código.

        :param codigo: Código do produto
        """
        produto = self.buscar_produto(codigo)
        if produto:
            self.produtos.remove(produto)
            print(f"Produto {produto.nome} removido com sucesso!")
        else:
            print("Erro: Produto não encontrado.")

    def listar_produtos(self):
        """
        Lista todos os produtos cadastrados.
        """
        for produto in self.produtos:
            print(produto)

class Caixa:
    def __init__(self):
        """
        Inicializa o caixa com valores iniciais e finais.
        """
        self.valor_inicial = 0
        self.valor_final = 0
        self.vendas = []

    def abrir_caixa(self, valor_inicial):
        """
        Abre o caixa com um valor inicial.

        :param valor_inicial: Valor inicial do caixa
        """
        self.valor_inicial = valor_inicial
        self.valor_final = valor_inicial
        print(f"O caixa está iniciando com R$ {valor_inicial:.2f}.")

    def nova_venda(self, mercado):
        """
        Inicia uma nova venda, permitindo adicionar produtos ao carrinho.

        :param mercado: Instância da classe Mercado
        """
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
        """
        Finaliza a venda, exibindo o resumo e atualizando o valor final do caixa.

        :param carrinho: Lista de produtos no carrinho
        """
        total = 0
        print("Resumo da venda:")
        for item in carrinho:
