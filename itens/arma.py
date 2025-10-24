from itens.item import Item

class Arma(Item):
    def __init__(self, nome, descricao, dano):
        super().__init__(nome, descricao)
        self.dano = dano
