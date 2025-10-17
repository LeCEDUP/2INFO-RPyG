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