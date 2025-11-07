from itens.item import Item
from itens.arma import Arma
from itens.protecao import Armadura
from personagens.protagonista import Protagonista
from personagens.inimigo import Inimigo
import time
import sys

class Item:
    def __init__(self, nome, descricao, efeito_cura=0):
        self.nome = nome
        self.descricao = descricao
        self.efeito_cura = efeito_cura

    def __str__(self):
        return self.nome
        
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.nome == other.nome
        return NotImplemented

class Arma(Item):
    def __init__(self, nome, dano):
        super().__init__(nome, f"Dano: {dano}")
        self.dano = dano

class Armadura(Item):
    def __init__(self, nome, defesa):
        super().__init__(nome, f"Defesa: {defesa}")
        self.defesa = defesa
        
class Personagem:
    def __init__(self, nome, vida, ataque_base, defesa_base):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.ataque_base = ataque_base
        self.defesa_base = defesa_base
        self.inventario = []

    def esta_vivo(self):
        return self.vida > 0

    def calcular_dano(self):
        return self.ataque_base

    def receber_dano(self, dano_recebido):
        dano_final = max(0, dano_recebido - self.defesa_base)
        self.vida -= dano_final
        if self.vida < 0: self.vida = 0

    def atacar(self, alvo):
        dano = self.calcular_dano()
        alvo.receber_dano(dano)
        print(f"🗡️ {self.nome} ataca {alvo.nome} causando {dano} de dano!")
        print(f"❤️ Vida de {alvo.nome}: {alvo.vida}/{alvo.vida_maxima}")

class Protagonista(Personagem):
    def __init__(self, nome, vida, ataque_base, defesa_base):
        super().__init__(nome, vida, ataque_base, defesa_base)
        self.arma_equipada = None
        self.armadura_equipada = None
        
        self.municao_pistola = 15
        self.faca = Arma(nome="Faca de sobrevivencia", dano=6)

    def equipar_item(self, item):
        
    
        if isinstance(item, Arma):
            self.arma_equipada = item
            print(f"🛠️ {self.nome} equipou {item.nome}.")
    
    def calcular_dano(self):
        dano = self.ataque_base
        if self.arma_equipada:
            dano += self.arma_equipada.dano
        return dano

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque_base, defesa_base):
        super().__init__(nome, vida, ataque_base, defesa_base)


def criar_instancia_item(nome):
    if nome == "Erva Verde":
        return Item(nome="Erva Verde", descricao="Restaura 25 de vida.", efeito_cura=25)
    if nome == "Químico":
        return Item(nome="Químico", descricao="Pode ser combinado com ervas.")
    if nome == "Primeiros Socorros":
        return Item(nome="Primeiros Socorros", descricao="Restaura 75 de vida.", efeito_cura=75)

    return Item(nome, "Item genérico.")
    
     

def menu_item_consumivel(protagonista):
    
    itens_consumiveis = [item for item in protagonista.inventario if item.efeito_cura > 0]
    
    if not itens_consumiveis:
        print("❌ Inventário vazio de itens de cura.")
        time.sleep(1)
        return False 

    print("\n--- 💊 Itens de Cura ---")
    for i, item in enumerate(itens_consumiveis):
        print(f"[{i + 1}] {item.nome} ({item.descricao})")
    print("[0] Voltar ao combate")

    while True:
        escolha = input("Escolha o item para usar: ")
        if escolha.isdigit():
            escolha_int = int(escolha)
            
            if escolha_int == 0:
                return False 
            
            elif 1 <= escolha_int <= len(itens_consumiveis):
                item_escolhido = itens_consumiveis[escolha_int - 1]
                
                cura = item_escolhido.efeito_cura
                protagonista.vida += cura
                if protagonista.vida > protagonista.vida_maxima:
                    protagonista.vida = protagonista.vida_maxima
                
                protagonista.inventario.remove(item_escolhido)
                print(f"✅ {protagonista.nome} usou {item_escolhido.nome} e restaurou {cura} de vida!")
                print(f"❤️ Vida atual: {protagonista.vida}/{protagonista.vida_maxima}")
                time.sleep(2)
                return True 
            
            else:
                print("Escolha inválida. Tente novamente.")
        else:
            print("Entrada inválida. Digite o número da opção.")


def menu_combate(protagonista, inimigo):

    print("[1] Atacar (Pistola)") 
    print(f"    (Dano: {protagonista.calcular_dano()}, Balas: {protagonista.municao_pistola})")
    print("[2] Atacar (Faca)")
    print(f"    (Dano: {protagonista.faca.dano})")
    print("[3] Usar Item (Cura)")

    while True:
        acao = input("Escolha sua ação: ")

        if acao == '1': 
            if protagonista.municao_pistola > 0:
                protagonista.municao_pistola -= 1
                protagonista.atacar(inimigo) 
                print(f" {protagonista.municao_pistola} balas restantes.")
                return True
            else:
                print("❌ SEM MUNIÇÃO! Você precisa usar a faca ou fugir.")
                time.sleep(1)
                continue 
        elif acao == '2': 
            
            dano_faca = protagonista.faca.dano
            inimigo.receber_dano(dano_faca)
            print(f"🔪 {protagonista.nome} ataca {inimigo.nome} com a faca, causando {dano_faca} de dano!")
            print(f"❤️ Vida de {inimigo.nome}: {inimigo.vida}/{inimigo.vida_maxima}")
            return True

        elif acao == '3': 
            if menu_item_consumivel(protagonista):
                return True 
            else:
                continue 

        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


