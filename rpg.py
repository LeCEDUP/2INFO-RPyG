import random
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

def introducao():
    maiorfrase = "Você é Harry Potter. Dementadores e Lord Voldemort estão à solta."
    print("="*65)
    print(" BEM-VINDO AO RPG DE HARRY POTTER ")
    print("="*65)
    print(maiorfrase)
    print("Equipe-se, lute e proteja Hogwarts")
    print("="*len(maiorfrase))

def menu_principal():
    print("\nMENU PRINCIPAL")
    print("1 - Iniciar Jogo")
    print("2 - Sair")
    return input("Escolha uma opção: ")

def monstro_atacar(monstro, heroi):
    dano = random.randint(monstro.ataque - 5, monstro.ataque + 5) - heroi.defesa
    if dano < 0:
        dano = 0
    heroi.vida -= dano
    print(f"{monstro.nome} atacou {heroi.nome} causando {dano} de dano!")