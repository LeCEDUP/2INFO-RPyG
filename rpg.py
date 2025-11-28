import random
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

# --------------------------
# Personagens
# --------------------------
corvian = Heroi("Corvian", 100, 15, 5)
amaris = {"nome": "Amaris", "profissao": "Médica"}

# Inimigos
vilao_final = Monstro("Caçador Misterioso", 100, 25, 5, "Humano")
horda_zumbi = Monstro("Horda de Zumbis", 120, 10, 2, "Zumbi")
mutante = Monstro("Mutante Feral", 80, 15, 4, "Mutante")  # Mais fraco

# Itens iniciais
faca = Arma("Faca de Sobrevivência", "Uma faca passada de geração em geração.", 10)
colete = Armadura("Colete de Couro", "Proteção básica.", 5)
poção = Item("Poção de Vida", "Restaura 30 de vida.")

corvian.inventario.extend([faca, colete])
corvian.equipar_item(faca)
corvian.equipar_item(colete)

# Flag para aprendizado de poção
aprendeu_pocao = False

# --------------------------
# Função de combate interativo padrão
# --------------------------
def combate_interativo(heroi, inimigo):
    global aprendeu_pocao
    print(f"\n--- BATALHA: {heroi.nome} VS {inimigo.nome} ---")
    
    while heroi.esta_vivo() and inimigo.esta_vivo():
        print(f"\n{heroi.nome} - Vida: {heroi.vida} | {inimigo.nome} - Vida: {inimigo.vida}")
        print("Escolha sua ação: [1] Atacar  [2] Defender  [3] Fugir  [4] Usar Poção")
        escolha = input("> ").strip()
        
        if escolha == "1":
            critico = random.random() < 0.2
            dano = max(0, heroi.ataque - inimigo.defesa)
            if critico:
                dano *= 2
                print("💥 CRÍTICO! Dano dobrado!")
            inimigo.receber_dano(dano)
        elif escolha == "2":
            print(f"{heroi.nome} se prepara para defender o próximo ataque.")
        elif escolha == "3":
            print(f"{heroi.nome} foge da batalha e volta para Amaris para se recuperar.")
            heroi.vida = min(heroi.vida + 50, 100)
            print(f"{amaris['nome']} recuperou você! Vida atual: {heroi.vida}")
            return True
        elif escolha == "4":
            if not aprendeu_pocao:
                print("Você ainda não sabe usar poções! Amaris precisa te ensinar.")
            else:
                poções = [item for item in heroi.inventario if isinstance(item, Item) and "Poção" in item.nome]
                if poções:
                    pocao = poções[0]
                    heroi.vida += 30
                    heroi.inventario.remove(pocao)
                    print(f"{heroi.nome} usou {pocao.nome}. Vida atual: {heroi.vida}")
                else:
                    print("Você não possui poções.")
        else:
            print("Opção inválida, tente novamente.")

        if inimigo.esta_vivo() and escolha != "3":
            dano_inimigo = max(0, inimigo.ataque - heroi.defesa)
            if escolha == "2":
                dano_inimigo = dano_inimigo // 2
            heroi.receber_dano(dano_inimigo)

    return heroi.esta_vivo()

