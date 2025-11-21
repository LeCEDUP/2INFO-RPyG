class Monstro:
    def __init__(self, nome, vida, dano, defesa, tipo="Monstro"):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.defesa = defesa
        self.tipo = tipo

    def atacar(self, alvo):
        print(f"\n {self.nome} cospe uma rajada de fogo em {alvo.nome}, causando {20} de dano!")
        alvo.receber_dano(self.dano)

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        print(f"{self.nome} recebeu {dano_final} de dano! (Defendeu {self.defesa})")
        if self.vida < 0:
            self.vida = 0
