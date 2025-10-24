from .personagem import Personagem

class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo