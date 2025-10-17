from .item import Item

class Arma(Item):
    def __init__(self, nome, bonus_ataque, raridade, descricao):
        super().__init__(nome, descricao)
        self.bonus_ataque = bonus_ataque
        self.raridade = raridade