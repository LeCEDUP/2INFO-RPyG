from .personagem import Personagem

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo, experiencia=10):
        """Monstro com um valor de experiência que concede ao ser derrotado.

        experiencia: quantidade de XP que o herói ganha ao derrotar este monstro.
        """
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo
        self.experiencia = experiencia