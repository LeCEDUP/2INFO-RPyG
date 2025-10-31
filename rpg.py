from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

Rei_goblin = Monstro("Rei_goblin", 150, 30, 10, "Grande")
goblin = Monstro("Goblin", 30, 8, 2 "Pequeno")
Heroi = Heroi("Darwin", 100, 15, 5)


espada = Arma("Espada Longa", "Uma espada afiada", 10)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)

print ("---Início da jornada---")

heroi.inventario.append(espada)
heroi.inventario.append(escudo)
print(f"{heroi.nome} encontrou uma {espada.nome}, um {escudo.nome}.")

heroi.equipar_item(espada)
heroi.equipar_item(escudo)

lutas = input("Escolha quantas vezes você vai querer lutar contra os goblins menores")
luta = 0 
while contador < quantidade:
    print("\n--- Batalha contra o Goblin ---")
    while heroi.esta_vivo() and goblin.esta_vivo():
        heroi.atacar(goblin)
        if goblin.esta_vivo():
            goblin.atacar(heroi)

    if heroi.esta_vivo():
        print(f"{heroi.nome} derrotou o {goblin.nome}!")
        heroi.ganhar_experiencia(50)
        print(f"Vida de {heroi.nome}: {heroi.vida}")
        print(f"Inventário de {heroi.nome}: {[item.nome for item in heroi.inventario]}")
        contador += 1

