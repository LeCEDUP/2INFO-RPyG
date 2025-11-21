import sys
import time

# --- Classes de Itens ---

class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def usar(self, personagem):
        print(f"{self.nome} não tem efeito definido.")

class Arma(Item):
    def __init__(self, nome, descricao, ataque):
        super().__init__(nome, descricao)
        self.ataque = ataque

class Armadura(Item):
    def __init__(self, nome, descricao, defesa):
        super().__init__(nome, descricao)
        self.defesa = defesa

class Pocao(Item):
    def __init__(self, nome, descricao, cura):
        super().__init__(nome, descricao)
        self.cura = cura

    def usar(self, personagem):
        personagem.vida += self.cura
        if personagem.vida > personagem.vida_maxima:
            personagem.vida = personagem.vida_maxima
        print(f"{personagem.nome} usou {self.nome} e recuperou {self.cura} de vida! Vida atual: {personagem.vida}")

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
       
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque_base = ataque
        self.defesa_base = defesa

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        dano_final = dano - self.defesa_base
        if dano_final < 0:
            dano_final = 0
        self.vida -= dano_final
        print(f"{self.nome} recebeu {dano_final} de dano! Vida restante: {self.vida if self.vida > 0 else 0}")

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.inventario = []
        self.arma = None
        self.armadura = None
        self.experiencia = 0
        self.nivel = 1

    def ataque_total(self):
        bonus = self.arma.ataque if self.arma else 0
        return self.ataque_base + bonus

    def defesa_total(self):
        bonus = self.armadura.defesa if self.armadura else 0
        return self.defesa_base + bonus

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")
        dano = self.ataque_total()
        alvo.receber_dano(dano)

    def equipar_item(self, item):
        if isinstance(item, Arma):
            self.arma = item
            print(f"{self.nome} arma equipada {item.nome}.")
        elif isinstance(item, Armadura):
            self.armadura = item
            print(f"{self.nome} armadura equipada {item.nome}.")
        else:
            print("Esse item não pode ser equipado.")

    def ganhar_experiencia(self, xp):
        self.experiencia += xp
        print(f"{self.nome} ganhou {xp} XP!")
        while self.experiencia >= self.nivel * 100:
            self.experiencia -= self.nivel * 100
            self.nivel += 1
            self.vida_maxima += 20
            self.vida = self.vida_maxima
            self.ataque_base += 5
            self.defesa_base += 2
            print(f"Parabéns! {self.nome} subiu para o nível {self.nivel}!")

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tamanho):
        super().__init__(nome, vida, ataque, defesa)
        self.tamanho = tamanho

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")
        dano = self.ataque_base
        alvo.receber_dano(dano)

# --- Funções para o jogo ---

