# Desenvolva o seu jogo aqui
from itens.arma import Arma
from itens.armadura import Armadura
from itens.item import Item
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import time

def pausa(texto, segundos=1):
    print(texto)
    time.sleep(segundos)

def introducao():
    print("🔥 Demon Slayer RPG 🔥")
    print("Você é um caçador de demônios em treinamento na Corporação dos Caçadores.")
    print("Seu objetivo: eliminar os demônios que ameaçam os humanos durante a noite.")
    print("Prepare sua espada Nichirin e sua respiração.\n")
