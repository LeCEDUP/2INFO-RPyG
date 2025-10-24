import random

# --------- CLASSES ----------
class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.itens = []

    def equipar_item(self, item):
        self.itens.append(item)
        if isinstance(item, Arma):
            self.ataque += item.bonus_ataque
        elif isinstance(item, Armadura):
            self.defesa += item.defesa
