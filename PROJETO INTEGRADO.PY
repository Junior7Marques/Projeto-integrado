class Produto:
    def __init__(self, nome, categoria, quantidade, preco, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, nome, categoria, quantidade, preco, localizacao):
        novo_produto = Produto(nome, categoria, quantidade, preco, localizacao)
        self.produtos.append(novo_produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def atualizar_estoque(self, nome, quantidade, operacao):
        for produto in self.produtos:
            if produto.nome == nome:
                if operacao == "entrada":
                    produto.quantidade += quantidade
                    print(f"Quantidade de '{nome}' atualizada para {produto.quantidade}.")
                elif operacao == "saida":
                    if produto.quantidade >= quantidade:
                        produto.quantidade -= quantidade
                        print(f"Quantidade de '{nome}' atualizada para {produto.quantidade}.")
                    else:
                        print("Quantidade insuficiente em estoque!")
                return
        print("Produto não encontrado.")

    def rastrear_localizacao(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                print(f"Produto '{nome}' está localizado em '{produto.localizacao}' com quantidade em estoque de {produto.quantidade}.")
                return
        print("Produto não encontrado.")

    def gerar_relatorio(self):
        print("Relatório de Estoque:")
        for produto in self.produtos:
            status = ""
            if produto.quantidade < 10:
                status = "Estoque baixo"
            elif produto.quantidade > 100:
                status = "Excesso de estoque"
            else:
                status = "Estoque adequado"
            print(f"Produto: {produto.nome}, Categoria: {produto.categoria}, Quantidade: {produto.quantidade}, Status: {status}")

# Cadastrando dois produtos iniciais
estoque = Estoque()
estoque.cadastrar_produto("Caneta", "Material de Escritório", 50, 1.5, "A1")
estoque.cadastrar_produto("Papel A4", "Material de Escritório", 200, 20, "B3")

# Menu para o usuário
while True:
    print("\nMenu de Opções:")
    print("1. Cadastrar Produto")
    print("2. Atualizar Estoque")
    print("3. Rastrear Localização e quantidade em estoque")
    print("4. Gerar Relatório")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ")
        categoria = input("Categoria: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        localizacao = input("Localização: ")
        estoque.cadastrar_produto(nome, categoria, quantidade, preco, localizacao)
    
    elif opcao == "2":
        nome = input("Nome do Produto: ")
        operacao = input("Digite 'entrada' para adicionar ou 'saida' para remover: ")
        quantidade = int(input("Quantidade: "))
        estoque.atualizar_estoque(nome, quantidade, operacao)
    
    elif opcao == "3":
        nome = input("Nome do Produto: ")
        estoque.rastrear_localizacao(nome)
    
    elif opcao == "4":
        estoque.gerar_relatorio()
    
    elif opcao == "5":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
