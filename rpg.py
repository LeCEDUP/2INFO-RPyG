# Desenvolva o seu jogo aqui
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro


# Criando personagens
heroi = Heroi("Scarlat, a Guardiã das Runas", 120, 18, 6)
lobo_sombrio = Monstro("Lobo Sombrio", 40, 10, 3, "Médio")
feiticeiro = Monstro("Feiticeiro das Sombras", 80, 15, 4, "Grande")
senhor_abismo = Monstro("Senhor do Abismo", 250, 28, 12, "Chefe Final")

# Criando itens
cajado_runas = Arma("Cajado das Runas", "Um cajado antigo que brilha com energia mágica.", 12)
manto_lunar = Armadura("Manto Lunar", "Um manto que protege contra ataques sombrios.", 7)
pocao_luz = Item("Poção de Luz", "Restaura 40 de vida.")

print("=== A LENDA DE ELDORIA ===\n")
print("As ruínas de Eldoria foram esquecidas há séculos, até que uma força sombria começou a emergir.")
print("Scarlat, a Guardiã das Runas, parte em uma jornada para selar o mal e restaurar o equilíbrio do reino.\n")

print("--- Início da Jornada ---")

# Lina encontra itens
heroi.inventario.append(cajado_runas)
heroi.inventario.append(manto_lunar)
heroi.inventario.append(pocao_luz)
print(f"{heroi.nome} encontrou um {cajado_runas.nome}, um {manto_lunar.nome} e uma {pocao_luz.nome}.")

# Lina equipa itens
heroi.equipar_item(cajado_runas)
heroi.equipar_item(manto_lunar)

print("\n--- Batalha nas Florestas Antigas (Lobo Sombrio) ---")
while heroi.esta_vivo() and lobo_sombrio.esta_vivo():
    heroi.atacar(lobo_sombrio)
    if lobo_sombrio.esta_vivo():
        lobo_sombrio.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} derrotou o {lobo_sombrio.nome}!")
    heroi.ganhar_experiencia(50)
    print(f"Vida de {heroi.nome}: {heroi.vida}")
    print(f"Inventário: {[item.nome for item in heroi.inventario]}")

print("\n--- Encontro nas Catacumbas (Feiticeiro das Sombras) ---")
while heroi.esta_vivo() and feiticeiro.esta_vivo():
    heroi.atacar(feiticeiro)
    if feiticeiro.esta_vivo():
        feiticeiro.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} venceu o {feiticeiro.nome} e sente o poder crescer dentro de si!")
    heroi.ganhar_experiencia(100)
else:
    print(f"{heroi.nome} foi derrotada nas catacumbas. O mal prevalece...")
    exit()

print("\n--- Scarlat usa a Poção de Luz antes da batalha final ---")
if pocao_luz in heroi.inventario:
    heroi.vida += 60
    heroi.inventario.remove(pocao_luz)
    print(f"{heroi.nome} usou {pocao_luz.nome}. Vida atual: {heroi.vida}")

print("\n--- Batalha Final nas Ruínas de Eldoria ---")
while heroi.esta_vivo() and senhor_abismo.esta_vivo():
    heroi.atacar(senhor_abismo)
    if senhor_abismo.esta_vivo():
        senhor_abismo.atacar(heroi)

if heroi.esta_vivo():
    print(f"\nCom um último golpe de luz, {heroi.nome} derrota o {senhor_abismo.nome}!")
    print("As trevas recuam, e o selo das Runas se restaura.")
    heroi.ganhar_experiencia(80)
    print("\nO reino está salvo, e o nome de Lina ecoará nas lendas de Eldoria.")
else:
    print(f"\n{heroi.nome} caiu diante do {senhor_abismo.nome}...")
    print("As trevas engolem Eldoria, e a esperança desaparece.")

print("\n--- Fim da Jornada ---")
