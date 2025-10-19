from .personagem import Personagem

class Inimigo(Personagem):
    inimigos = []
    def __init__(self, nome, vida, ataque, defesa, tipo, exp_valor):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo
        self.exp_valor = exp_valor
        Inimigo.inimigos.append(self)