import random

class Personagem:
    def __init__(self, nome, vida, ataque, defesa, dano_critico):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.dano_critico = dano_critico

    def atacar(self, alvo):
        if  random.randint(1, 50) == 1:
            ataque_critico()
        else:
            dano = max(0, self.ataque - alvo.defesa)
            alvo.receber_dano(dano)
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def ataque_critico(self, dano_critico, alvo):
        dano = dano * 2
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano crítico.")
