import random

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa) + random.randint(0, 9)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} - Vida restante: {self.vida} \n")

    def esta_vivo(self):
        return self.vida > 0