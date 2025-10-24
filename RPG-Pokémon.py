import random
import time

# ---------------- CLASSES BÁSICAS ---------------- #

class Pokemon:
    def __init__(self, nome, tipo, vida, ataque, especial_nome, especial_dano):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.especial_nome = especial_nome
        self.especial_dano = especial_dano

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, outro):
        dano = self.ataque + random.randint(-2, 5)
        dano = max(0, dano)
        outro.vida = max(0, outro.vida - dano)
        print(f"{self.nome} atacou {outro.nome} causando {dano} de dano! ({outro.vida}/{outro.vida_max} HP restante)")

    def ataque_especial(self, outro):
        dano = self.especial_dano + random.randint(-5, 5)
        dano = max(0, dano)
        outro.vida = max(0, outro.vida - dano)
        print(f"{self.nome} usou {self.especial_nome}! Causou {dano} de dano! ({outro.vida}/{outro.vida_max} HP restante)")

    def curar(self, valor=None):
        if valor is None:
            self.vida = self.vida_max
        else:
            self.vida = min(self.vida + valor, self.vida_max)

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - Vida: {self.vida}/{self.vida_max}"


class Treinador:
    def __init__(self, nome, pokemons, pokebolas=3, dinheiro=100):
        self.nome = nome
        self.pokemons = pokemons
        self.pokebolas = pokebolas
        self.insignias = 0
        self.dinheiro = dinheiro

    def pokemon_vivo(self):
        for p in self.pokemons:
            if p.esta_vivo():
                return p
        return None

    def listar_pokemons(self):
        for i, p in enumerate(self.pokemons):
            status = "VIVO" if p.esta_vivo() else "Nocauteado"
            print(f"{i+1}. {p} - {status}")

    def trocar_pokemon(self):
        vivos = [p for p in self.pokemons if p.esta_vivo()]
        if len(vivos) <= 1:
            print("Você não tem outros Pokémon vivos para trocar!")
            return self.pokemon_vivo()
        print("\nEscolha seu Pokémon:")
        for i, p in enumerate(vivos):
            print(f"{i+1}. {p}")
        while True:
            escolha = input(">> ")
            if escolha.isdigit():
                idx = int(escolha) - 1
                if 0 <= idx < len(vivos):
                    return vivos[idx]
            print("Escolha inválida. Tente novamente.")

# ---------------- SISTEMA DE CURA ---------------- #

def menu_cura(jogador):
    while True:
        print("\nDeseja curar algum Pokémon antes de continuar? (s/n)")
        escolha = input(">> ").lower()
        if escolha == "s":
            print("\nSeus Pokémon:")
            for i, p in enumerate(jogador.pokemons):
                print(f"{i+1} - {p} ({p.vida}/{p.vida_max} HP)")
            while True:
                escolha_pok = input("Escolha um Pokémon para curar (0 para cancelar): ")
                if escolha_pok == "0":
                    break
                if escolha_pok.isdigit() and 1 <= int(escolha_pok) <= len(jogador.pokemons):
                    p = jogador.pokemons[int(escolha_pok)-1]
                    print(f"\nDinheiro disponível: ${jogador.dinheiro}")
                    print("1 - Poção (50 HP) - $30")
                    print("2 - Super Poção (100 HP) - $60")
                    tipo_pocao = input("Escolha a poção: ")
                    if tipo_pocao == "1" and jogador.dinheiro >= 30:
                        p.curar(50)
                        jogador.dinheiro -= 30
                        print(f"{p.nome} recuperou 50 HP! ({p.vida}/{p.vida_max})")
                        break
                    elif tipo_pocao == "2" and jogador.dinheiro >= 60:
                        p.curar(100)
                        jogador.dinheiro -= 60
                        print(f"{p.nome} recuperou 100 HP! ({p.vida}/{p.vida_max})")
                        break
                    else:
                        print("Dinheiro insuficiente ou opção inválida!")
                else:
                    print("Escolha inválida!")
        elif escolha == "n":
            break
        else:
            print("Escolha inválida!")

