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