def simular_combate(protagonista, inimigo):
    
    print(f"\n📢 INÍCIO DO COMBATE CONTRA {inimigo.nome.upper()}!")
    time.sleep(1)

    while protagonista.esta_vivo() and inimigo.esta_vivo():
        
        if protagonista.esta_vivo():
            menu_combate(protagonista, inimigo)
            time.sleep(1)

        if not inimigo.esta_vivo():
            break

        if inimigo.esta_vivo():
            inimigo.atacar(protagonista)
            time.sleep(2)

        if not protagonista.esta_vivo():
            break

    return protagonista.esta_vivo()


def mostrar_introducao():
    print("==============================================")
    print("           RESIDENT EVIL VILLAGE              ")
    print("==============================================")
    print("Sua filha, Rose, foi sequestrada. Sua busca te levou a um vilarejo isolado, mal-assombrado e coberto por neve...")
    print("Você acorda após um acidente, sozinho e desarmado. Ouve uivos à distância.")
    print("\nSeu único objetivo: sobreviver e encontrar Rose.")

def iniciar_jogo():
    
    protagonista = Protagonista("Ethan Winters", 100, 11, 8)
    protagonista.vida_maxima = 100
    
    inimigo_basico = Inimigo("Lycan", 50, 11, 5)
    inimigo_basico.vida_maxima = 50
    inimigo_chefe = Inimigo("Lady Dimitrescu", 140, 19, 5)
    inimigo_chefe.vida_maxima = 140

    faca = Arma(nome="Faca de sobrevivencia", dano=6)
    arma = Arma(nome="Pistola LEMI", dano=12)
    erva = criar_instancia_item(nome="Erva Verde")

    print(f"\n{protagonista.nome} encontra uma {faca.nome} e uma {erva.nome}.")
    time.sleep(3)

    protagonista.inventario.append(faca)
    protagonista.inventario.append(arma)
    protagonista.inventario.append(erva)
    
    protagonista.equipar_item(arma)
    
    print(f"\n{protagonista.nome} começa a explorar os locais em busca de sua filha Rose.")
    time.sleep(3)

    print(f"\n{protagonista.nome} enquanto procurava pistas para encontrar sua filha, escutou barulhos muito assustadores, vindo de um quarto escuro.")
    time.sleep(3)

    print(f"\n{protagonista.nome} caminhou até esse quarto para descobrir o que estava fazendo esse barulho. Quando {protagonista.nome} chegou lá, encontrou um {inimigo_basico.nome} e começaram uma luta!")
    time.sleep(3)

    protagonista_venceu_lycan = simular_combate(protagonista, inimigo_basico)

    if protagonista_venceu_lycan:
        print(f"\n{protagonista.nome} derrotou o {inimigo_basico.nome}!")
        time.sleep(3)
        
        print("💪 Ethan continua em frente, explorando a área.")
        time.sleep(3)
        
        print(f"\n{protagonista.nome} explora novos locais até achar um castelo antigo e parecendo ser abandonado.")
        time.sleep(3)

        print(f"\n{protagonista.nome} consegue entrar no castelo e escuta um choro, parecendo o choro de sua filha, e do mesmo lugar, {protagonista.nome} escuta uma voz de uma mulher falando com a criança.")
        time.sleep(4)
        print(f"\n{protagonista.nome} corre até o local e encontra sua filha no colo de uma mulher, {protagonista.nome} fala para a mulher soltar sua filha e devolver pra ele.")
        time.sleep(4)
        print(f"\n{protagonista.nome} descobre que a mulher é nada mais nada menos que {inimigo_chefe.nome}, dona do castelo e do vilarejo inteiro. Ela levanta brava e eles começam uma luta")
        time.sleep(3)

        protagonista_venceu_chefe = simular_combate(protagonista, inimigo_chefe)

        if protagonista_venceu_chefe: 
            print(f"\n{protagonista.nome} derrotou a {inimigo_chefe.nome}!")
            time.sleep(3)
            print(f"{protagonista.nome} consegue derrotar Lady Dimitrescu e recuperar sua filha Rose. Eles voltam para casa a salvos!")
            time.sleep(3)
            print("\nFim de Jogo!")
        else:
            print(f"\n{protagonista.nome} foi derrotado por Lady Dimitrescu...")
            print("\nFim de Jogo!")
    else:
        print(f"\n{protagonista.nome} foi derrotado pelo Lycan na vila...")
        print("\nFim de Jogo!")

mostrar_introducao()
iniciar_jogo()