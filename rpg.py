import random

class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.itens = []

class Monstro:
    def __init__(self, nome, vida, ataque, defesa, tipo):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo

class Arma:
    def __init__(self, nome, dano, bonus_ataque):
        self.nome = nome
        self.dano = dano
        self.bonus_ataque = bonus_ataque

class Armadura:
    def __init__(self, nome, defesa):
        self.nome = nome
        self.defesa = defesa

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Iniciar Aventura\n2 - Sair\n3 - Ver Introdução")
    return input("Escolha: ")

class Heroi:
    ...
    def atacar(self, inimigo):
        dano_bruto = random.randint(self.ataque - 3, self.ataque + 3)
        dano_real = max(dano_bruto - inimigo.defesa, 0)
        if random.random() < 0.15:
            dano_real = int(dano_real * 1.8)
            print("✨ CRÍTICO GLAMOUR ✨")
        inimigo.vida = max(inimigo.vida - dano_real, 0)
        print(f"{self.nome} atacou {inimigo.nome} causando {dano_real} de dano! Vida restante: {inimigo.vida}\n")

class Monstro:
    ...
    def atacar(self, inimigo):
        dano_bruto = random.randint(self.ataque - 3, self.ataque + 3)
        dano_real = max(dano_bruto - inimigo.defesa, 0)
        if random.random() < 0.15:
            dano_real = int(dano_real * 1.8)
            print("⚡ POLLY CRÍTICA! ⚡")
        inimigo.vida = max(inimigo.vida - dano_real, 0)
        print(f"{self.nome} contra-ataca causando {dano_real} de dano! Vida restante: {inimigo.vida}\n")

class Heroi:
    ...
    def equipar_item(self, item):
        self.itens.append(item)
        if isinstance(item, Arma):
            self.ataque += item.bonus_ataque
        elif isinstance(item, Armadura):
            self.defesa += item.defesa

       