# ---------------- LOJA ---------------- #

def visitar_loja(jogador):
    while True:
        print("\n--- Loja Pokémon ---")
        print(f"Dinheiro disponível: ${jogador.dinheiro}")
        print("1 - Poção (50 HP) - $30")
        print("2 - Super Poção (100 HP) - $60")
        print("0 - Sair")
        escolha = input("Escolha o item para comprar: ")
        if escolha == "0":
            break
        elif escolha == "1" and jogador.dinheiro >= 30:
            jogador.dinheiro -= 30
            print("Você comprou uma Poção!")
        elif escolha == "2" and jogador.dinheiro >= 60:
            jogador.dinheiro -= 60
            print("Você comprou uma Super Poção!")
        else:
            print("Dinheiro insuficiente ou opção inválida!")

# ---------------- FUNÇÕES DE JOGO EXISTENTES ---------------- #

def escolher_pokemon_inicial():
    print("Escolha seu Pokémon inicial:")
    print("1 - Charmander 🔥")
    print("2 - Squirtle 💧")
    print("3 - Bulbassauro 🌿")
    while True:
        escolha = input(">> ")
        if escolha == "1":
            return Pokemon("Charmander", "Fogo", 245, 112, "Lança-Chamas", 120)
        elif escolha == "2":
            return Pokemon("Squirtle", "Água", 155, 110, "Jato d'Água", 118)
        elif escolha == "3":
            return Pokemon("Bulbassauro", "Planta", 110, 111, "Chicote de Cipó", 117)
        else:
            print("Escolha inválida!")

def chance_captura_percentual(pokemon_selvagem):
    vida_perdida = pokemon_selvagem.vida_max - pokemon_selvagem.vida
    bonus = int((vida_perdida / pokemon_selvagem.vida_max) * 50)
    chance = 40 + bonus
    chance = max(5, min(95, chance))
    return chance

def capturar_pokemon(jogador, pokemon_selvagem):
    if jogador.pokebolas <= 0:
        print("Você não tem mais Pokébolas!")
        return False
    jogador.pokebolas -= 1
    porcentagem = chance_captura_percentual(pokemon_selvagem)
    rolagem = random.randint(1, 100)
    print(f"\nVocê lançou uma Pokébola! Chance de captura: {porcentagem}% (rolou {rolagem})")
    time.sleep(1)
    if rolagem <= porcentagem:
        print(f"✨ {pokemon_selvagem.nome} foi capturado com sucesso! ✨")
        jogador.pokemons.append(pokemon_selvagem)
        return True
    else:
        print(f"{pokemon_selvagem.nome} escapou da Pokébola!")
        return False

def batalha(jogador, oponente, captura_possivel=True):
    print(f"\n--- Batalha contra {oponente.nome}! ---")
    while True:
        pokemon_jogador = jogador.pokemon_vivo()
        pokemon_inimigo = oponente.pokemon_vivo()
        if pokemon_jogador is None:
            print("Todos os seus Pokémon foram derrotados! Fim da jornada.")
            exit()
        if pokemon_inimigo is None:
            print(f"\nVocê derrotou {oponente.nome}!")
            jogador.dinheiro += 50  # Recompensa de vitória
            return True
        print(f"\nSeu Pokémon: {pokemon_jogador}")
        print(f"Inimigo: {pokemon_inimigo}")
        print("\n1. Atacar\n2. Ataque Especial\n3. Trocar Pokémon")
        if captura_possivel:
            print("4. Tentar Capturar\n5. Fugir")
        else:
            print("4. Fugir")
        acao = input(">> ")
        if acao == "1":
            pokemon_jogador.atacar(pokemon_inimigo)
        elif acao == "2":
            pokemon_jogador.ataque_especial(pokemon_inimigo)
        elif acao == "3":
            novo = jogador.trocar_pokemon()
            if novo:
                print(f"Você trocou para {novo.nome}!")
        elif captura_possivel and acao == "4":
            capturado = capturar_pokemon(jogador, pokemon_inimigo)
            if capturado:
                return True
        elif (not captura_possivel and acao == "4") or (captura_possivel and acao == "5"):
            print("Você fugiu da batalha... Fim da jornada.")
            exit()
        else:
            print("Ação inválida!")
            continue
        if not pokemon_inimigo.esta_vivo():
            print(f"{pokemon_inimigo.nome} foi nocauteado!")
            continue
        time.sleep(0.8)
        if random.random() < 0.3:
            pokemon_inimigo.ataque_especial(pokemon_jogador)
        else:
            pokemon_inimigo.atacar(pokemon_jogador)
        if not pokemon_jogador.esta_vivo():
            print(f"{pokemon_jogador.nome} foi derrotado!")
            if jogador.pokemon_vivo() is None:
                print("Todos os seus Pokémon foram derrotados! Fim da jornada.")
                exit()
            else:
                print("Escolha seu próximo Pokémon no menu de troca.")
                continue

