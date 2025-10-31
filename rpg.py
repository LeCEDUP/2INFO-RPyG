from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

Rei_goblin = Monstro("Rei_goblin", 150, 30, 10, "Grande")
heroi = Heroi("Darwin", 100, 15, 5)


espada = Arma("Espada Longa", "Uma espada afiada", 10)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)

print ("---Início da jornada---")

heroi.inventario.append(espada)
heroi.inventario.append(escudo)
print(f"{heroi.nome} encontrou uma {espada.nome}, um {escudo.nome}.")

heroi.equipar_item(espada)
heroi.equipar_item(escudo)

lutas = int(input("Escolha quantas vezes você vai querer lutar contra os goblins menores: "))
luta = 0 
while luta < lutas:
    print("\n--- Batalha contra o Goblin ---")
    goblin = Monstro("Goblin", 30, 8, 2, "Pequeno")
    while heroi.esta_vivo() and goblin.esta_vivo():
        heroi.atacar(goblin)
        if goblin.esta_vivo():
            goblin.atacar(heroi)

    if heroi.esta_vivo():
        print(f"{heroi.nome} derrotou o {goblin.nome}!")
        heroi.ganhar_experiencia(50)
        print(f"Vida de {heroi.nome}: {heroi.vida}")
        print(f"Inventário de {heroi.nome}: {[item.nome for item in heroi.inventario]}")
        luta += 1

print("\n--- Batalha contra o Rei Goblin (Desafio Final) ---")
while heroi.esta_vivo() and Rei_goblin.esta_vivo():
    heroi.atacar(Rei_goblin)
    if Rei_goblin.esta_vivo():
        Rei_goblin.atacar(heroi)

if heroi.esta_vivo():
    print(f"\nParabéns, {heroi.nome}! Você derrotou o {Rei_goblin.nome} e salvou o reino!")
    heroi.ganhar_experiencia(200)
else:
    print(f"\n{heroi.nome} foi derrotado pelo {Rei_goblin.nome}. Fim de jogo.")

print("\n--- Fim da Jornada ---")