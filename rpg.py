from itens.arma import Arma
from itens.armadura import Armadura
from itens.pocao import Pocao
from personagens.heroi import Heroi
from personagens.monstro import Monstro

nome = input("Digite o nome do seu héroi: ")
heroi = Heroi(nome, 100, 35, 20)
goblin = Monstro("Goblin", 30, 8, 2, "Pequeno")
esqueleto = Monstro("Esqueleto", 15, 10, 0, "Pequeno")
mega_esqueleto = Monstro("Mega Esqueleto", 40, 25, 20, "Médio")
dragao = Monstro("Dragão", 200, 30, 10, "Grande")

espada = Arma("Espada Longa", "Uma espada afiada.", 10)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)
arco = Arma("Arco Longo", "Um arco inka", 20)
pocao_vida = Pocao("Poção de Vida", "Restaura 30 de vida.")
pocao_dano = Pocao("Poção de Dano", "Aumenta 20 de dano.")

print("--- Início da Aventura ---")
print("Você é um héroi que foi invocado em outro mundo por uma deusa. No início da sua aventura, você encontra itens!")
print("Você apenas pode levar a espada e o escudo ou então apenas o arco longo, qual você deseja?")
escolha = input("Digite 'A' para a primeira escolha e 'B' para a segunda escolha: ").upper()
if escolha == "A":
    heroi.inventario.append(espada)
    heroi.inventario.append(escudo)
    heroi.equipar_item(espada)
    heroi.equipar_item(escudo)
elif escolha == "B":
    heroi.inventario.append(arco)
    heroi.equipar_item(arco)
else:
    print("Você somente tem a opção A e B!!")

escolha2 = input("Novamente, você encontra outros dois itens, duas poções, mas você pode escolher apenas uma, deseja a de vida (A) ou a de dano (B): ").upper()
if escolha2 == "A":
    heroi.inventario.append(pocao_vida)
    heroi.equipar_item(pocao_vida)
elif escolha2 == "B":
    heroi.inventario.append(pocao_dano)
    heroi.equipar_item(pocao_dano)
else:
    print("Você somente tem a opção A e B")

print("Finalmente, você encontra seu primeiro inimigo, um goblin! ele avança contra você a fim de porradaria")

print("--- Batalha contra o Goblin ---")
while heroi.esta_vivo() and goblin.esta_vivo():
    heroi.atacar(goblin)
    if goblin.esta_vivo():
        goblin.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} derrotou o {goblin.nome}!")
    heroi.ganhar_experiencia(50)
    print(f"Vida de {heroi.nome}: {heroi.vida}")
    print(f"Inventário de {heroi.nome}: {[item.nome for item in heroi.inventario]}")

if pocao_dano or pocao_vida in heroi.inventario:
    escolha3 = input("Após uma veroz batalha contra o goblin, você sente suas forças aumentarem, deseja utilizar sua poção?(S/N): ")
    if escolha3 == "S": 
        if pocao_vida in heroi.inventario:
            heroi.vida += 30
            heroi.inventario.remove(pocao_vida)
            print(f"{heroi.nome} usou {pocao_vida.nome}. Vida atual: {heroi.vida}")
        elif pocao_dano in heroi.inventario:
            heroi.ataque += 20
            heroi.inventario.remove(pocao_dano)
            print(f"{heroi.nome} usou {pocao_dano.nome} Dano Atual: {heroi.ataque}")
        else: 
            print("Héroi não possui poção!")
    elif escolha3 == "N":
        print(f"Você decide ir do jeito que está para a última batalha! Vida Atual: {heroi.vida} / Dano Atual: {heroi.ataque}")
    else: 
        print("Digite S de sim ou N de não!")