def slowprint(text, delay=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def introducao():
    slowprint("Bem-vindo ao reino de Hogwarts!\n")
    slowprint("Um lugar onde guerreiros nascem e monstros espreitam nas sombras.\n")
    slowprint("Você é Arthur, um jovem guerreiro, destinado a salvar o reino das forças do mal.\n")
    slowprint("Sua jornada começa agora...\n")

def mostrar_inventario(heroi):
    print("\nSeu inventário:")
    if not heroi.inventario:
        print(" - Vazio")
    else:
        for i, item in enumerate(heroi.inventario, 1):
            print(f" {i}. {item.nome} - {item.descricao}")

def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Ver status do herói")
    print("2. Ver inventário")
    print("3. Equipar item")
    print("4. Usar poção")
    print("5. Lutar contra um monstro")
    print("6. Sair do jogo")

def escolher_item_por_tipo(heroi, tipo_classe):
    itens_tipo = [item for item in heroi.inventario if isinstance(item, tipo_classe)]
    if not itens_tipo:
        print(f"Você não tem itens do tipo {tipo_classe.__name__} para equipar.")
        return None
    print(f"Escolha um {tipo_classe.__name__} para equipar:")
    for i, item in enumerate(itens_tipo, 1):
        print(f"{i}. {item.nome} - {item.descricao}")
    escolha = input("Digite o número do item: ")
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(itens_tipo):
        print("Escolha inválida.")
        return None
    return itens_tipo[int(escolha)-1]

def escolher_pocao(heroi):
    pocao = None
    for item in heroi.inventario:
        if isinstance(item, Pocao):
            pocao = item
            break
    if not pocao:
        print("Não há poções para usar.")
        return None
    return pocao

def luta(heroi, monstro):
    slowprint(f"\nUma batalha começa! {heroi.nome} VS {monstro.nome} ({monstro.tamanho})\n")
    while heroi.esta_vivo() and monstro.esta_vivo():
        print(f"\nVida {heroi.nome}: {heroi.vida}/{heroi.vida_maxima}")
        print(f"Vida {monstro.nome}: {monstro.vida}/{monstro.vida_maxima}")
        print("\n1. Atacar")
        print("2. Usar poção")
        print("3. Fugir")
        escolha = input("Escolha sua ação: ")
        if escolha == '1':
            heroi.atacar(monstro)
            if monstro.esta_vivo():
                monstro.atacar(heroi)
        elif escolha == '2':
            pocao = escolher_pocao(heroi)
            if pocao:
                pocao.usar(heroi)
                heroi.inventario.remove(pocao)
                if monstro.esta_vivo():
                    monstro.atacar(heroi)
        elif escolha == '3':
            slowprint(f"{heroi.nome} fugiu da batalha!")
            return False
        else:
            print("Opção inválida.")
    if heroi.esta_vivo():
        slowprint(f"\n{heroi.nome} venceu a batalha contra {monstro.nome}!")
        xp = 50 if monstro.tamanho == "Pequeno" else 150
        heroi.ganhar_experiencia(xp)
        return True
    else:
        slowprint(f"\n{heroi.nome} foi derrotado pelo {monstro.nome}...")
        return False

def main():
    introducao()
    
    # Criando personagem principal
    heroi = Heroi("Arthur", 100, 20, 10)
    
    # Criando itens iniciais
    espada = Arma("Espada Longa", "Uma espada afiada.", 30)
    faca = Arma("Faca Canivete", "Uma espada afiada.", 10)
    escudoferro = Armadura("Escudo de Ferro", "Um escudo resistente.", 20)
    escudodiamante = Armadura ("Escudo de Diamante", "Um escudo resistente.", 35)
    pocao = Pocao("Poção de Vida", "Restaura 50 de vida.", 75)

    # Adicionando itens ao inventário
    heroi.inventario.extend([espada, escudoferro,escudodiamante, pocao, faca])

    slowprint("Você começa sua aventura com alguns itens em seu inventário.")

    # Loop principal do jogo
    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print(f"\nNome: {heroi.nome}")
            print(f"Vida: {heroi.vida}/{heroi.vida_maxima}")
            print(f"Ataque: {heroi.ataque_total()}")
            print(f"Defesa: {heroi.defesa_total()}")
            print(f"Nível: {heroi.nivel}")
            print(f"Experiência: {heroi.experiencia}/{heroi.nivel * 100}")
            arma_nome = heroi.arma.nome if heroi.arma else "Nenhuma"
            armadura_nome = heroi.armadura.nome if heroi.armadura else "Nenhuma"
            print(f"Arma equipada: {arma_nome}")
            print(f"Armadura equipada: {armadura_nome}")

        elif escolha == '2':
            mostrar_inventario(heroi)

        elif escolha == '3':
            print("\nQual item quer equipar?")
            print("1. Arma")
            print("2. Armadura")
            tipo = input("Escolha: ")
            if tipo == '1':
                item = escolher_item_por_tipo(heroi, Arma)
                if item:
                    heroi.equipar_item(item)
            elif tipo == '2':
                item = escolher_item_por_tipo(heroi, Armadura)
                if item:
                    heroi.equipar_item(item)
            else:
                print("Opção inválida.")

        elif escolha == '4':
            pocao = escolher_pocao(heroi)
            if pocao:
                pocao.usar(heroi)
                heroi.inventario.remove(pocao)

        elif escolha == '5':
            print("\nEscolha um monstro para enfrentar:")
            print("1. Gnomo mal (Pequeno)")
            print("2. Dragão (Grande)")
            monstro_escolha = input("Escolha: ")
            if monstro_escolha == '1':
                goblin = Monstro("Gnomo mal", 30, 8, 2, "Pequeno")
                venceu = luta(heroi, goblin)
                if not venceu:
                    print("Você perdeu a batalha. Fim de jogo.")
                    break
            elif monstro_escolha == '2':
                dragao = Monstro("Dragão", 200, 30, 10, "Grande")
                venceu = luta(heroi, dragao)
                if not venceu:
                    print("Você perdeu a batalha. Fim de jogo.")
                    break
                else:
                    print("Parabéns! Você derrotou o Dragão e salvou o reino!")
                    break
            else:
                print("Opção inválida.")

        elif escolha == '6':
            print("Saindo do jogo... Até a próxima!")
            sys.exit()

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()