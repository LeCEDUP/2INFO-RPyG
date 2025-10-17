# RPG - Vitor Eduardo dos Santos de Oliveira - 2-Info-11
import time

# Importação das classes
from itens.item import Item
from itens.armadura import Armadura
from itens.arma import Arma
from personagens.heroi import Heroi
from personagens.monstro import Inimigo

# Criação de Armas
pistola_blaster = Arma("Pistola Blaster", 8, "Um blaster antigo com notáveis marcas de uso, há um símbolo do império talhado em sua superfície junto com um código de identificação de stormtrooper.")
fuzil_blaster = Arma("Fuzil Blaster", 10, "...")
sniper_blaster = Arma("Fuzil de Precisão Blaster", 12, "...")
sabre_normal = Arma("Sabre de Luz", 19, "...")
sabre_energizado = Arma("Sabre de Luz Energizado", 24, "...")
sabre_amaldicoado = Arma("Sabre de Luz Amaldiçoado", 29, "...")

# Criação de Hérois
luke_skywalker = Heroi("Luke Skywalker", 180, 12, 6)
han_solo = Heroi("Han Solo", 195, 9, 7)
#Criação de Inimigos
storm_strooper = Inimigo("Stormtrooper", 55, 3, 3, "Soldado Imperial")
death_trooper = Inimigo("Deathtrooper", 75, 5, 6, "Soldado Imperial")
lorde_sith = Inimigo("Lorde Sith", 170, 14, 8, "Lorde Sith")

# Início

print("Bem vindo ao RPyG de Star Wars!")

# Funções Principais:

def menu_principal():
    print("\n --- Menu Principal ---")
    print("1. Iniciar")
    print("2. Criar novo personagem")
    print("3. Sair")

def jogar():
    pass

# Main

while True:        
    menu_principal()
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            time.sleep(1)
            print("Iniciando...")
        
        case 2:
            pass

        case 3:
            print("Desligando...")
            time.sleep(1)
            print("Salvando...")
            time.sleep(1)
            break