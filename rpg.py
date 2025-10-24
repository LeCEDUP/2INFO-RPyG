import random

class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.itens = []

class Monstro:
    def __init__(self, nome, vida, ataque, defesa, tipo):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo

class Arma:
    def __init__(self, nome, dano, bonus_ataque):
        self.nome = nome
        self.dano = dano
        self.bonus_ataque = bonus_ataque

class Armadura:
    def __init__(self, nome, defesa):
        self.nome = nome
        self.defesa = defesa

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Iniciar Aventura\n2 - Sair\n3 - Ver Introdução")
    return input("Escolha: ")

class Heroi:
    ...
    def atacar(self, inimigo):
        dano_bruto = random.randint(self.ataque - 3, self.ataque + 3)
        dano_real = max(dano_bruto - inimigo.defesa, 0)
        if random.random() < 0.15:
            dano_real = int(dano_real * 1.8)
            print("✨ CRÍTICO GLAMOUR ✨")
        inimigo.vida = max(inimigo.vida - dano_real, 0)
        print(f"{self.nome} atacou {inimigo.nome} causando {dano_real} de dano! Vida restante: {inimigo.vida}\n")

class Monstro:
    ...
    def atacar(self, inimigo):
        dano_bruto = random.randint(self.ataque - 3, self.ataque + 3)
        dano_real = max(dano_bruto - inimigo.defesa, 0)
        if random.random() < 0.15:
            dano_real = int(dano_real * 1.8)
            print("⚡ POLLY CRÍTICA! ⚡")
        inimigo.vida = max(inimigo.vida - dano_real, 0)
        print(f"{self.nome} contra-ataca causando {dano_real} de dano! Vida restante: {inimigo.vida}\n")

class Heroi:
    ...
    def equipar_item(self, item):
        self.itens.append(item)
        if isinstance(item, Arma):
            self.ataque += item.bonus_ataque
        elif isinstance(item, Armadura):
            self.defesa += item.defesa

def menu_introducao():
    while True:
        print("\n===== INTRODUÇÃO INTERATIVA =====")
        print("1 - Sobre o Jogo")
        print("2 - Armaduras")
        print("3 - Armas")
        print("4 - Superpoderes")
        print("5 - Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n✨ SOBRE O JOGO ✨")
            print("O mundo fashion está em perigo!")
            print("Polly Pocket quer roubar o brilho da Barbie!")
        elif escolha == "2":
            print("\nARMADURAS DISPONÍVEIS: Vestido Brilhante, Casaco Fashion, Jaqueta Rosa de Poder...")
        elif escolha == "3":
            print("\nARMAS DISPONÍVEIS: Batom Laser, Secador Explosivo, Salto da Justiça...")
        elif escolha == "4":
            print("\nSUPERPODERES DISPONÍVEIS: Bola de Glitter, Invisibilidade Fashion...")
        elif escolha == "5":
            break
        else:
            print("Opção inválida!\n")
       
def escolher_itens(nome_categoria, opcoes):
    print(f"\nEscolha até 2 {nome_categoria}:")
    for i, item in enumerate(opcoes, 1):
        print(f"{i}. {item.nome if hasattr(item, 'nome') else item}")

    escolhas = []
    while len(escolhas) < 2:
        escolha = input(f"Digite o número (Enter para parar): ")
        if escolha == "":
            break
        if not escolha.isdigit() or int(escolha) not in range(1, len(opcoes) + 1):
            print("Escolha inválida!")
            continue
        item = opcoes[int(escolha) - 1]
        if item in escolhas:
            print("Você já escolheu esse!")
            continue
        escolhas.append(item)
    return escolhas

def sortear_itens():
    armas_possiveis = [
        Arma("Batom Laser", random.randint(10, 18), random.randint(1, 4)),
        Arma("Secador Explosivo", random.randint(11, 19), random.randint(2, 5)),
        Arma("Salto da Justiça", random.randint(8, 15), random.randint(1, 3)),
        Arma("Escova Reluzente", random.randint(9, 17), random.randint(1, 4)),
        Arma("Pincel Mágico", random.randint(7, 14), random.randint(1, 3))
    ]

    armaduras_possiveis = [
        Armadura("Vestido Brilhante", random.randint(4, 8)),
        Armadura("Casaco Fashion", random.randint(3, 7)),
        Armadura("Jaqueta Rosa de Poder", random.randint(5, 9)),
        Armadura("Saia de Diamante", random.randint(4, 8)),
        Armadura("Capa da Elegância", random.randint(4, 9))
    ]

    superpoderes_possiveis = [
        "Bola de Glitter",
        "Invisibilidade Fashion",
        "Raio Rosa",
        "Teletransporte Glamouroso",
        "Chicote de Confete"
    ]

    return armas_possiveis, armaduras_possiveis, superpoderes_possiveis

def iniciar_aventura():
    nome = input("Qual é o nome da sua Barbie heroína? ")
    barbie = Heroi(nome, 100, random.randint(14, 20), random.randint(5, 10))

    armas, armaduras, poderes = sortear_itens()
    armas_escolhidas = escolher_itens("armas", armas)
    armaduras_escolhidas = escolher_itens("armaduras", armaduras)
    poderes_escolhidos = escolher_itens("superpoderes", poderes)

    for a in armas_escolhidas:
        barbie.equipar_item(a)
    for a in armaduras_escolhidas:
        barbie.equipar_item(a)

    polly = Monstro("Polly Pocket", random.randint(90, 110), random.randint(13, 20), random.randint(5, 10), "Fashion Rival")

    print(f"\n✨ BATALHA COMEÇOU! ✨")
    print(f"{barbie.nome} vs Polly Pocket\n")

    while barbie.vida > 0 and polly.vida > 0:
        print(f"{barbie.nome} HP: {barbie.vida} | Polly HP: {polly.vida}")
        print("1 - Atacar\n2 - Fugir")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            barbie.atacar(polly)
            if polly.vida <= 0:
                print(f"✨ {barbie.nome} venceu com muito glamour! ✨")
                break
            polly.atacar(barbie)
            if barbie.vida <= 0:
                print(f"❌ {barbie.nome} perdeu o brilho... Polly dominou a passarela!")
                break
        elif acao == "2":
            print(f"{barbie.nome} saiu da passarela com dignidade ✨")
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        escolha = menu_principal()
        if escolha == "1":
            iniciar_aventura()
        elif escolha == "2":
            print("👋 Saindo do mundo fashion... até logo!")
            break
        elif escolha == "3":
            menu_introducao()
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()
          

     