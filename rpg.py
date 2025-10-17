from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

def introdução():
    print("Bem-vindo ao mundo mágico de Harry Potter!")
    print("Você é Harry Potter, um jovem bruxo destinado a enfrentar grandes desafios.")
    print("Sua missão é derrotar os inimigos que ameaçam o mundo bruxo e salvar Hogwarts.")
    print("Prepare-se para uma aventura épica cheia de magia, batalhas e descobertas!")

# Criando personagens
HarryPotter = Heroi("Harry Potter", 100, 30, 15)
Dementadores = Monstro("Dementadores", 80, 5, 5, "Grande")
Voldemort = Monstro("Voldemort", 200, 45, 10, "Pequeno")


# Criando itens
espada = Arma("Varinha", "Uma feita para cada bruxo.", 10)
escudo = Armadura("Protego", "Um feitiço de escudo.", 5)
pocao_vida = Item("Poção Wiggenweld", "Restaura 30 de vida.")

print("--- Início da Guerra ---")

# Herói encontra um item
HarryPotter.inventario.append(espada)
HarryPotter.inventario.append(escudo)
HarryPotter.inventario.append(pocao_vida)
print(f"{HarryPotter.nome} encontrou uma {espada.nome}, aprendeu a fazer {escudo.nome} e uma {pocao_vida.nome}.")

# Herói equipa itens
HarryPotter.equipar_item(espada)
HarryPotter.equipar_item(escudo)

print("\n--- Batalha contra o Dementadores ---")
while HarryPotter.esta_vivo() and Dementadores.esta_vivo():
    HarryPotter.atacar(Dementadores)
    if Dementadores.esta_vivo():
        Dementadores.atacar(HarryPotter)


if HarryPotter.esta_vivo():
    print(f"{HarryPotter.nome} derrotou o {Dementadores.nome}!")
    HarryPotter.ganhar_experiencia(50)
    print(f"Vida de {HarryPotter.nome}: {HarryPotter.vida}")
    print(f"Inventário de {HarryPotter.nome}: {[item.nome for item in HarryPotter.inventario]}")

print("\n--- Harry Potter usa poção ---")
if pocao_vida in HarryPotter.inventario:
    HarryPotter.vida += 30
    HarryPotter.inventario.remove(pocao_vida)
    print(f"{HarryPotter.nome} usou {pocao_vida.nome}. Vida atual: {HarryPotter.vida}")

print("\n--- Batalha contra o Voldemort (Desafio Final) ---")
while HarryPotter.esta_vivo() and Voldemort .esta_vivo():
    HarryPotter.atacar(Voldemort)
    if Voldemort .esta_vivo():
        Voldemort .atacar(HarryPotter)

if HarryPotter.esta_vivo():
    print(f"\nParabéns, {HarryPotter.nome}! Você derrotou o {Voldemort.nome} e salvou o Hogwarts!")
    HarryPotter.ganhar_experiencia(200)
else:
    print(f"\n{HarryPotter.nome} foi derrotado pelo {Voldemort.nome}. Fim,Voldemort ganhou a guerra.")

print("\n--- Fim da guerra ---")