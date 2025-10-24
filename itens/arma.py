from .item import Item

class Arma(Item):
    def __init__(self, nome, dano, descricao=""):
       
        super().__init__(nome, descricao)
        
       
        self.dano = dano