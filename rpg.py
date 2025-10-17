from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

def introducao():
    print("Bem-vindo ao mundo de Hogwarts!")
    print("Você é o Harry Potter em uma missão para derrotar monstros e salvar o reino.")
    print("Prepare-se para a aventura!")

# Criando personagens
HarryPotter = Heroi("Harry Potter", 100, 15, 5)
goblin = Monstro("", 30, 8, 2, "Pequeno")
dragao = Monstro("Dragão", 200, 30, 10, "Grande")

# Criando itens
espada = Arma("Varinha", "Uma espada afiada.", 10)
escudo = Armadura("Protego", "Um escudo resistente.", 5)
pocao_vida = Item("Poção de Vida", "Restaura 30 de vida.")

print("--- Início da Aventura ---")

# Herói encontra um item
HarryPotter.inventario.append(espada)
HarryPotter.inventario.append(escudo)
HarryPotter.inventario.append(pocao_vida)
print(f"{HarryPotter.nome} encontrou uma {espada.nome}, um {escudo.nome} e uma {pocao_vida.nome}.")

# Herói equipa itens
HarryPotter.equipar_item(espada)
HarryPotter.equipar_item(escudo)

print("\n--- Batalha contra o Goblin ---")
while HarryPotter.esta_vivo() and goblin.esta_vivo():
    HarryPotter.atacar(goblin)
    if goblin.esta_vivo():
        goblin.atacar(HarryPotter)


if HarryPotter.esta_vivo():
    print(f"{HarryPotter.nome} derrotou o {goblin.nome}!")
    HarryPotter.ganhar_experiencia(50)
    print(f"Vida de {HarryPotter.nome}: {HarryPotter.vida}")
    print(f"Inventário de {HarryPotter.nome}: {[item.nome for item in HarryPotter.inventario]}")

print("\n--- Herói usa poção ---")
if pocao_vida in HarryPotter.inventario:
    HarryPotter.vida += 30
    HarryPotter.inventario.remove(pocao_vida)
    print(f"{HarryPotter.nome} usou {pocao_vida.nome}. Vida atual: {HarryPotter.vida}")

print("\n--- Batalha contra o Dragão (Desafio Final) ---")
while HarryPotter.esta_vivo() and dragao.esta_vivo():
    HarryPotter.atacar(dragao)
    if dragao.esta_vivo():
        dragao.atacar(HarryPotter)

if HarryPotter.esta_vivo():
    print(f"\nParabéns, {HarryPotter.nome}! Você derrotou o {dragao.nome} e salvou o reino!")
    HarryPotter.ganhar_experiencia(200)
else:
    print(f"\n{HarryPotter.nome} foi derrotado pelo {dragao.nome}. Fim de jogo.")

print("\n--- Fim da Aventura ---")