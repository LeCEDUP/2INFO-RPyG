import random

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        
    def atacar(self, alvo):
        if  random.randint(1, 10) == 1:
            dano = max(0, self.ataque - alvo.defesa)
            self.ataque_critico(alvo, dano)
        else:
            dano = max(0, self.ataque - alvo.defesa)
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
            alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def ataque_critico(self, alvo, dano):
        dano_critico = dano * 2
        print(f"{self.nome} atacou {alvo.nome} causando {dano_critico} de dano crítico.")
        alvo.receber_dano_critico(dano_critico)

    def receber_dano_critico(self, dano_critico):
        self.vida -= dano_critico
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano_critico} de dano crítico. Vida restante: {self.vida}")