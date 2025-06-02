# criar
class Cliente:
    def __init__ (self, nome, cpf, renda_mensal, score_credito):
        self.nome = nome
        self.cpf = cpf
        self.renda_mensal = renda_mensal
        self.score_credito = score_credito

#verificação de crédito
    def verificar_credito(self):
        if self.renda_mensal >= 2000 and self.score_credito >= 600:
            print(f"O cliente {self.nome} teve o crédito aprovado para concessao de compras.")
        else:
            print(f"O cliente {self.nome} teve o crédito negado.")

# imprimir mensagem para o cliente
cliente1 = Cliente("Beatriz", "456.789.123-15", 3000.00, 800)
cliente2 = Cliente("Alessandra", "123.789.456-26", 1500.00, 700)
cliente3 = Cliente("Nathan", "123.456.789-10", 2000.00, 500)

# Verificar crédito para o cliente
cliente1.verificar_credito()
cliente2.verificar_credito()
cliente3.verificar_credito()


