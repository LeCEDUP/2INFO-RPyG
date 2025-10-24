from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro


personagens = [
    Heroi("Bella", 100, 15, 5),
    Heroi("Luna", 80, 20, 3),
    Heroi("Clara", 120, 10, 8)
]


inimigos = [
    Monstro("Bactéria Malvada", 40, 10, 3, "Microrganismo"),
    Monstro("Espinho de Cactus", 150, 25, 8, "Planta Perigosa")
]


poderes = [
    Arma("Batom Poderoso", "Ataque de batom que causa muito dano", 12),
    Arma("Sombra Explosiva", "Sombra que explode e atinge o inimigo", 15),
]

armaduras = [
    Armadura("Creme Hidratante", "Reduz dano recebido", 5),
    Armadura("Base Mágica", "Protege a pele do ataque inimigo", 8)
]

itens = [
    Item("Máscara Facial", "Restaura 30 de vida"),
    Item("Gloss Energizante", "Restaura 20 de vida")
]

print(" Bem-vindo ao RPG Cosmético Interativo ---")

print("\nEscolha seu personagem:")
for i, p in enumerate(personagens):
    print(f"{i+1}. {p.nome} (Vida: {p.vida}, Ataque: {p.ataque}, Defesa: {p.defesa})")

escolha = int(input("Digite o número do personagem que deseja jogar: ")) - 1
heroi = personagens[escolha]


heroi.inventario.append(poderes[0])
heroi.inventario.append(armaduras[0])
heroi.inventario.append(itens[0])
heroi.equipar_item(poderes[0])
heroi.equipar_item(armaduras[0])

print(f"\nVocê escolheu {heroi.nome}!\n")

for inimigo in inimigos:
    print(f"Batalha contra {inimigo.nome} ---")
    while heroi.esta_vivo() and inimigo.esta_vivo():
       
        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Usar item")
        acao = input("Digite 1 ou 2: ")

        if acao == "1":
           
            armas_disponiveis = [item for item in heroi.inventario if isinstance(item, Arma)]
            print("\nEscolha seu poder:")
            for i, p in enumerate(armas_disponiveis):
                print(f"{i+1}. {p.nome} ({p.descricao}, Dano: {heroi.ataque})")
            poder_escolhido = int(input("Digite o número do poder: ")) - 1

            
            if 0 <= poder_escolhido < len(armas_disponiveis):
                heroi.equipar_item(armas_disponiveis[poder_escolhido])
                heroi.atacar(inimigo)
            else:
                print("Escolha inválida! Você perdeu o turno.")

        elif acao == "2":
            itens_disponiveis = [item for item in heroi.inventario if isinstance(item, Item)]
            if not itens_disponiveis:
                print("Você não tem itens para usar!")
            else:
                print("\nEscolha um item para usar:")
                for i, item in enumerate(itens_disponiveis):
                    print(f"{i+1}. {item.nome} ({item.descricao})")
                item_escolhido = int(input("Digite o número do item: ")) - 1
                if 0 <= item_escolhido < len(itens_disponiveis):
                    item = itens_disponiveis[item_escolhido]
                    if "30" in item.descricao:
                        heroi.vida += 30
                    elif "20" in item.descricao:
                        heroi.vida += 20
                    heroi.inventario.remove(item)
                    print(f"{heroi.nome} usou {item.nome}. Vida atual: {heroi.vida}")
                else:
                    print("Escolha inválida! Você perdeu o turno.")
