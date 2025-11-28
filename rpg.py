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

""""
Facehugger só implanta se o tripulante for pego
Se infectado, inicia-se o ciclo de gestação(Chestburster).
Xenomorfo pode ser morto nada impossivel porem é melhor não tentar
"""
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

#personagens
def status(ripley):
    inv = [item.nome for item in ripley.inventario]
    print(f"\n[STATUS] Vida: {ripley.vida}| inventário: {inv}")

#--------Funções de jogo---------
def status(jogador):
    inv = [item.nome for item in jogador.inventario]
    print(f"\n[STATUS] Vida: {jogador.vida} | Inventário: {inv}")


def explorar(jogador):
    """Exploração com chance de encontrar itens ou o Facehugger"""
    global infectado, gestacao_turns_remaining
    pausa("\nVocê caminha pelos corredores escuros da Sevastopol...")
    evento = random.choice(["nada", "item", "facehugger"])

    if evento == "nada":
        pausa("Tudo silencioso... por enquanto.")
    elif evento == "item":
        item_encontrado = random.choice([lanterna, motion_tracker, medkit])
        pausa(f"Você encontrou um(a) {item_encontrado.nome}!")
        jogador.inventario.append(item_encontrado)
    elif evento == "facehugger":
        pausa("Você ouve um som agudo e vê algo se movendo rapidamente!")
        acao = escolha("Tentar correr (c) ou lutar (l)? ", ["c", "l"])
        if acao == "c":
            if random.random() < 0.6:
                pausa("Você consegue escapar! O Facehugger some nas sombras.")
            else:
                pausa("O Facehugger salta em seu rosto!")
                infectado = True
                gestacao_turns_remaining = random.randint(Gestacao_min, Gestacao_max)
                pausa("Você sente algo estranho em seu peito...")
        else:
            pausa("Você tenta lutar contra o Facehugger...")
            if random.random() < 0.4:
                pausa("Você o afasta com dificuldade e sobrevive.")
            else:
                pausa("Ele gruda em seu rosto!")
                infectado = True
                gestacao_turns_remaining = random.randint(Gestacao_min, Gestacao_max)
                pausa("Você desmaia sentindo algo dentro de você...")


def gestacao(jogador):
    global infectado, gestacao_turns_remaining
    if infectado and gestacao_turns_remaining is not None:
        gestacao_turns_remaining -= 1
        if gestacao_turns_remaining <= 0:
            pausa("\nVocê sente uma dor terrível no peito...")
            pausa("Algo está rasgando de dentro para fora!")
            pausa("O Chestburster emerge violentamente — seu destino está selado.")
            jogador.vida = 0
            infectado = False
            return True
    return False


def combate(jogador, inimigo):
    """Combate com chance de vitória muito baixa contra o Xenomorfo"""
    pausa(f"\nVocê se depara com {inimigo.nome}!")
    while jogador.vida > 0 and inimigo.vida > 0:
        acao = escolha("Atacar (a), fugir (f): ", ["a", "f"])
        if acao == "a":
            dano = jogador.forca - inimigo.defesa
            if dano > 0:
                inimigo.vida -= dano
                pausa(f"Você causa {dano} de dano!")
            else:
                pausa("Seus golpes não fazem efeito!")

            if inimigo.vida <= 0:
                pausa(f"Você derrotou o {inimigo.nome}! Incrível!")
                return True

            pausa("O Xenomorfo reage!")
            dano_inimigo = inimigo.forca - jogador.defesa
            if dano_inimigo < 0:
                dano_inimigo = 0
            jogador.vida -= dano_inimigo
            pausa(f"Você sofre {dano_inimigo} de dano! Vida restante: {jogador.vida}")

        elif acao == "f":
            if random.random() < 0.5:
                pausa("Você consegue escapar por pouco!")
                return False
            else:
                pausa("Você tenta correr, mas o Xenomorfo é rápido demais!")
                jogador.vida = 0
                pausa("Ele o alcança e tudo termina ali.")
                return False

    return False


def ciclo_turno(jogador):
    global infectado, gestacao_turns_remaining
    while jogador.vida > 0:
        status(jogador)
        if gestacao(jogador):
            break

        acao = escolha("\nExplorar (e), descansar (d), status (s): ", ["e", "d", "s"])
        if acao == "e":
            explorar(jogador)
        elif acao == "d":
            pausa("Você tenta descansar um pouco...")
            jogador.vida = min(100, jogador.vida + 10)
            pausa("Você se sente um pouco melhor.")
        elif acao == "s":
            status(jogador)

        # Chance de encontrar o Xenomorfo após alguns turnos
        if random.random() < 0.2:
            resultado = combate(jogador, alien)
            if resultado:
                pausa("Você sobreviveu... mas sabe que ele voltará.")
            if jogador.vida <= 0:
                break

    if jogador.vida <= 0:
        pausa("\n--- FIM DE JOGO ---")
    else:
        pausa("\n--- Você sobreviveu... por enquanto ---")

#------Configurações do jogo------
tripulante = Heroi("Ripley", 100, 15, 5)
face_hugger = Monstro("Face Hugger", 30, 8, 2, "Pequeno")
alien = Monstro("Xenomorfo", 550, 100, 20, "Grande")

lanterna = Item("Lanterna", "Ajuda a enxergar em áreas escuras, mas atrai criaturas.")
motion_tracker = Item("Motion Tracker", "Detecta tudo que se move perto.")
medkit = Item("Medkit", "Restaura 50 de vida.")
lança_chamas = Arma("Lança-Chamas", "Pouco combustível; afasta o Xenomorfo por pouco tempo.", 50)
roupa_espacial = Armadura("Roupa Espacial", "Protege contra danos e vácuo.", 10)

# Infecção
infectado = False
gestacao_turns_remaining = None
Gestacao_min = 3
Gestacao_max = 8

# Início da história
print("--- Início da Aventura ---")
pausa(f"{tripulante.nome} acorda sozinha na estação Sevastopol...")
pausa("O som distante de metal sendo arranhado ecoa pelos corredores.")
pausa("Você sente que não está sozinha.\n")

# Inicia o loop principal
ciclo_turno(tripulante)
