class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

class Livro:
    def __init__(self, titulo, autor, status="disponível"):
        self.titulo = titulo
        self.autor = autor
        self.status = status

        if status == "emprestado":
            print(f"O livro '{self.titulo}' está indisponível.")
        else:
            print(f"O livro '{self.titulo}' está disponível")

class Usuario(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def pegar_livro_emprestado(self, livro):
        if livro.status == "disponível":
            livro.status = "emprestado"
            print(f"{self.nome} pegou o livro '{livro.titulo}' emprestado.")
        else:
            print(f"O livro '{livro.titulo}' está indisponível.")

    def devolver_livro(self, livro):
        livro.status = "disponível"
        print(f"{self.nome} devolveu o livro '{livro.titulo}'.")

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def emprestar_livro(self, usuario, livro):
        usuario.pegar_livro_emprestado(livro)





     # Criando a biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Criando um usuário
usuario1 = Usuario("Ana", 30)

# Adicionando usuário à biblioteca
biblioteca.adicionar_usuario(usuario1)

# Empréstimo do livro1
print("\n--- Empréstimo ---")
biblioteca.emprestar_livro(usuario1, livro1)

# Tentando emprestar novamente o mesmo livro
print("\n--- Tentativa de novo empréstimo do mesmo livro ---")
biblioteca.emprestar_livro(usuario1, livro1)

# Devolução do livro
print("\n--- Devolução ---")
usuario1.devolver_livro(livro1)

# Tentando emprestar novamente (agora deve funcionar)
print("\n--- Novo empréstimo após devolução ---")
biblioteca.emprestar_livro(usuario1, livro1)

# Mostrando status dos livros
print("\n--- Status dos livros ---")
for livro in biblioteca.livros:
    print(f"{livro.titulo}: {livro.status}")
   

        