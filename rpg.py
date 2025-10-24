from personagens.heroi import Heroi
from personagens.monstro import Monstro
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
import random
import sys

heroi = Heroi("A Fera", 120, 18, 6)

Esqueleto = Monstro("Esqueleto", 40, 10, 0, "Morto vivo", experiencia=12)
Soldado_Morto = Monstro("Soldado Morto", 50, 15, 10, "Morto vivo", experiencia=20)
Bau_vivo = Monstro("Baú vivo", 30, 30, 5, "Mimico", experiencia=15)
Cavaleiro_Morto = Monstro("Cavaleiro Morto", 100, 20, 40, "Morto vivo", experiencia=40)
Ogro = Monstro("Ogro", 150, 30, 0, "Floresta", experiencia=30)
Goblin = Monstro("Goblin", 25, 5, 5, "Floresta", experiencia=8)
Aranha_Gigante = Monstro("Aranha Gigante", 80, 25, 10, "Floresta", experiencia=25)
Mago_Negro = Monstro("Mago Negro", 100, 60, 10, "Mago", experiencia=60)
Aberracao = Monstro("Aberração", 200, 50, 40, "Morto vivo", experiencia=300)
MONSTROS = [Esqueleto, Soldado_Morto, Bau_vivo, Cavaleiro_Morto, Ogro, Goblin, Aranha_Gigante,
            Mago_Negro, Aberracao]

PHASES = [
    [Goblin, Esqueleto],
    [Aranha_Gigante, Ogro, Soldado_Morto],
    [Mago_Negro, Cavaleiro_Morto, Bau_vivo],
    [Aberracao],
]

CURRENT_PHASE = 0
DEFEATS_IN_PHASE = 0
DEFEATS_REQUIRED = 3 

Carne = Item("Carne", "Restaura 10 de vida")
Carne_Podre = Item("Carne Podre", "Restaura 5 de vida")
Carne_Fresca = Item("Carne Fresca", "Restaura 30 de vida")
Pocao_Negra = Item("Poção Negra", "Perde 10% da vida mas ganha 15% de dano")
Pedra_Azul = Item("Pedra Azul", "Aumenta a armadura em 10%")
Carne_Mostro = Item("Carne Mostro", "Aumenta o dano em 30%")

Osso = Arma("Osso", "Um osso de alguem", 5)
Osso_Grande = Arma("Osso Grande", "Um osso bem grande e duro de alguem", 10)
Espada = Arma("Espada de Ferro", "Uma espada de ferro classica", 15)
Espada_dos_Mostros = Arma("Espada dos Mostros", "Uma espada feita a partir de monstros", 30)
Machado_de_Guerra = Arma("Machado de Guerra", "Uma arma feita para batalhar", 50)

Escudo = Armadura("Escudo de Ferro", "Um escudo resistente", 10)
Casco = Armadura("Casco", "Um casco de uma griatura antiga", 30)
Armadura_do_Quardiao = Armadura("Armadura do Quardião", "Armadura robusta deixada por um quardião", 50)



def imprimir_status():
    print(f"\n--- Status de {heroi.nome} ---")
    print(f"Vida: {heroi.vida}/{getattr(heroi, 'max_vida', heroi.vida)}")
    print(f"Ataque: {heroi.ataque}")
    print(f"Defesa: {heroi.defesa}")
    print(f"Nível: {getattr(heroi, 'nivel', '?')}")
  
    if hasattr(heroi, 'experiencia'):
        faltam = heroi.experiencia_para_proximo_nivel()
        print(f"Experiência: {heroi.experiencia} (faltam {faltam} para o próximo nível)")
    arma_nome = heroi.arma_equipada.nome if getattr(heroi, 'arma_equipada', None) else 'Nenhuma'
    armadura_nome = heroi.armadura_equipada.nome if getattr(heroi, 'armadura_equipada', None) else 'Nenhuma'
    print(f"Arma equipada: {arma_nome} | Armadura equipada: {armadura_nome}")
    print(f"Inventário: {[item.nome for item in heroi.inventario]}")
 
    try:
        print(f"Fase atual: {CURRENT_PHASE + 1}/{len(PHASES)} - Derrotas nesta fase: {DEFEATS_IN_PHASE}/{DEFEATS_REQUIRED}")
    except Exception:
        pass



