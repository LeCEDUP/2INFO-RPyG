from .protagonista import Personagem

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo="Comum"):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo