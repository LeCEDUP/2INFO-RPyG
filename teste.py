from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro


# Criando personagens
heroi = Heroi("helen", 100, 15, 5)
goblin = Monstro("julia", 30, 8, 2, "Pequeno")
dragao = Monstro("carol", 50, 30, 10, "medio")

# Criando itens
esmalte = Arma("Esmalte", "cor vermelha.", 10)
acetona = Armadura("acetona", "Um escudo rdo esmalte.", 5)
pocao_vida = Item("Poção de Vida", "Restaura do esmalte")

print("--- Início da Aventura ---") 

# Herói encontra um item
heroi.inventario.append(esmalte)
heroi.inventario.append(acetona)
heroi.inventerio.append(pocao_vida)
print(f"{heroi.nome} encontrou uma {esmalte.nome}, um {acetona.nome} e uma {pocao_vida.nome}.")

# Herói equipa itens
heroi.equipar_item(esmalte)
heroi.equipar_item(acetona)

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

print("\n--- Fim da Aventura ---")