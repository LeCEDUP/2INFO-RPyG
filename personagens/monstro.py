class Monstro:
    def __init__(self, nome, vida, ataque, defesa, tipo):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo

    def atacar(self, inimigo):
        print(" {self.nome} contra-ataca {inimigo.nome} com {self.ataque} de poder!")
        inimigo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        dano_real = max(dano - self.defesa, 0)
        self.vida -= dano_real
        print(f"{self.nome} levou {dano_real} de dano! Vida restante: {self.vida}")
