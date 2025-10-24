class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def exibir_informacoes(self):
        print(f" {self.nome}: {self.descricao}")
