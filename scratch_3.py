class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")

class Professor(Pessoa):
    def __init__(self, nome, departamento):
        super().__init__(nome)
        self.departamento = departamento

    def apresentar(self):
        print(f"Sou o Professor {self.nome} do departamento de {self.departamento.nome}")

class Departamento:
        def __init__(self, nome):
            self.nome = nome

departamentoMatematica = Departamento("Matemática")
professorStephenson = Professor("Stephenson", departamentoMatematica)

departamentoPortugues = Departamento("Portugues")
professorJoseAugusto= Professor("José Augusto", departamentoPortugues)

departamentoCiencias= Departamento("Ciências")
professorHilton = Professor("Hilton", departamentoCiencias)

departamentoHistoria = Departamento("História")
professorNelson = Professor("Nelson", departamentoHistoria)

departamentoGeografia = Departamento("Geografia")
professorXimbiu = Professor("Ximbiu", departamentoGeografia)

#imprimir
professorStephenson.apresentar()
professorJoseAugusto.apresentar()
professorHilton.apresentar()
professorNelson.apresentar()
professorXimbiu.apresentar()




