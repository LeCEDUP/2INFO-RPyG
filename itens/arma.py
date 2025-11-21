from .item import Item

class Arma(Item):
    armas = []
    def __init__(self, nome: str, bonus_ataque: float, descricao: str):
        super().__init__(nome, descricao)
        self.bonus_ataque = bonus_ataque
        Arma.armas.append(self)