# --------------------------
# Função de primeira batalha obrigatória (derrota)
# --------------------------
def combate_obrigatorio_perder(heroi, inimigo):
    print(f"\n--- BATALHA: {heroi.nome} VS {inimigo.nome} ---")
    print(f"{inimigo.nome} é muito poderoso! Você precisa enfrentar essa luta, mas não conseguirá vencê-lo.\n")
    
    turno = 1
    while heroi.esta_vivo():
        print(f"\nTurno {turno} - {heroi.nome} (Vida: {heroi.vida}) vs {inimigo.nome} (Vida: {inimigo.vida})")
        print("Escolha sua ação: [1] Atacar  [2] Defender  [3] Fugir")
        escolha = input("> ").strip()

        if escolha == "1":  # Atacar
            critico = random.random() < 0.2
            dano = max(0, heroi.ataque - inimigo.defesa)
            if critico:
                dano *= 2
                print("💥 CRÍTICO! Dano dobrado!")
            inimigo.vida -= dano
            print(f"{heroi.nome} causou {dano} de dano. Vida do inimigo: {inimigo.vida}")
        elif escolha == "2":  # Defender
            print(f"{heroi.nome} se prepara para reduzir dano no próximo ataque.")
        elif escolha == "3":  # Fugir
            print(f"{heroi.nome} tenta fugir, mas {inimigo.nome} é rápido e não permite!")
        else:
            print("Opção inválida!")

        # Ataque do vilão
        dano_inimigo = max(0, inimigo.ataque - heroi.defesa)
        if escolha == "2":
            dano_inimigo = dano_inimigo // 2
        heroi.vida -= dano_inimigo
        print(f"{inimigo.nome} atacou e causou {dano_inimigo} de dano. Vida de {heroi.nome}: {heroi.vida}")

        turno += 1

        if heroi.vida <= 0:
            print(f"\n{heroi.nome} foi derrotado pelo {inimigo.nome}...\n")
            break

    return False  # Sempre derrota

# --------------------------
# História
# --------------------------
print("--- Apocalipse Zumbi ---")
print("O vírus transformou humanos em caçadores cruéis. Corvian sobrevive no caos.\n")

input("Pressione Enter para continuar...\n")
print("Enquanto coleta lenha, um estrondo na cabana do vizinho. Chegando lá, um buraco vazio e uma figura sussurra:")
print("- Tarde demais.\n")

# Primeira batalha (jogável, mas derrota garantida)
combate_obrigatorio_perder(corvian, vilao_final)

input("Pressione Enter para continuar...\n")
print(f"{amaris['nome']} aparece e ajuda Corvian a se recuperar dos ferimentos.")
print(f"Ela ensina Corvian a usar poções de vida para se proteger melhor.\n")
aprendeu_pocao = True
corvian.inventario.append(poção)
corvian.vida = 100
print(f"{corvian.nome} aprendeu a usar poções! Vida restaurada: {corvian.vida}")

input("Pressione Enter para continuar...\n")
print("Após a recuperação, Corvian parte para enfrentar novos desafios.")

# Segunda batalha: Horda de Zumbis
sobreviveu = combate_interativo(corvian, horda_zumbi)
if sobreviveu:
    print("Você derrotou a Horda de Zumbis e recebeu uma Poção de Vida como recompensa!")
    corvian.inventario.append(Item("Poção de Vida", "Restaura 30 de vida."))
else:
    print("Você foi derrotado. Fim de jogo.")
    exit()

input("\nPressione Enter para continuar...\n")
print("Um Mutante Feral aparece, mais fraco que o esperado, mas ainda perigoso!")

# Terceira batalha: Mutante Feral (derrotável)
sobreviveu = combate_interativo(corvian, mutante)
if sobreviveu:
    print(f"\nVocê derrotou o {mutante.nome}!")
    print("Com cuidado, Corvian e Amaris retiram a pele do mutante e fabricam uma armadura resistente.")
    armadura_mutante = Armadura("Armadura de Pele de Mutante", "Aumenta ataque e defesa para enfrentar o vilão final.", 15)
    corvian.equipar_item(armadura_mutante)
    print(f"{corvian.nome} agora está equipado com a {armadura_mutante.nome}!")
else:
    print("Você foi derrotado. Fim de jogo.")
    exit()

input("\nPressione Enter para continuar...\n")
print(f"Preparado e fortalecido, Corvian se aproxima para enfrentar novamente o {vilao_final.nome}.")

# Batalha final: Vilão (narrativa)
print(f"\nApós uma luta épica, Corvian derrota o {vilao_final.nome} com a ajuda de Amaris!")
print("O reino é salvo e, finalmente, Corvian e Amaris podem viver em paz e se casar.")

print("\n--- Fim da Aventura ---")
