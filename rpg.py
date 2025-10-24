from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

# --- Criação dos Personagens ---
heroi = Heroi("Luna, a Guardiã", 120, 18, 7)
orc = Monstro("Orc das Montanhas", 60, 10, 4, "Médio")
feiticeiro = Monstro("Feiticeiro Sombrio", 100, 15, 5, "Grande")
dragao = Monstro("Dragão Ancião", 250, 35, 12, "Gigante")

# --- Criação dos Itens ---
espada_sagrada = Arma("Espada Sagrada", "Uma lâmina reluzente forjada por anjos.", 12)
armadura_de_ouro = Armadura("Armadura de Ouro", "Protege contra ataques mágicos e físicos.", 8)
pocao_vida = Item("Poção de Vida", "Restaura 40 pontos de vida.")

print("--- 🌟 Início da Aventura de Luna ---")

# Herói encontra os itens
heroi.inventario.append(espada_sagrada)
heroi.inventario.append(armadura_de_ouro)
heroi.inventario.append(pocao_vida)
print(f"{heroi.nome} encontrou uma {espada_sagrada.nome}, um {armadura_de_ouro.nome} e uma {pocao_vida.nome}.")

# Herói equipa os itens
heroi.equipar_item(espada_sagrada)
heroi.equipar_item(armadura_de_ouro)

# --- Primeira Batalha ---
print("\n⚔️  Batalha contra o Orc das Montanhas!")
while heroi.esta_vivo() and orc.esta_vivo():
    heroi.atacar(orc)
    if orc.esta_vivo():
        orc.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} derrotou o {orc.nome}!")
    heroi.ganhar_experiencia(50)

# --- Segunda Batalha ---
print("\n🔥  Encontro com o Feiticeiro Sombrio!")
while heroi.esta_vivo() and feiticeiro.esta_vivo():
    heroi.atacar(feiticeiro)
    if feiticeiro.esta_vivo():
        feiticeiro.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} venceu o {feiticeiro.nome} e sente-se mais forte!")
    heroi.ganhar_experiencia(100)

# --- Herói usa poção ---
print("\n💧  Luna usa uma poção para se curar.")
if pocao_vida in heroi.inventario:
    heroi.vida += 40
    heroi.inventario.remove(pocao_vida)
    print(f"{heroi.nome} usou {pocao_vida.nome}. Vida atual: {heroi.vida}")

# --- Batalha Final ---
print("\n🐲  Batalha Final contra o Dragão Ancião!")
while heroi.esta_vivo() and dragao.esta_vivo():
    heroi.atacar(dragao)
    if dragao.esta_vivo():
        dragao.atacar(heroi)

if heroi.esta_vivo():
    print(f"\n🏆  Parabéns, {heroi.nome}! Você derrotou o {dragao.nome} e trouxe paz ao reino!")
    heroi.ganhar_experiencia(300)
else:
    print(f"\n💀  {heroi.nome} foi derrotada pelo {dragao.nome}... O reino sucumbiu às chamas.")

print("\n--- 🌙 Fim da Aventura ---")
