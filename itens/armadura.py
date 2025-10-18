from .item import Item

class Armadura(Item):
    def __init__(self, nome: str, bonus_defesa: int, descricao: str):
        super().__init__(nome, descricao)
        self.bonus_defesa = bonus_defesa