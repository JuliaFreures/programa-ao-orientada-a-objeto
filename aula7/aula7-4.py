class Pessoa:
    def __init__(self, nome, idade, **kwargs):
        self.nome = nome
        self.idade = idade
        print(f"[Pessoa] {self.nome}, {self.idade} anos criada.")

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


class Trabalhador(Pessoa):
    def __init__(self, profissao, **kwargs):
        super().__init__(**kwargs)
        self.profissao = profissao
        print(f"[Trabalhador] Profissão: {self.profissao}")

    def trabalhar(self):
        return f"{self.nome} está trabalhando como {self.profissao}."


class Estudante(Pessoa):
    def __init__(self, curso, **kwargs):
        super().__init__(**kwargs)
        self.curso = curso
        print(f"[Estudante] Curso: {self.curso}")

    def estudar(self):
        return f"{self.nome} está estudando {self.curso}."


class Estagiario(Trabalhador, Estudante):
    def __init__(self, empresa, **kwargs):
        super().__init__(**kwargs)
        self.empresa = empresa
        print(f"[Estagiario] Empresa: {self.empresa}")

    def rotina(self):
        return f"{self.nome} estagia na empresa {self.empresa}, trabalha como {self.profissao} e estuda {self.curso}."


estagiario1 = Estagiario(
    nome="Lucas",
    idade=21,
    profissao="Assistente de TI",
    curso="Engenharia da Computação",
    empresa="TechCorp"
)

print(estagiario1.apresentar())
print(estagiario1.trabalhar())
print(estagiario1.estudar())
print(estagiario1.rotina())