DROPS_BY_PHASE = [
    
    [Osso, Carne_Podre],
    
    [Carne, Osso_Grande, Escudo],
    
    [Carne_Fresca, Espada, Pedra_Azul, Casco],
 
    [Espada_dos_Mostros, Armadura_do_Quardiao, Machado_de_Guerra, Carne_Mostro, Pocao_Negra],
]


def usar_item(nome_item):
    encontrados = [i for i in heroi.inventario if i.nome.lower() == nome_item.lower()]
    if not encontrados:
        print("Você não tem esse item no inventário.")
        return
    item = encontrados[0]
    if item is Carne:
        heroi.vida = min(heroi.max_vida, heroi.vida + 10)
        print(f"{heroi.nome} comeu {item.nome} e recuperou 10 de vida. Vida atual: {heroi.vida}")
    elif item is Carne_Fresca:
        heroi.vida = min(heroi.max_vida, heroi.vida + 30)
        print(f"{heroi.nome} comeu {item.nome} e recuperou 30 de vida. Vida atual: {heroi.vida}")
    elif item is Carne_Podre:
        heroi.vida = min(heroi.max_vida, heroi.vida + 5)
        print(f"{heroi.nome} comeu {item.nome} e recuperou 5 de vida. Vida atual: {heroi.vida}")
    elif item is Pocao_Negra:
        perda = max(1, int(heroi.vida * 0.10))
        ganho = max(1, int(heroi.ataque * 0.15))
        heroi.vida -= perda
        heroi.ataque += ganho
        print(f"{heroi.nome} usou {item.nome}: -{perda} vida, +{ganho} ataque (temporário).")
    elif item is Carne_Mostro:
        ganho = max(1, int(heroi.ataque * 0.30))
        heroi.ataque += ganho
        print(f"{heroi.nome} comeu {item.nome} e ganhou +{ganho} de ataque.")
    elif item is Pedra_Azul:
        ganho = max(1, int(heroi.defesa * 0.10))
        heroi.defesa += ganho
        print(f"{heroi.nome} usou {item.nome} e aumentou a defesa em +{ganho}.")
    else:
        print(f"{item.nome} não tem efeito implementado ainda.")
    
    try:
        heroi.inventario.remove(item)
    except ValueError:
        pass


def encontro_aleatorio():
    
    global CURRENT_PHASE
    if CURRENT_PHASE >= len(PHASES):
        CURRENT_PHASE = len(PHASES) - 1
    opcoes = PHASES[CURRENT_PHASE]
    monstro = random.choice(opcoes)
    
    inimigo = Monstro(monstro.nome, monstro.vida, monstro.ataque, monstro.defesa, monstro.tipo, experiencia=getattr(monstro, 'experiencia', 10))
    print(f"\nVocê encontrou um {inimigo.nome} ({inimigo.tipo}) na Fase {CURRENT_PHASE + 1}!")
    batalha(inimigo)


def jogar_fora(nome_item):
    
    success = heroi.descartar_item(nome_item)
    if success:
        print(f"Você jogou fora {nome_item}.")
    else:
        print(f"Não foi possível jogar fora {nome_item}.")


