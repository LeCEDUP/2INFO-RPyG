# RPG - Vitor Eduardo dos Santos de Oliveira - 2-Info-11
import random
import time

# Importação das classes
from itens.item import Item
from itens.armadura import Armadura
from itens.arma import Arma
from personagens.heroi import Heroi
from personagens.monstro import Inimigo

# Armas
bastao_madeira = Arma("Bastão de Madeira", 6, "...")
pistola_blaster = Arma("Pistola Blaster", 6, "Um blaster antigo com notáveis marcas de uso, há um símbolo do império talhado em sua superfície junto com um código de identificação de stormtrooper.")
fuzil_blaster = Arma("Fuzil Blaster", 10, "...")
sniper_blaster = Arma("Fuzil de Precisão Blaster", 12, "...")
sabre_normal = Arma("Sabre de Luz", 19, "...")
sabre_energizado = Arma("Sabre de Luz Energizado", 24, "...")
sabre_amaldicoado = Arma("Sabre de Luz Amaldiçoado", 29, "...")

armas = Arma.armas

# Armaduras
am_aldeao = Armadura("Vestes de Aldeão", 2, "...")
am_contrabandista = Armadura("Vestes de Contrabandista", 2, "...")
am_metal = Armadura("Reforço de Metal", 4, "...")
am_stormtrooper = Armadura("Armadura de Stormtrooper", 8, "...")
am_deathtrooper = Armadura("Armadura de Deathtrooper", 12, "...")
am_sith = Armadura("Armadura Sith", 16, "...")

armaduras = Armadura.armaduras

# Itens
cristal_kyber = Item("Cristal Kyber", "...")

# Hérois
luke_skywalker = Heroi("Luke Skywalker", 180, 20, 6, inventario=[bastao_madeira, am_aldeao])
han_solo = Heroi("Han Solo", 195, 21, 7, inventario=[pistola_blaster, am_contrabandista])

herois = Heroi.herois

# Inimigos
storm_strooper = Inimigo("Stormtrooper", 55, 10, 3, "Soldado Imperial", 110)
death_trooper = Inimigo("Deathtrooper", 75, 40, 6, "Soldado Imperial", 250)
lorde_sith = Inimigo("Lorde Sith", 170, 80, 8, "Lorde Sith", 800)

inimigos = Inimigo.inimigos

# Funções Principais:

def pausa(tempo: float):
    time.sleep(tempo)

def menu_principal():
    pausa(1)
    print("\n --- Menu Principal ---")
    print("1. Iniciar")
    print("2. Criar novo personagem")
    print("3. Sair \n")

def mostrar_herois():
    num_heroi = 1
    for heroi in herois:
        print(f"{num_heroi}. {heroi.nome} - HP: {heroi.vida}, Ataque: {heroi.ataque}, Defesa: {heroi.defesa}.")
        num_heroi = num_heroi + 1

def escolher_heroi():
    while True:
        print("\n Hérois disponíveis:")
        mostrar_herois()
        escolha = input("Escolha uma opção: ")
        if escolha is not None:
            try:
                heroi_escolhido = herois[int(escolha) - 1]
                print(f"Você escolheu {heroi_escolhido.nome}")
                return heroi_escolhido
            except:
                print("\n Escolha uma opção válida!")
        else:
            print("\n Você deve escolher um héroi!")

def encontrar_inimigo(heroi, inimigo):
    print(f"{heroi.nome} encontrou {inimigo.nome}. \n")
    return inimigo

def batalha(heroi, inimigo):
    turno = True
    if heroi.esta_vivo():
        while True:
            if heroi.esta_vivo() and inimigo.esta_vivo():
                if turno:
                    pausa(1)
                    heroi.atacar(inimigo)
                    turno = False
                else:
                    pausa(1)
                    inimigo.atacar(heroi)
                    turno = True
            elif heroi.esta_vivo():
                pausa(1)        
                heroi.ganhar_experiencia(inimigo.exp_valor)
                return heroi.esta_vivo()
            elif inimigo.esta_vivo():
                return heroi.esta_vivo()
            
