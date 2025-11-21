from .item import Item

class Armadura(Item):
    armaduras = []
    def __init__(self, nome: str, bonus_defesa: int, descricao: str):
        super().__init__(nome, descricao)
        self.bonus_defesa = bonus_defesa
        Armadura.armaduras.append(self)