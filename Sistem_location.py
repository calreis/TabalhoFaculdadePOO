from datetime import datetime

class Marca:
    def __init__(self, nome: str):
        self.nome = nome

class Modelo:
    def __init__(self, nome: str, marca: Marca):
        self.nome = nome
        self.marca = marca

class Veiculo:
    def __init__(self, placa, cor, ano, combustivel, num_portas, quilometragem,
                 renavam, chassi, valor_locacao, modelo: Modelo):
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.num_portas = num_portas
        self.quilometragem = quilometragem
        self.renavam = renavam
        self.chassi = chassi
        self.valor_locacao = valor_locacao
        self.modelo = modelo
        self.disponivel = True

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Veículo {self.placa} alugado com sucesso.")
        else:
            print(f"Veículo {self.placa} não está disponível.")

    def devolver(self):
        self.disponivel = True
        print(f"Veículo {self.placa} devolvido com sucesso.")

class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

class Locacao:
    def __init__(self, cliente: Cliente, veiculo: Veiculo):
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_hora_locacao = datetime.now()
        self.data_hora_devolucao = None

        if veiculo.disponivel:
            veiculo.alugar()
        else:
            raise Exception("Veículo indisponível para locação.")

    def devolver_veiculo(self):
        self.data_hora_devolucao = datetime.now()
        self.veiculo.devolver()

# Exemplo de uso
if __name__ == "__main__":
    marca = Marca("Toyota")
    modelo = Modelo("Corolla", marca)
    veiculo = Veiculo("ABC1234", "Preto", 2022, "Gasolina", 4, 50000, "123456789", "9BWZZZ377VT004251", 199.99, modelo)

    cliente = Cliente("João Silva", "123.456.789-00", "(11) 91234-5678", "joao@email.com")

    locacao = Locacao(cliente, veiculo)

    # Após algum tempo...
    locacao.devolver_veiculo()