def batalha(inimigo):
   
    global CURRENT_PHASE, DEFEATS_IN_PHASE
    while heroi.esta_vivo() and inimigo.esta_vivo():
        print(f"\nSua vez: Vida {heroi.vida} | {inimigo.nome}: Vida {inimigo.vida}")
        escolha = input("Escolha: (a)tacar, (u)sar item, (f)ugir: ").strip().lower()
        if escolha in ('a', 'atacar'):
            heroi.atacar(inimigo)
        elif escolha in ('u', 'usar'):
            nome_item = input("Digite o nome do item para usar: ")
            usar_item(nome_item)
        elif escolha in ('f', 'fugir'):
            if random.random() < 0.5:
                print("Você conseguiu fugir!")
               
                try:
                    inimigo_nome = (inimigo.nome or '').lower()
                except Exception:
                    inimigo_nome = ''
                if inimigo_nome in ('aberração', 'aberracao'):
                    prev = max(0, CURRENT_PHASE - 1)
                    if prev != CURRENT_PHASE:
                        CURRENT_PHASE = prev
                        print("Você fugiu do chefão e recuou para a fase anterior para se fortalecer.")
                    else:
                        print("Você fugiu do chefão, mas já está na fase inicial.")
                return
            else:
                print("Fuga falhou!")
        else:
            print("Ação inválida.")
            continue

        if inimigo.esta_vivo():
            inimigo.atacar(heroi)

    if heroi.esta_vivo():
        print(f"\nVocê derrotou o {inimigo.nome}!")
        if random.random() < 0.6:
            phase_idx = min(CURRENT_PHASE, len(DROPS_BY_PHASE) - 1)
            choices = DROPS_BY_PHASE[phase_idx] if phase_idx >= 0 else []
            if choices:
                drop = random.choice(choices)
                heroi.inventario.append(drop)
                print(f"Você encontrou: {drop.nome}.")
     
        if hasattr(heroi, 'ganhar_experiencia') and hasattr(inimigo, 'experiencia'):
            heroi.ganhar_experiencia(inimigo.experiencia)
    
        DEFEATS_IN_PHASE += 1
   
        if inimigo.nome.lower() == 'aberração' or inimigo.nome.lower() == 'aberracao':
            print(f"\nParabéns! Você derrotou a {inimigo.nome}, o chefão final! O reino está salvo.")
            sys.exit(0)

        required = DEFEATS_REQUIRED
     
        if DEFEATS_IN_PHASE >= required:
            DEFEATS_IN_PHASE = 0
            if CURRENT_PHASE < len(PHASES) - 1:
                CURRENT_PHASE += 1
                print(f"\nVocê avançou para a Fase {CURRENT_PHASE + 1}! Novos inimigos surgem...")
            else:
                print("\nVocê já está na fase final. Prepare-se para o chefão!")
    else:
        print("Você foi derrotado... Fim de jogo.")
        sys.exit(0)


def mostrar_intro():
    print("\n--- Prologue: A Sombra sobre Vale Antigo ---\n")
    print("As brumas cobriram o Vale Antigo. Antigas fortalezas ecoam com passos que não pertencem aos vivos.")
    print("Você é conhecido apenas como 'A Fera', um guerreiro marcado pelas cicatrizes do passado.")
    print("Sua missão: descobrir a origem da corrupção e salvar o que resta do reino. Sobreviva, evolua e escolha seu destino.")


def run_game():
    mostrar_intro()
   
    if not any(i.nome == 'Osso' for i in heroi.inventario):
        heroi.inventario.extend([Osso, Escudo, Carne])

    while True:
        print("\nO que deseja fazer agora?")
        print("1) Explorar")
        print("2) Descansar (recupera 20 vida)")
        print("3) Ver status")
        print("4) Ver inventário / equipar item")
        print("5) Usar item")
        print("6) Sair do jogo")
        print("7) Jogar fora item")
        opc = input("Escolha (1-7): ").strip()
        if opc == '1':
            encontro_aleatorio()
        elif opc == '2':
            heroi.vida = min(heroi.max_vida, heroi.vida + 20)
            print(f"Você descansou e recuperou 20 de vida. Vida atual: {heroi.vida}")
        elif opc == '3':
            imprimir_status()
        elif opc == '4':
            print(f"Inventário: {[item.nome for item in heroi.inventario]}")
            escolher = input("Digite o nome do item para equipar (ou enter para voltar): ")
            if escolher:
                encontrados = [i for i in heroi.inventario if i.nome.lower() == escolher.lower()]
                if encontrados:
                    heroi.equipar_item(encontrados[0])
                else:
                    print("Item não encontrado no inventário.")
        elif opc == '5':
            nome_item = input("Nome do item para usar: ")
            usar_item(nome_item)
        elif opc == '6':
            print("Saindo do jogo. Até a próxima aventura!")
            break
        elif opc == '7':
            nome_item = input("Nome do item para jogar fora: ")
            jogar_fora(nome_item)
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    run_game()





