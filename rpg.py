from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

nome = input("Digite o nome do seu héroi")
heroi = Heroi(nome, 100, 35, 20)
goblin = Monstro("Goblin", 30, 8, 2, "Pequeno")
esqueleto = Monstro("Esqueleto", 15, 10, 0, "Pequeno")
mega_esqueleto = Monstro("Mega Esqueleto", 40, 25, 20, "Médio")
dragao = Monstro("Dragão", 200, 30, 10, "Grande")

espada = Arma("Espada Longa", "Uma espada afiada.", 10)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)
arco = Arma("Arco Longo", "Um arco inka", 20)
pocao_vida = Item("Poção de Vida", "Restaura 30 de vida.")
pocao_dano = Item("Poção de Dano", "Aumenta 20 de dano.")

print("--- Início da Aventura ---")
print("Você é um héroi que foi invocado em outro mundo por uma deusa. No início da sua aventura, você encontra itens!")
print("Você apenas pode levar a espada e o escudo ou então apenas o arco longo, qual você deseja?")
escolha = input("Digite 'A' para a primeira escolha e 'B' para a segunda escolha.").upper()
if escolha == "A":
    heroi.equipar_item(espada)
    heroi.equipar_item(escudo)
    print("Você equipou a espada e o escudo!")
elif escolha == "B":
    heroi.equipar_item(arco)
    print("Você equipou o arco e flecha!")
else:
    print("Você somente tem a opção A e B!!")