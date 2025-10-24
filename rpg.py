from itens.item import Item
from itens.arma import Arma
from itens.protecao import Protecao
from personagens.protagonista import Protagonista
from personagens.inimigo import Inimigo


def mostrar_introducao():
    print("==============================================")
    print("              RESIDENT EVIL VILLAGE")
    print("==============================================")
    print("Sua filha, Rose, foi sequestrada. Sua busca te levou a um vilarejo isolado e coberto por neve...")
    print("Você acorda após um acidente, sozinho e desarmado. Ouve uivos à distância.")
    print("\nSeu único objetivo: sobreviver e encontrar Rose.")

def iniciar_jogo():
    protagonista = Protagonista("Ethan Winters", 100, 9, 7)
    
    inimigo_basico = Inimigo("Lycan", 50, 10, 5)
    
    inimigo_chefe = Inimigo("Lady Dimitrescu", 350, 65, 20)

    faca = Arma(nome="Faca de sobrevivencia", dano = 5)
    arma = Arma(nome="Pistola LEMI", dano = 12)
    
    erva = Item(nome="Erva Verde", descricao="Restaura 25 de vida.")

    print(f"\n{protagonista.nome} encontra uma {arma.nome}, uma {faca.nome} e uma {erva.nome}.")

    protagonista.inventario.append(faca)
    protagonista.inventario.append(arma)
    protagonista.inventario.append(erva)
    
    protagonista.equipar_item(arma)
    protagonista.equipar_item(faca)

    print(f"\n{protagonista.nome} começa a explorar os locais em busca de sua filha Rose.")
    print(f"\n{protagonista.nome} enquanto procurava pistas para encontrar sua filha, escutou barulhos muito assustadores, vindo de um quarto escuro.")

    print(f"\n{protagonista.nome}caminhou até esse quarto para descobrir o que estava fazendo esse barulho. Quando ele chegou lá, encontrou um{inimigo_basico.nome} e começaram uma luta")
    while protagonista.esta_vivo() and inimigo_basico.esta_vivo():
        protagonista.atacar(inimigo_basico)
        if inimigo_basico.esta_vivo():
            inimigo_basico.atacar(protagonista)
