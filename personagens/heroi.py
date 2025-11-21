class Heroi:
    def __init__(self, nome, vida, dano, defesa):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.defesa = defesa
        self.arma = None
        self.armadura = None

    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou {arma.nome}! (+{arma.dano} dano)")

    def equipar_armadura(self, armadura):
        self.armadura = armadura
        print(f"{self.nome} vestiu {armadura.nome}! (+{armadura.defesa} defesa)")

    def atacar(self, inimigo):
        dano_total = self.dano + (self.arma.dano if self.arma else 0)
        print(f"{self.nome} golpeia {inimigo.nome}, causando {dano_total} de dano!")
        inimigo.receber_dano(dano_total)

    def receber_dano(self, dano):
        defesa_total = self.defesa + (self.armadura.defesa if self.armadura else 0)
        dano_final = max(0, dano - defesa_total)
        self.vida -= dano_final
        print(f"{self.nome} recebeu {dano_final} de dano! (Defendeu {defesa_total})")
        if self.vida < 0:
            self.vida = 0
