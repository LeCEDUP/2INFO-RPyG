# Desenvolva o seu jogo aqui
from itens.arma import Arma
from itens.armadura import Armadura
from itens.item import Item
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import time

def pausa(texto, segundos=1):
    print(texto)
    time.sleep(segundos)

def introducao():
    print("🔥 Demon Slayer RPG 🔥")
    print("Você é um caçador de demônios em treinamento na Corporação dos Caçadores.")
    print("Seu objetivo: eliminar os demônios que ameaçam os humanos durante a noite.")
    print("Prepare sua espada Nichirin e sua respiração.\n")

def main():
    introducao()

    nome = input("Digite o nome do seu caçador: ")
    heroi = Heroi(nome, 100, 15, 5)

     espada_nichirin = Arma("Espada Nichirin", "Espada forjada com minério especial, eficaz contra demônios.", 10)
    uniforme = Armadura("Uniforme da Corporação", "Protege contra ataques e cortes.", 5)
    poção_vida = Item("Poção de Recuperação", "Restaura 30 de vida.")

    heroi.inventario.extend([espada_nichirin, uniforme, poção_vida])
    heroi.equipar_item(espada_nichirin)
    heroi.equipar_item(uniforme)

     pausa(f"\n{heroi.nome} iniciou sua jornada com a {espada_nichirin.nome} e o {uniforme.nome} equipados!")

    demonio_filho = Monstro("Demônio Menor", 40, 8, 3, "Fraco")
    demonio_lua_inferior = Monstro("Lua Inferior Seis", 90, 15, 6, "Médio")
    demonio_lua_superior = Monstro("Akaza - Lua Superior Três", 200, 25, 10, "Poderoso")

    pausa("\n🌲 Você entra em uma floresta sombria à noite...")
    pausa("Um Demônio Menor surge do escuro e ataca!")

    batalha(heroi, demonio_filho)
    if not heroi.esta_vivo():
        fim_de_jogo(heroi)
        return

    heroi.ganhar_experiencia(50)
    pausa("Você encontra uma nova Poção de Recuperação e guarda no inventário.")
    heroi.inventario.append(Item("Poção de Recuperação", "Restaura 30 de vida."))

    pausa("\n💀 A lua brilha forte... surge uma das Luas Inferiores!")
    batalha(heroi, demonio_lua_inferior)
    if not heroi.esta_vivo():
        fim_de_jogo(heroi)
        return

    heroi.ganhar_experiencia(100)
    pausa("Você encontrou a 'Bandana da Perseverança' (+3 defesa).")
    bandana = Armadura("Bandana da Perseverança", "Símbolo dos caçadores veteranos.", 3)
    heroi.inventario.append(bandana)
    heroi.equipar_item(bandana)
        pausa("\n🔥 O ar fica pesado... Akaza surge diante de você!")
    pausa("Akaza sorri e diz: 'Mostre-me sua força, Caçador!'")

    batalha(heroi, demonio_lua_superior)
    if heroi.esta_vivo():
        pausa(f"\n🎉 {heroi.nome} derrotou Akaza, a Lua Superior Três!")
        pausa("Você se torna um Pilar (Hashira) da Corporação dos Caçadores!")
        heroi.ganhar_experiencia(300)
        print("\n🏆 Fim da Jornada. Você se tornou uma lenda entre os caçadores.")
    else:
        fim_de_jogo(heroi)

def batalha(heroi, inimigo):
    while heroi.esta_vivo() and inimigo.esta_vivo():
        print(f"\n{heroi.nome}: {heroi.vida} HP | {inimigo.nome}: {inimigo.vida} HP")
        print("1. Atacar")
        print("2. Usar Poção")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            heroi.atacar(inimigo)
        elif acao == "2":
            usar_pocao(heroi)
        else:
            print("Ação inválida.")

        if inimigo.esta_vivo():
            inimigo.atacar(heroi)


def usar_pocao(heroi):
    for item in heroi.inventario:
        if item.nome.startswith("Poção"):
            heroi.vida += 30
            heroi.inventario.remove(item)
            print(f"{heroi.nome} usou {item.nome}. Vida atual: {heroi.vida}")
            return
    print("Você não tem poções disponíveis!")


def fim_de_jogo(heroi):
    print(f"\n💀 {heroi.nome} foi derrotado... o ciclo da noite continua.")
    print("⚔️ Fim de jogo.")


if __name__ == "__main__":
    main()