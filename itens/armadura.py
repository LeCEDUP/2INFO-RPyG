from itens.item import Item

class Armadura(Item):
    def __init__(self, nome, defesa):
        super().__init__(nome)
        self.defesa = defesa
