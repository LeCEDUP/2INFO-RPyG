from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro


personagens = [
    Heroi("Bella", 100, 15, 5),
    Heroi("Luna", 80, 20, 3),
    Heroi("Clara", 120, 10, 8)
]


inimigos = [
    Monstro("Bactéria Malvada", 40, 10, 3, "Microrganismo"),
    Monstro("Espinho de Cactus", 150, 25, 8, "Planta Perigosa")
]


poderes = [
    Arma("Batom Poderoso", "Ataque de batom que causa muito dano", 12),
    Arma("Sombra Explosiva", "Sombra que explode e atinge o inimigo", 15),
]

armaduras = [
    Armadura("Creme Hidratante", "Reduz dano recebido", 5),
    Armadura("Base Mágica", "Protege a pele do ataque inimigo", 8)
]

itens = [
    Item("Máscara Facial", "Restaura 30 de vida"),
    Item("Gloss Energizante", "Restaura 20 de vida")
]