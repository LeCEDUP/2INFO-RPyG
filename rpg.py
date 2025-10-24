# Desenvolva o seu jogo aqui
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro


# Criando personagens
heroi = Heroi("Scarlat, a Guardiã das Runas", 230, 18, 6)
dragão = Monstro("Dragão", 90, 10, 3, "Médio")
mago = Monstro("Mago", 130, 15, 4, "Grande")
senhor_gelado = Monstro("Senhor gelado", 450, 28, 12, "Chefe Final")

# Criando itens
espada_runas = Arma("Espada das Runas", "Uma espada antiga que brilha com energia mágica.", 12)
capa = Armadura("Capa", "Uma capa que protege contra ataques sombrios.", 7)
furia = Item("Furia", "Uma poção que restaura 60 de vida.")

print("=== A LENDA DE ELDORIA ===\n")
print("As ruínas de Eldoria foram esquecidas há séculos, até que uma força sombria começou a emergir.")
print("Scarlat, a Guardiã das Runas, parte em uma jornada para selar o mal e restaurar o equilíbrio do reino.\n")

print("--- Início da Jornada ---")

# Lina encontra itens
heroi.inventario.append(espada_runas)
heroi.inventario.append(capa)
heroi.inventario.append(furia)
print(f"{heroi.nome} encontrou um {espada_runas.nome}, um {capa.nome} e uma {furia.nome}.")

# Lina equipa itens
heroi.equipar_item(espada_runas)
heroi.equipar_item(capa)

print("\n--- Batalha nas Florestas Antigas (Dragão) ---")
while heroi.esta_vivo() and dragão.esta_vivo():
    heroi.atacar(dragão)
    if dragão.esta_vivo():
        dragão.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} derrotou o {dragão.nome}!")
    heroi.ganhar_experiencia(50)
    print(f"Vida de {heroi.nome}: {heroi.vida}")
    print(f"Inventário: {[item.nome for item in heroi.inventario]}")

print("\n--- Encontro nas Catacumbas (mago) ---")
while heroi.esta_vivo() and mago.esta_vivo():
    heroi.atacar(mago)
    if mago.esta_vivo():
        mago.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} venceu o {mago.nome} e sente o poder crescer dentro de si!")
    heroi.ganhar_experiencia(100)
else:
    print(f"{heroi.nome} foi derrotada nas catacumbas. O mal prevalece...")
    exit()

print("\n--- Scarlat usa a Furia antes da batalha final ---")
if pocao_luz in heroi.inventario:
    heroi.vida += 60
    heroi.inventario.remove(furia)
    print(f"{heroi.nome} usou {furia.nome}. Vida atual: {heroi.vida}")

print("\n--- Batalha Final nas Ruínas de Eldoria ---")
while heroi.esta_vivo() and senhor_gelado.esta_vivo():
    heroi.atacar(senhor_gelado)
    if senhor_gelado.esta_vivo():
        senhor_gelado.atacar(heroi)

if heroi.esta_vivo():
    print(f"\nCom um último golpe de luz, {heroi.nome} derrota o {senhor_gelado.nome}!")
    print("As trevas recuam, e o selo das Runas se restaura.")
    heroi.ganhar_experiencia(100)
    print("\nO reino está salvo, e o nome de Scarlat ecoará nas lendas de Eldoria.")
else:
    print(f"\n{heroi.nome} caiu diante do {senhor_gelado.nome}...")
    print("As trevas engolem Eldoria, e a esperança desaparece.")

print("\n--- Fim da Jornada ---")
