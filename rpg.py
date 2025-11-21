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

    def batalha(heroi, inimigo, ataques_heroi=1, ataques_inimigo=1):
    print(f"\n A batalha começou entre {heroi.nome} e {inimigo.nome} ({inimigo.tipo})!")

    while heroi.vida > 0 and inimigo.vida > 0:
        input(f"\nPressione ENTER para que {heroi.nome} ataque...")

        for _ in range(ataques_heroi):
            heroi.atacar(inimigo)
            if inimigo.vida <= 0:
                print(f"\n {heroi.nome} derrotou o {inimigo.nome}! O reino está salvo!")
                return

        for _ in range(ataques_inimigo):
            print(f"\n O {inimigo.nome} prepara um ataque de fogo!")
            inimigo.atacar(heroi)
            if heroi.vida <= 0:
                print(f"\n {heroi.nome} foi derrotado pelo {inimigo.nome}... O reino está perdido.")
                return

        print(f"\n {heroi.nome}: {heroi.vida} de vida |  {inimigo.nome}: {inimigo.vida} de vida")

        def iniciar_aventura():
    nome = input("Qual é o nome do seu herói? ")
    vida_heroi = 100
    dano_heroi = int(input("Defina o dano base do herói: "))
    ataques_heroi = int(input("Quantos ataques o herói pode fazer por turno? "))

     ataques_dragao = 1 
    heroi = Heroi(nome, vida_heroi, dano_heroi, 5)
    dragao = Monstro("Dragão Ancião", 200, 20, 10, tipo="Dragão") 

     espada = Arma("Espada Dragonsword", "Forjada com fogo de dragão.", 10)
    armadura = Armadura("Armadura de Escamas Vermelhas", "Protege contra fogo.", 8)

    heroi.equipar_arma(espada)
    heroi.equipar_armadura(armadura)

    batalha(heroi, dragao, ataques_heroi, ataques_dragao)

def main():
    introducao()
    while True:
        escolha = menu_principal()
        if escolha == "1":
            iniciar_aventura()
        elif escolha == "2":
            sobre()
        elif escolha == "3":
            print("Até mais, bravo aventureiro! ")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
