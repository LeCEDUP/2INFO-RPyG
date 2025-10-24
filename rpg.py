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

def batalha(heroi, monstro):
    print(f"\n {heroi.nome} vs {monstro.nome} ")

    while heroi.esta_vivo() and monstro.esta_vivo():
        print("\nO que deseja fazer?")
        print("1 - Atacar")
        print("2 - Usar Poção (+30 de vida)")
        escolha = input("Escolha: ")

        if escolha == "1":
            dano_heroi = random.randint(heroi.ataque - 5, heroi.ataque + 5) - monstro.defesa
            if dano_heroi < 0:
                dano_heroi = 0
            monstro.vida -= dano_heroi
            print(f"{heroi.nome} atacou {monstro.nome} causando {dano_heroi} de dano!")
            if monstro.vida <= 0:
                print(f"{monstro.nome} foi derrotado!")
                break

        elif escolha == "2":
            pocoes = [item for item in heroi.inventario if "Poção" in item.nome]
            if pocoes:
                heroi.vida += 30
                heroi.inventario.remove(pocoes[0])
                print(f"{heroi.nome} usou {pocoes[0].nome}. Vida atual: {heroi.vida}")
            else:
                print("Você não tem poções")

        else:
            print("Opção inválida")
            continue

        if monstro.vida > 0:
            monstro_atacar(monstro, heroi)
            if heroi.vida <= 0:
                print(f"{heroi.nome} foi derrotado!")
                break

def main():
    introducao()

    while True:
        opcao = menu_principal()
        if opcao == "1":
  
            espada = Arma("Varinha", "Uma varinha que é diferente pra cada bruxo.", 10)
            escudo = Armadura("Protego", "Um feitiço que gera escudo resistente.", 5)
            pocao = Item("Poção Wiggenweld", "Restaura 30 de vida.")

            harry = Heroi("Harry Potter", 100, 28, 10)
            dementador = Monstro("Dementador", 75, 25, 5, "Pequeno")
            voldemort = Monstro("Voldemort", 120, 30, 12, "Grande")

            harry.inventario.append(espada)
            harry.inventario.append(escudo)
            harry.inventario.append(pocao)
            harry.equipar_item(espada)
            harry.equipar_item(escudo)
            print(f"{harry.nome} equipou {espada.nome} e {escudo.nome}!")

            print("\n--- PRIMEIRA BATALHA: DEMENTADOR ---")
            batalha(harry, dementador)

            if harry.esta_vivo():
  
                print("\n--- DESAFIO FINAL: VOLDEMORT ---")
                batalha(harry, voldemort)

            if harry.esta_vivo():
                print("Parabéns! Você derrotou todos os inimigos e salvou Hogwarts!")
            else:
                print("Você foi derrotado... ")

        elif opcao == "2":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
