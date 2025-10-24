from itens.item import Item
from itens.arma import Arma
from itens.protecao import Armadura
from personagens.protagonista import Protagonista
from personagens.inimigo import Inimigo
import time

def mostrar_introducao():
    print("==============================================")
    print("              RESIDENT EVIL VILLAGE")
    print("==============================================")
    print("Sua filha, Rose, foi sequestrada. Sua busca te levou a um vilarejo isolado, mal-assombrado e coberto por neve...")
    print("Você acorda após um acidente, sozinho e desarmado. Ouve uivos à distância.")
    print("\nSeu único objetivo: sobreviver e encontrar Rose.")

def iniciar_jogo():
    protagonista = Protagonista("Ethan Winters", 100, 11, 8)
    
    inimigo_basico = Inimigo("Lycan", 50, 8, 5)
    inimigo_chefe = Inimigo("Lady Dimitrescu", 180, 19, 5)

    faca = Arma(nome="Faca de sobrevivencia", dano=6)
    arma = Arma(nome="Pistola LEMI", dano=12)
    erva = Item(nome="Erva Verde", descricao="Restaura 25 de vida.")

    print(f"\n{protagonista.nome} encontra uma {faca.nome} e uma {erva.nome}.")
    time.sleep(3)

    protagonista.inventario.append(faca)
    protagonista.inventario.append(arma)
    protagonista.inventario.append(erva)
    
    protagonista.equipar_item(arma)
    protagonista.equipar_item(erva)
    
    print(f"\n{protagonista.nome} começa a explorar os locais em busca de sua filha Rose.")
    time.sleep(3)

    print(f"\n{protagonista.nome} enquanto procurava pistas para encontrar sua filha, escutou barulhos muito assustadores, vindo de um quarto escuro.")
    time.sleep(3)

    print(f"\n{protagonista.nome} caminhou até esse quarto para descobrir o que estava fazendo esse barulho. Quando {protagonista.nome} chegou lá, encontrou um {inimigo_basico.nome} e começaram uma luta!")
    time.sleep(3)

    while protagonista.esta_vivo() and inimigo_basico.esta_vivo():
        protagonista.atacar(inimigo_basico)
        time.sleep(2)
        if inimigo_basico.esta_vivo():
            inimigo_basico.atacar(protagonista)
            time.sleep(2)

    if protagonista.esta_vivo():
        print(f"\n{protagonista.nome} derrotou o {inimigo_basico.nome}!")
        time.sleep(3)
        print(f"\n{protagonista.nome} ficou muito machucado após a luta, ele usa a {erva.nome} para se recuperar.")
        time.sleep(3)
        
        protagonista.vida += 25
        if protagonista.vida > 100:
            protagonista.vida = 100
        protagonista.inventario.remove(erva)
        
        print(f"Vida de {protagonista.nome} foi restaurada para: {protagonista.vida}")
        time.sleep(3)
        
        print(f"\n{protagonista.nome} explora novos locais até achar um castelo antigo e parecendo ser abandonado.")
        time.sleep(3)

    print(f"\n{protagonista.nome} consegue entrar no castelo e escuta um choro, parecendo o choro de sua filha, e do mesmo lugar, {protagonista.nome} escuta uma voz de uma mulher falando com a criança.")
    time.sleep(4)
    print(f"\n{protagonista.nome} corre até o local e encontra sua filha no colo de uma mulher, {protagonista.nome} fala para a mulher soltar sua filha e devolver pra ele.")
    time.sleep(4)
    print(f"\n{protagonista.nome} descobre que a mulher é nada mais nada menos que {inimigo_chefe.nome}, dona do castelo e do vilarejo inteiro. Ela levanta brava e eles começam uma luta")
    time.sleep(3)

    while protagonista.esta_vivo() and inimigo_chefe.esta_vivo():
        protagonista.atacar(inimigo_chefe)
        time.sleep(2)
        if inimigo_chefe.esta_vivo():
            inimigo_chefe.atacar(protagonista)
            time.sleep(2)

    if protagonista.esta_vivo():  
        print(f"\n{protagonista.nome} derrotou a {inimigo_chefe.nome}!")
        time.sleep(3)
        print(f"{protagonista.nome} consegue derrotar Lady Dimitrescu e recuperar sua filha Rose. Eles voltam para casa a salvos!")
        time.sleep(3)
        print("\nFim de Jogo!")
    else:
        print(f"\n{protagonista.nome} foi derrotado... A busca por Rose chegou a um fim trágico.")
        print("\nFim de Jogo!")

mostrar_introducao()
iniciar_jogo()