def encontrar_item(heroi, tipo_item):
    match tipo_item:
        case "armas":
            arma_encontrada = armas[random.randint(0, len(armas) - 1)]
            print(f"{heroi.nome} encontrou {arma_encontrada.nome} (+{arma_encontrada.bonus_ataque} Dano)")
            heroi.ataque += arma_encontrada.bonus_ataque
            heroi.inventario.append(arma_encontrada)
        case "armaduras":
            armadura_encontrada = armaduras[random.randint(0, len(armaduras) - 1)]
            print(f"{heroi.nome} encontrou {armadura_encontrada.nome} (+{armadura_encontrada.bonus_defesa} Defesa)")
            heroi.defesa += armadura_encontrada.bonus_defesa
            heroi.inventario.append(armadura_encontrada)

def jogo():
    heroi = escolher_heroi()
    print(f"{heroi.nome} estava imprisionado nas celas de uma nave imperial, porém por um erro na central de controle da nave, as celas se abrem, será que conseguirá escapar? \n")
    pausa(2)
    print("Ao sair da cela, há algumas armas e armaduras jogadas pelo chão do corredor da prisão. \n")
    pausa(1.5)
    print(f"{heroi.nome} começa sua história com {heroi.inventario[0].nome} (+{heroi.inventario[0].bonus_ataque} Dano) e {heroi.inventario[1].nome} (+{heroi.inventario[1].bonus_defesa} Defesa) \n")
    
    if batalha(heroi, encontrar_inimigo(heroi, storm_strooper)):
        print(f"Após derrotar {storm_strooper.nome}, {heroi.nome} avista uma arma no chão.")
        pausa(1)
        encontrar_item(heroi, "armas")
        pausa(1)
        print(f"\n {heroi.nome} segue andando pelos corredores, e avista um grupo de soldados imperiais vestidos de preto. \n")
        pausa(1)
        print(f"Um deles olha para {heroi.nome} e diz: \n")
        pausa(1)
        print(f"{death_trooper.nome}: Eu cuido desse fugitivo. \n")
    else:
        pausa(1)
        print(f"\n Ao tentar fugir da nave {heroi.nome} é derrotado, esse é o fim da história de nosso herói! \n")
    
    if heroi.esta_vivo():
        if batalha(heroi, encontrar_inimigo(heroi, death_trooper)):
            pausa(1)
            print(f"Após derrotar o deathtrooper, {heroi.nome} avista uma arma e uma armadura no chão. \n")
            pausa(1)
            encontrar_item(heroi, "armas")
            pausa(0.5)
            encontrar_item(heroi, "armaduras")
            print(f"{heroi.nome} avista a porta de saída no final de um longo corredor.\n")
            pausa(1)
            print(f"{heroi.nome}: Preciso fugir agora!\n")
            pausa(0.5)
            print(f"Para a infelicidade de {heroi.nome} surge das sombras uma figura escura, vestindo trajes negros.\n")
            pausa(2)
            print(f"\n Dessa figura se observa um objeto metálico que logo se revela um sabre de luz vermelho, a cor pertencente aos lordes sith. \n")
            pausa(2)
        else:
            pausa(1)
            print(f"Mesmo com garra, {heroi.nome} é derrotado por um soldado imperial, esse é o fim da história de nosso herói.")
            
    if heroi.esta_vivo():
        if batalha(heroi, encontrar_inimigo(heroi, lorde_sith)):
            print(f"{heroi.nome} com muita perseverança e habilidade consegue escapar da nave imperial. \n")
            pausa(1)
            print(f"Um final digno à história de {heroi.nome}.")
            pausa(2)
            print("Fim.")
        else:
            pausa(1)
            print(f"Por mais que {heroi.nome} estivesse perto de escapar, ele foi derrotado por um {lorde_sith.nome}, esse é o triste fim da história de nosso herói.")


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

            case '4':
                break

            case _:
                print("\n Escolha uma opção válida!")
    else:
        print("\n Você deve escolhar uma opção!")