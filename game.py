"""Runner interativo que reutiliza as instâncias definidas em `rpg.py`.
Execute: python game.py
"""
from rpg import heroi, MONSTROS, Carne, Carne_Podre, Carne_Fresca, Pocao_Negra, Pedra_Azul, Carne_Mostro, Osso, Escudo
from personagens.monstro import Monstro
import random
import sys


def imprimir_status():
    print(f"\n--- Status de {heroi.nome} ---")
    print(f"Vida: {heroi.vida}")
    print(f"Ataque: {heroi.ataque}")
    print(f"Defesa: {heroi.defesa}")
    print(f"Nível: {getattr(heroi, 'nivel', '?')}")
    print(f"Inventário: {[item.nome for item in heroi.inventario]}")


def usar_item(nome_item):
    encontrados = [i for i in heroi.inventario if i.nome.lower() == nome_item.lower()]
    if not encontrados:
        print("Você não tem esse item no inventário.")
        return
    item = encontrados[0]
    if item is Carne:
        heroi.vida += 10
        print(f"{heroi.nome} comeu {item.nome} e recuperou 10 de vida.")
    elif item is Carne_Fresca:
        heroi.vida += 30
        print(f"{heroi.nome} comeu {item.nome} e recuperou 30 de vida.")
    elif item is Carne_Podre:
        heroi.vida += 5
        print(f"{heroi.nome} comeu {item.nome} e recuperou 5 de vida.")
    elif item is Pocao_Negra:
        perda = max(1, int(heroi.vida * 0.10))
        ganho = max(1, int(heroi.ataque * 0.15))
        heroi.vida -= perda
        heroi.ataque += ganho
        print(f"{heroi.nome} usou {item.nome}: -{perda} vida, +{ganho} ataque (temporário).")
    elif item is Carne_Mostro:
        ganho = max(1, int(heroi.ataque * 0.30))
        heroi.ataque += ganho
        print(f"{heroi.nome} comeu {item.nome} e ganhou +{ganho} de ataque.")
    elif item is Pedra_Azul:
        ganho = max(1, int(heroi.defesa * 0.10))
        heroi.defesa += ganho
        print(f"{heroi.nome} usou {item.nome} e aumentou a defesa em +{ganho}.")
    else:
        print(f"{item.nome} não tem efeito implementado ainda.")
  
    try:
        heroi.inventario.remove(item)
    except ValueError:
        pass


def encontro_aleatorio():
    monstro = random.choice(MONSTROS)
    inimigo = Monstro(monstro.nome, monstro.vida, monstro.ataque, monstro.defesa, monstro.tipo)
    print(f"\nVocê encontrou um {inimigo.nome} ({inimigo.tipo})!")
    batalha(inimigo)


def batalha(inimigo):
    while heroi.esta_vivo() and inimigo.esta_vivo():
        print(f"\nSua vez: Vida {heroi.vida} | {inimigo.nome}: Vida {inimigo.vida}")
        escolha = input("Escolha: (a)tacar, (u)sar item, (f)ugir: ").strip().lower()
        if escolha == 'a' or escolha == 'atacar':
            heroi.atacar(inimigo)
        elif escolha == 'u' or escolha == 'usar':
            nome_item = input("Digite o nome do item para usar: ")
            usar_item(nome_item)
        elif escolha == 'f' or escolha == 'fugir':
            if random.random() < 0.5:
                print("Você conseguiu fugir!")
                return
            else:
                print("Fuga falhou!")
        else:
            print("Ação inválida.")
            continue

        if inimigo.esta_vivo():
            inimigo.atacar(heroi)

    if heroi.esta_vivo():
        print(f"\nVocê derrotou o {inimigo.nome}!")
        if random.random() < 0.6:
            drop = random.choice([Carne, Carne_Podre, Carne_Fresca, Osso, Escudo])
            heroi.inventario.append(drop)
            print(f"Você encontrou: {drop.nome}.")
        if hasattr(heroi, 'ganhar_experiencia'):
            heroi.ganhar_experiencia(20)
    else:
        print("Você foi derrotado... Fim de jogo.")
        sys.exit(0)


def mostrar_intro():
    print("\n--- Prologue: A Sombra sobre Vale Antigo ---\n")
    print("As brumas cobriram o Vale Antigo. Antigas fortalezas ecoam com passos que não pertencem aos vivos.")
    print("Você é conhecido apenas como 'A Fera', um guerreiro marcado pelas cicatrizes do passado.")
    print("Sua missão: descobrir a origem da corrupção e salvar o que resta do reino. Sobreviva, evolua e escolha seu destino.")


def run_game():
    mostrar_intro()
   
    if not any(i.nome == 'Osso' for i in heroi.inventario):
        heroi.inventario.extend([Osso, Escudo, Carne])

    while True:
        print("\nO que deseja fazer agora?")
        print("1) Explorar")
        print("2) Descansar (recupera 20 vida)")
        print("3) Ver status")
        print("4) Ver inventário / equipar item")
        print("5) Usar item")
        print("6) Sair do jogo")
        opc = input("Escolha (1-6): ").strip()
        if opc == '1':
            encontro_aleatorio()
        elif opc == '2':
            heroi.vida += 20
            print(f"Você descansou e recuperou 20 de vida. Vida atual: {heroi.vida}")
        elif opc == '3':
            imprimir_status()
        elif opc == '4':
            print(f"Inventário: {[item.nome for item in heroi.inventario]}")
            escolher = input("Digite o nome do item para equipar (ou enter para voltar): ")
            if escolher:
                encontrados = [i for i in heroi.inventario if i.nome.lower() == escolher.lower()]
                if encontrados:
                    heroi.equipar_item(encontrados[0])
                else:
                    print("Item não encontrado no inventário.")
        elif opc == '5':
            nome_item = input("Nome do item para usar: ")
            usar_item(nome_item)
        elif opc == '6':
            print("Saindo do jogo. Até a próxima aventura!")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    run_game()
