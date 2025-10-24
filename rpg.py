from itens.item import Item
from itens.arma import Varinha
from itens.armadura import Armadura
from personagens.heroi import Bruxo
from personagens.monstro import Vilao


# Criando personagens
harry = Bruxo("Harry Potter", 100, 50, 10)
hermione = Bruxo("Hermione", 100, 45, 20)
ron = Bruxo("Ron", 100, 40, 10)
voldemort = Vilao("Voldemort", 100, 50, 15, "Feiticeiro")
basilisco = Vilao( "Basilisco", 110, 40, 10, "Serpente Gigante")
hipogrifo = Vilao("Hipogrifo", 100, 35, 15, "Criatura Mágica")
# Criando itens
varinha_harry = Varinha("Varinha do harry","A poderosa varinha de harry", 10)
varinha_hermione = Varinha("Varinha da hermione", "A varinha da inteligente hermione", 10)
varinha_ron = Varinha("Varinha do ron", "A leal varinha de ron", 10)
varinha_voldemort = Varinha("Varinha das varinhas", "A poderosa varinha das varinhas", 15)
escudo = Armadura("Escudo de pele de dragão", "Um escudo poderoso e resistente", 10)
pocao_vida = Item("Poção de Vida", "Restaura 30 de vida.")

print("--- Início da Aventura ---")

# Herói encontra um item
harry.inventario.append(varinha_harry)
harry.inventario.append(escudo)
harry.inventario.append(pocao_vida)
print(f"{harry.nome} encontrou uma {varinha_harry.nome}, um {escudo.nome} e uma {pocao_vida.nome}.")

# Herói equipa itens
harry.equipar_item(varinha_harry)
harry.equipar_item(escudo)

print("\n--- Batalha contra o Basilisco ---")
while harry.esta_vivo() and basilisco.esta_vivo():
    harry.atacar(basilisco)
    if basilisco.esta_vivo():
        basilisco.atacar(harry)

if harry.esta_vivo():
    print(f"{harry.nome} derrotou o {basilisco.nome}!")
    harry.ganhar_experiencia(50)
    harry.inventario.append(pocao_vida)
    print("Ao derrotar o Basilisco, Harry encontrou uma Poção de Vida!")
    print(f"Vida de {harry.nome}: {harry.vida}")
    print(f"Inventário de {harry.nome}: {[item.nome for item in harry.inventario]}")

    print("\n--- harry usa poção ---")
if pocao_vida in harry.inventario:
    harry.vida += 30
    harry.inventario.remove(pocao_vida)
    print(f"{harry.nome} usou {pocao_vida.nome}. Vida atual: {harry.vida}")

    print("\n--- Batalha contra o Hipogrifo ---")
while harry.esta_vivo() and hipogrifo.esta_vivo():
    harry.atacar(hipogrifo)
    if hipogrifo.esta_vivo():
        hipogrifo.atacar(harry)

if harry.esta_vivo():
    print(f"{harry.nome} derrotou o {hipogrifo.nome}!")
    harry.ganhar_experiencia(50)
    print(f"Vida de {harry.nome}: {harry.vida}")
    print(f"Inventário de {harry.nome}: {[item.nome for item in harry.inventario]}")

print("\n--- harry usa poção ---")
if pocao_vida in harry.inventario:
    harry.vida += 30
    harry.inventario.remove(pocao_vida)
    print(f"{harry.nome} usou {pocao_vida.nome}. Vida atual: {harry.vida}")

print("\n--- Batalha contra o Voldemort (Desafio Final) ---")
while harry.esta_vivo() and voldemort.esta_vivo():
    harry.atacar(voldemort)
    if voldemort.esta_vivo():
        voldemort.atacar(harry)

if harry.esta_vivo():
    print(f"\nParabéns, {harry.nome}! Você derrotou o {voldemort.nome} e salvou o mundo bruxo!")
    harry.ganhar_experiencia(200)
else:
    print(f"\n{harry.nome} foi derrotado pelo {voldemort.nome}. Fim de jogo.")
