class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.itens = []

    def equipar_item(self, item):
        self.itens.append(item)
        print("{self.nome} equipou {item.nome}!")

    def atacar(self, inimigo):
        dano_total = self.ataque
        for item in self.itens:
            if hasattr(item, 'dano'):
                dano_total += item.dano
            if hasattr(item, 'bonus_ataque'):
                dano_total += item.bonus_ataque

        print("{self.nome} ataca {inimigo.nome} causando {dano_total} de dano!")
        inimigo.receber_dano(dano_total)

    def receber_dano(self, dano):
        dano_real = max(dano - self.defesa, 0)
        self.vida -= dano_real
        print("{self.nome} recebeu {dano_real} de dano! Vida restante: {self.vida}")


