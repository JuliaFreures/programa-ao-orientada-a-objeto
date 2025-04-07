#Exercicio 1
class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def inscrever(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f'{self.nome} se inscreveu na disciplina {disciplina.nome}.')
disciplina1 = Disciplina("TI")


aluno1 = Aluno("João")
aluno1.inscrever(disciplina1)
aluno2 = Aluno("Carla")
aluno2.inscrever(disciplina1)
aluno3 = Aluno("Pedro")
aluno3.inscrever(disciplina1)

print("-------------------------------")

#Exercicio 2
class Empregado:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)
        print(f'{empregado.nome} foi adicionado ao departamento {self.nome}.')

    def listar_empregados(self):
        print(f'Empregados do Departamento {self.nome}:')
        if not self.empregados:
            print('Não há empregados no departamento.')
        else:
            for empregado in self.empregados:
                print(f'- {empregado.nome}')

empregado1= Empregado("Ana")
empregado2= Empregado("gabriel")
empregado3= Empregado("Clara")

departamento_ti = Departamento("TI")
departamento_ti.adicionar_empregado(empregado1)
departamento_ti.adicionar_empregado(empregado2)
departamento_ti.adicionar_empregado(empregado3)

departamento_ti.listar_empregados()

print("-------------------------------")
#Exercicio 3
class Porta:
    def __init__(self, numero):
        self.numero = numero
        self.aberta = False

    def abrir(self):
        self.aberta = True

    def fechar(self):
        self.aberta = False

    def estado(self):
        return "aberta" if self.aberta else "fechada"

class Casa:
    def __init__(self):
        self.portas = [Porta(1), Porta(2), Porta(3)]

    def exibir(self):
        for porta in self.portas:
            print(f'Porta {porta.numero} está {porta.estado()}.')

minha_casa = Casa()


minha_casa.portas[0].abrir()
minha_casa.portas[2].fechar()


minha_casa.exibir()

print("-------------------------------")
#Exercicio 4
class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def mover(self):
        print(f"O carro está se movendo a {self.velocidade} km/h.")

class Bicicleta(Veiculo):
    def __init__(self):
        self.velocidade = 0

    def pedalar(self):
        self.velocidade += 5

    def mover(self):
        print(f"A bicicleta está se movendo a {self.velocidade} km/h.")

carro = Carro()
bicicleta = Bicicleta()

carro.acelerar()
carro.mover()

bicicleta.pedalar()
bicicleta.mover()
bicicleta.pedalar()
bicicleta.mover()
bicicleta.pedalar()
bicicleta.mover()





