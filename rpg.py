from itens.item import Item
from itens.arma import Varinha
from itens.armadura import Armadura
from personagens.bruxo import Bruxo
from personagens.monstro import Vilao


# Criando personagens
harry = Bruxo("Harry Potter", 100, 30, 10)
hermione = Bruxo("Hermione", 100, 25, 10)
ron = Bruxo("Ron", 100, 25, 5)
voldemort = Vilao("Voldemort", 100, 50, 10, "Feiticeiro")

# Criando itens
varinha.harry = Varinha("Varinha do harry","A poderosa varinha de harry", 10)
varinha.hermione = Varinha ("Varinha da hermione", "A varinha da inteliente hermione", 10)
varinha.ron = Varinha ("Varinha do ron", "A leal varinha de ron", 10)
varinha.voldemort = Varinha ("Varinha das varinhas", "A varinha mais poderosa do mundo bruxo" 15)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)
pocao_vida = Item("Poção de Vida", "Restaura 30 de vida.")

print("--- Início da Aventura ---")

# Herói encontra um item
bruxo.inventario.append(espada)
bruxo.inventario.append(escudo)
bruxo.inventario.append(pocao_vida)
print(f"{bruxo.nome} encontrou uma {espada.nome}, um {escudo.nome} e uma {pocao_vida.nome}.")

# Herói equipa itens
heroi.equipar_item(espada)
heroi.equipar_item(escudo)

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

print("\n--- Herói usa poção ---")
if pocao_vida in heroi.inventario:
    heroi.vida += 30
    heroi.inventario.remove(pocao_vida)
    print(f"{heroi.nome} usou {pocao_vida.nome}. Vida atual: {heroi.vida}")

print("\n--- Batalha contra o Dragão (Desafio Final) ---")
while heroi.esta_vivo() and dragao.esta_vivo():
    heroi.atacar(dragao)
    if dragao.esta_vivo():
        dragao.atacar(heroi)

if heroi.esta_vivo():
    print(f"\nParabéns, {heroi.nome}! Você derrotou o {dragao.nome} e salvou o reino!")
    heroi.ganhar_experiencia(200)
else:
    print(f"\n{heroi.nome} foi derrotado pelo {dragao.nome}. Fim de jogo.")
