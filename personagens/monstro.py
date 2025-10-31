from .personagem import Personagem

class Inimigo(Personagem):
    inimigos = []
    def __init__(self, nome: str, vida: float, ataque: float, defesa: float, tipo: str, exp_valor: float):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo
        self.exp_valor = exp_valor
        Inimigo.inimigos.append(self)