""""
Facehugger só implanta se o tripulante for pego
Se infectado, inicia-se o ciclo de gestação(Chestburster).
Xenomorfo pode ser morto nada impossivel porem é melhor não tentar
"""

# Desenvolva o seu jogo aqui
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import time

#------Utilidades------
def pausa(texto="". delay=1.4):
    """"Pausa curta para ritmo narrativo"""
    print(texto)
    time.sleep(delay)

def escolha(prompt, opcoes):
    """Apresenta opções e retorna escolha válida (string index começando em 1)"""
    while True:
        resp = input(prompt),strip()
        if resp in opcoes:
            return resp
        print("Escolha inválida. Tente novamente")

def status(ripley):
    inv = [item.nome for item in ripley.inventario]
    print(f"\n[STATUS] Vida: {ripley.vida}| inventário: {inv}")

#------Configurações do jogo------
#Personagem principal
tripulante = Heroi("Ripley", 100, 15, 5)

#Monstros
face_hugger = Monstro("Face Hugger", 30, 8, 2, "Pequeno")
alien = Monstro("Xenomorfo",550, 100, 20, "Grande")

#itens
pistola = Arma("pistola", "Um .38 revolver com maximo 8 tiros. +5 de ataque", 5)
lanterna = Item("lanterna", "Ajuda a enxergar em áreas escuros, mas atrai criaturas")
motion_tracker = Item("Motion_tracker", "dectecta tudo que se move perto.")
medkit = Item("Medkit", "Restaura 50 de vida.")
Lança_chamas = Arma("Lança-Chamas", "Pouco combustível; afasta o Xenomorfo por pouco tempo.", 0)
roupa_espacial = Armadura("Roupa Espacial", "Protege contra danos e a vácuo")

#Infecção
infectado = False
gestacao_turns_remaining = None
Gestacao_min = 3
Gestacao_max = 8

print("--- Início da Aventura ---")
print(f"{tripulante.nome} acorda sozinha na estação Sevastopol. Algo se move nas sombras...")

#encontro de itens
tripulante.inventario.append(pistola)
tripulante.inventario.append(motion_tracker)
tripulante.inventario.append(medkit)
print(f"{tripulante.nome} encontrou uma {pistola.nome}, um {motion_tracker.nome} e uma {medkit.nome}.")

# tripulante equipa itens
tripulante.equipar_item(pistola)
tripulante.equipar_item(motion_tracker)

print("\n--- Batalha contra o Face Hugger ---")
while tripulante.esta_vivo() and face_hugger.esta_vivo():
    tripulante.atacar(face_hugger)
    if tripulante.esta_vivo():
        tripulante.atacar(tripulante)