# ===================== HISTÓRIA ======================

def main():
    print("🌅 Bem-vindo ao mundo dos Pokémon!")
    time.sleep(1)
    print("Você é um jovem treinador que acaba de chegar ao laboratório do Professor Carvalho.")
    time.sleep(1)
    print("Seu sonho é se tornar o maior campeão da Liga Pokémon!")
    time.sleep(1)
    print("Mas antes, é preciso escolher seu primeiro parceiro...")
    time.sleep(1)
    nome = input("\nProfessor Carvalho: Qual é o seu nome, jovem treinador? ")
    inicial = escolher_pokemon_inicial()
    jogador = Treinador(nome, [inicial], pokebolas=5, dinheiro=100)
    jogador.pokemons.append(inicial)

    print("\n--- Sua jornada começa em Pallet! ---")


    # Cura inicial
    menu_cura(jogador)

    # 1ª Batalha Selvagem
    rato = Pokemon("Rattata", "Normal", 30, 8, "Investida", 12)
    print("\nUm Rattata selvagem apareceu!")
    batalha(jogador, Treinador("Rattata Selvagem", [rato]), captura_possivel=True)

    # Loja entre batalhas
    visitar_loja(jogador)

    # 1º Ginásio
    menu_cura(jogador)
    print("\n--- Ginásio de Pewter: Líder Brock ---")
    brock = Treinador("Brock", [Pokemon("Geodude", "Pedra", 50, 10, "Pedra Dura", 16)])
    batalha(jogador, brock, captura_possivel=False)
    jogador.insignias += 1
    print("Você ganhou a Insígnia de Rocha! 🏅")

    # 2ª Batalha Selvagem
    menu_cura(jogador)
    pidgey = Pokemon("Pidgey", "Voador", 35, 9, "Rajada de Vento", 13)
    print("\nUm Pidgey selvagem apareceu!")
    batalha(jogador, Treinador("Pidgey Selvagem", [pidgey]), captura_possivel=True)

    visitar_loja(jogador)

    # 2º Ginásio
    menu_cura(jogador)
    print("\n--- Ginásio de Cerulean: Líder Misty ---")
    misty = Treinador("Misty", [Pokemon("Staryu", "Água", 55, 5, "Jato d'Água", 10)])
    batalha(jogador, misty, captura_possivel=False)
    jogador.insignias += 1
    print("Você ganhou a Insígnia da Água! 💧")

    # Batalha Final - Liga Pokémon
    menu_cura(jogador)
    print("\n--- Batalha Final: Campeão Lance 🐉 ---")
    lance = Treinador("Lance", [Pokemon("Dragonite", "Dragão", 60, 15, "Hiper Raio", 10)])
    batalha(jogador, lance, captura_possivel=False)

    print(f"\n🏆 Parabéns, {jogador.nome}! Você venceu Lance e se tornou o novo Campeão da Liga Pokémon de Kanto! 🏆")

# ---------------- EXECUÇÃO ---------------- #
if __name__ == "__main__":
    main()