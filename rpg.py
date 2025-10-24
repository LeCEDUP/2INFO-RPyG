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


       