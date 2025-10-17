# RPG - Vitor Eduardo dos Santos de Oliveira - 2-Info-11

from time import *

# Importação das classes:

from itens.item import Item
from itens.armadura import Armadura
from itens.arma import Arma
from personagens.heroi import Heroi
from personagens.monstro import Monstro

# Menu:

print("Bem vindo ao RPyG de Star Wars!")

print("1. Iniciar")
print("2. Criar novo personagem")
print("3. Sair")

opcao_menu = input("Escolha uma opção: ")

match opcao_menu:
    case '1':
        print("iniciar")
    
    case '2':
        pass

    case '3':
        print("Desligando...")
        time.sleep(0.2)