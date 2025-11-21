from itens.item import Item

class Arma(Item):
    def __init__(self, nome, dano, bonus_ataque):
        super().__init__(nome)
        self.dano = dano
        self.bonus_ataque = bonus_ataque

