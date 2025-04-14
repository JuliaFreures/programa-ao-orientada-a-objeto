#Exercicio 5
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")


class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, taxa_saque=2.50):
        super().__init__(titular, saldo)
        self.taxa_saque = taxa_saque

    def sacar(self, valor):
        valor_total = valor + self.taxa_saque
        if 0 < valor_total <= self.saldo:
            self.saldo -= valor_total
            print(f"Saque de R${valor:.2f} com taxa de R${self.taxa_saque:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque com taxa.")


conta1 = Conta("Maria", 1000)
conta1.depositar(200)
conta1.sacar(300)

print("\n--- Conta Corrente ---")
conta2 = ContaCorrente("João", 1000)
conta2.depositar(500)
conta2.sacar(300)

#Exercicio 6
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def __str__(self):
        return f"Aluno: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} adicionado ao professor {self.nome}.")
        else:
            print("Só é possível adicionar instâncias da classe Aluno.")

    def listar_alunos(self):
        print(f"\nLista de alunos do professor {self.nome}:")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in self.alunos:
                print(f"- {aluno}")


aluno1 = Aluno("Lucas", 20, "A001")
aluno2 = Aluno("Carla", 22, "A002")

professor = Professor("Carlos", 45, "Matemática")
professor.adicionar_aluno(aluno1)
professor.adicionar_aluno(aluno2)
professor.listar_alunos()

#Exercicio 7
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Livro(Produto):
    def __init__(self, nome, preco, autor, paginas):
        super().__init__(nome, preco)
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.nome} (Autor: {self.autor}, {self.paginas} páginas) - R${self.preco:.2f}"


class Eletronico(Produto):
    def __init__(self, nome, preco, marca, garantia_meses):
        super().__init__(nome, preco)
        self.marca = marca
        self.garantia_meses = garantia_meses

    def __str__(self):
        return f"Eletrônico: {self.nome} (Marca: {self.marca}, Garantia: {self.garantia_meses} meses) - R${self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)
            print(f"{produto.nome} adicionado ao carrinho.")
        else:
            print("Só é possível adicionar produtos válidos.")

    def listar_produtos(self):
        print("\nProdutos no carrinho:")
        if not self.produtos:
            print("Carrinho vazio.")
        else:
            for produto in self.produtos:
                print(f"- {produto}")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        print(f"\nTotal da compra: R${total:.2f}")
        return total

livro1 = Livro("Acotar", 59.90, "Sarah J.", 320)
eletronico1 = Eletronico("Fone Bluetooth", 199.90, "JBL", 12)


carrinho = Carrinho()
carrinho.adicionar_produto(livro1)
carrinho.adicionar_produto(eletronico1)


carrinho.listar_produtos()
carrinho.calcular_total()



