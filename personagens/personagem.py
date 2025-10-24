class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, inimigo):
        dano = max(0, self.ataque - inimigo.defesa)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
