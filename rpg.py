from itens.item import Item
from itens.arma import Varinha
from itens.armadura import Armadura
from personagens.bruxo import Bruxo
from personagens.monstro import Vilao


# Criando personagens
harry = Bruxo("Harry Potter", 100, 30, 10)
hermione = Bruxo("Hermione", 100, 25, 10)
ron = Bruxo("Ron", 100, 25, 5)
voldemort = Vilao("Voldemort", 100, 50, 15, "Feiticeiro")
basilisco = Vilao( "Basilisco", 110, 40, 10, "Serpente Gigante")
hipogrifo = Vilao("Hipogrifo", 100, 35, 15, "Criatura Mágica")
# Criando itens
varinha.harry = Varinha("Varinha do harry","A poderosa varinha de harry", 10)
varinha.hermione = Varinha ("Varinha da hermione", "A varinha da inteligente hermione", 10)
varinha.ron = Varinha ("Varinha do ron", "A leal varinha de ron", 10)
varinha.voldemort = Varinha ("Varinha das varinhas", "A varinha mais poderosa do mundo bruxo" 15)
escudo = Armadura("Escudo de pele de dragão", "Um escudo poderoso e resistente", 10)
pocao_vida = Item("Poção de Vida", "Restaura 30 de vida.")

print("--- Início da Aventura ---")

# Herói encontra um item
bruxo.inventario.append(varinha)
bruxo.inventario.append(escudo)
bruxo.inventario.append(pocao_vida)
print(f"{bruxo.nome} encontrou uma {varinha.nome}, um {escudo.nome} e uma {pocao_vida.nome}.")

# Herói equipa itens
bruxo.equipar_item(varinha)
bruxo.equipar_item(escudo)

print("\n--- Batalha contra o Basilisco ---")
while bruxo.esta_vivo() and basilisco.esta_vivo():
    bruxo.atacar(basilisco)
    if basilisco.esta_vivo():
        basilisco.atacar(bruxo)

if bruxo.esta_vivo():
    print(f"{bruxo.nome} derrotou o {basilisco.nome}!")
    bruxo.ganhar_experiencia(50)
    print(f"Vida de {bruxo.nome}: {bruxo.vida}")
    print(f"Inventário de {bruxo.nome}: {[item.nome for item in bruxo.inventario]}")

    print("\n--- Bruxo usa poção ---")
if pocao_vida in bruxo.inventario:
    bruxo.vida += 30
    bruxo.inventario.remove(pocao_vida)
    print(f"{bruxo.nome} usou {pocao_vida.nome}. Vida atual: {bruxo.vida}")

    print("\n--- Batalha contra o Hipogrifo ---")
while bruxo.esta_vivo() and hipogrifo.esta_vivo():
    bruxo.atacar(hipogrifo)
    if hipogrifo.esta_vivo():
        hipogrifo.atacar(bruxo)

if bruxo.esta_vivo():
    print(f"{bruxo.nome} derrotou o {hipogrifo.nome}!")
    bruxo.ganhar_experiencia(50)
    print(f"Vida de {bruxo.nome}: {bruxo.vida}")
    print(f"Inventário de {bruxo.nome}: {[item.nome for item in bruxo.inventario]}")

print("\n--- Bruxo usa poção ---")
if pocao_vida in bruxo.inventario:
    bruxo.vida += 30
    bruxo.inventario.remove(pocao_vida)
    print(f"{bruxo.nome} usou {pocao_vida.nome}. Vida atual: {bruxo.vida}")

print("\n--- Batalha contra o Voldemort (Desafio Final) ---")
while heroi.esta_vivo() and voldemort.esta_vivo():
    bruxo.atacar(voldemort)
    if voldemort.esta_vivo():
        voldemort.atacar(bruxo)

if heroi.esta_vivo():
    print(f"\nParabéns, {bruxo.nome}! Você derrotou o {voldemort.nome} e salvou o mundo bruxo!")
    bruxo.ganhar_experiencia(200)
else:
    print(f"\n{bruxo.nome} foi derrotado pelo {bruxo.nome}. Fim de jogo.")
