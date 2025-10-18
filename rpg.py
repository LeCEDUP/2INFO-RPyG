# RPG - Vitor Eduardo dos Santos de Oliveira - 2-Info-11
import time

# Importação das classes
from itens.item import Item
from itens.armadura import Armadura
from itens.arma import Arma
from personagens.heroi import Heroi
from personagens.monstro import Inimigo

#e Armas
pistola_blaster = Arma("Pistola Blaster", 8, "Um blaster antigo com notáveis marcas de uso, há um símbolo do império talhado em sua superfície junto com um código de identificação de stormtrooper.")
fuzil_blaster = Arma("Fuzil Blaster", 10, "...")
sniper_blaster = Arma("Fuzil de Precisão Blaster", 12, "...")
sabre_normal = Arma("Sabre de Luz", 19, "...")
sabre_energizado = Arma("Sabre de Luz Energizado", 24, "...")
sabre_amaldicoado = Arma("Sabre de Luz Amaldiçoado", 29, "...")

# Armaduras
am_aldeao = Armadura("Vestes de Aldeão", 2, "...")
am_metal = Armadura("Reforço de Metal", 4, "...")
am_stormtrooper = Armadura("Armadura de Stormtrooper", 8, "...")
am_deathtrooper = Armadura("Armadura de Deathtrooper", 12, "...")
am_sith = Armadura("Armadura Sith", 16, "...")

# Itens
cristal_kyber = Item("Cristal Kyber", "...")

# Hérois
luke_skywalker = Heroi("Luke Skywalker", 180, 12, 6)
han_solo = Heroi("Han Solo", 195, 9, 7)

# Inimigos
storm_strooper = Inimigo("Stormtrooper", 55, 3, 3, "Soldado Imperial")
death_trooper = Inimigo("Deathtrooper", 75, 5, 6, "Soldado Imperial")
lorde_sith = Inimigo("Lorde Sith", 170, 14, 8, "Lorde Sith")

# Funções Principais:

def pausa(tempo: float):
    time.sleep(tempo)

def menu_principal():
    pausa(1)
    print("\n --- Menu Principal ---")
    print("1. Iniciar")
    print("2. Criar novo personagem")
    print("3. Sair \n")

def jogo():
    print("Teste")

# Main
print("Bem vindo RPG de Star Wars puramente em Python!")

while True:        
    menu_principal()
    escolha = input("Escolha uma opção: ")
    
    if escolha is not None:
        match escolha:
            case '1':
                pausa(1)
                print("\n Iniciando... \n")
                pausa(1)
                jogo()
            
            case '2':
                print("\n Em breve!")

            case '3':
                print("\n Salvando...")
                pausa(1)
                print("\n Desligando... \n")
                pausa(1)
                break

            case _:
                print("\n Escolha uma opção válida!")
    else:
        print("\n Você deve escolhar uma opção!")