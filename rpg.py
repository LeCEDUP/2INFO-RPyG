from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

def introducao():
    print("""
    
                        RPG DOS DRAGÕES 
   
    Em um reino esquecido, dragões despertaram das montanhas
    de fogo e espalham destruição.
    Você, um jovem guerreiro, é a última esperança do reino.
    Derrote o Dragão Ancião e restaure a paz!
    """)

def menu_principal():
    print("""
     MENU PRINCIPAL 
    1. Iniciar aventura
    2. Sobre
    3. Sair
    """)
    return input("Escolha uma opção: ")

def sobre():
    print("""
     Jogo de RPG de texto - Tema: Dragões
    Desenvolvido em Python com orientação a objetos.
    Explore o reino e enfrente o poderoso Dragão Ancião!
    """)