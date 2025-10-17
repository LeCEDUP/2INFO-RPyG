# Desenvolva o seu jogo aqui
import random
import time

# Barbie vs Draculaura - A Batalha pelo Mundo Rosa 
# Feito com muito glitter ✨


# CLASSE DOS PERSONAGENS
class Personagem:
    def __init__(self, nome, vida, poder):
        self.nome = nome
        self.vida = vida
        self.poder = poder

    def atacar(self, inimigo):
        dano = random.randint(self.poder - 5, self.poder + 5)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        time.sleep(1)

    def esta_vivo(self):
        return self.vida > 0



# INTRODUÇÃO DO JOGO

def introducao():
    print(" Bem-vindo(a) ao RPG: Barbie vs Draculaura ")
    time.sleep(1)
    print("O Mundo Rosa está em perigo! ")
    time.sleep(1)
    print("Barbie e Draculaura estão brigando pra ver quem manda no mundo rosa!")
    time.sleep(2)
    print("\nEscolha o seu lado...\n")



# ESCOLHER PERSONAGEM
def escolher_personagem():
    print("1 - Barbie (Ataques de Glitter e Encanto)")
    print("2 - Draculaura (Ataques Sombrio e Charme )")
    escolha = input("\nQuem você quer ser? (1 ou 2): ")

    if escolha == "1":
        jogador = Personagem("Barbie", 100, 20)
        inimigo = Personagem("Draculaura", 100, 18)
    else:
        jogador = Personagem("Draculaura", 100, 18)
        inimigo = Personagem("Barbie", 100, 20)

    print(f"\nVocê escolheu {jogador.nome}! Que comece o brilho... ou a escuridão! \n")
    time.sleep(1)
    return jogador, inimigo

# SISTEMA DE BATALHA
def batalha(jogador, inimigo):
    print(f" {jogador.nome} vs {inimigo.nome} \n")
    time.sleep(1)

    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"{jogador.nome}: {jogador.vida}  | {inimigo.nome}: {inimigo.vida} ")
        print("\nO que você quer fazer?")
        print("1 - Ataque básico")
        print("2 - Ataque especial ")
        print("3 - Passar a vez kk")

        escolha = input("> ")

        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            dano_especial = random.randint(jogador.poder + 5, jogador.poder + 15)
            inimigo.vida -= dano_especial
            print(f"{jogador.nome} lançou um ATAQUE ESPECIAL e causou {dano_especial} de dano!!! ")
            time.sleep(1)
        elif escolha == "3":
            print(f"{jogador.nome} tirou um tempo pra retocar o glitter... ")
            time.sleep(1)
        else:
            print("Você se confundiu com o espelho! ")
            time.sleep(1)

        if inimigo.esta_vivo():
            inimigo.atacar(jogador)

    if jogador.esta_vivo():
        print(f"\n {jogador.nome} venceu e agora domina o Mundo Rosa! ")
    else:
        print(f"\n {inimigo.nome} venceu... O rosa agora é sombrio e cheio de estilo gótico. ")



# INÍCIO DO JOGO
def jogar():
    introducao()
    jogador, inimigo = escolher_personagem()
    batalha(jogador, inimigo)
    print("\n Fim de jogo \n")

jogar()



