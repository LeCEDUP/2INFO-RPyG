from .personagem import Personagem
from itens.arma import Arma
from itens.armadura import Armadura


class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa, nivel=1, experiencia=0, inventario=None, max_level=50):
        
        super().__init__(nome, vida, ataque, defesa)
        self.max_vida = vida
        self.vida = vida
        self.nivel = nivel
        self.experiencia = experiencia
        self.inventario = inventario if inventario is not None else []
      
        self.arma_equipada = None
        self.armadura_equipada = None
        
        self.max_level = max_level

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} ganhou {exp} de experiência. Total: {self.experiencia}")
     
        while self.nivel < self.max_level:
            need = self.experiencia_para_proximo_nivel()
            if self.experiencia >= need and need > 0:
                self.experiencia -= need
                self.subir_nivel()
            else:
                break

    def subir_nivel(self):
        if self.nivel >= self.max_level:
            print(f"{self.nome} já atingiu o nível máximo ({self.max_level}).")
            return
        self.nivel += 1
       
        self.max_vida += 20
        self.vida = min(self.max_vida, self.vida + 20)
       
        self.ataque += 5
        self.defesa += 2
        print(f"{self.nome} subiu para o nível {self.nivel}! Seus atributos aumentaram.")

    def experiencia_para_proximo_nivel(self):
        """Retorna quantos pontos de experiência faltam para subir ao próximo nível.

        Usa uma curva crescente para exigir mais XP em níveis altos
        (por exemplo 100 * nivel^1.2).
        """
        necessario = int(100 * (self.nivel ** 1.2))
        faltam = necessario - self.experiencia
        return max(0, faltam)

    def equipar_item(self, item):
        if item not in self.inventario:
            print(f"{self.nome} não possui {getattr(item, 'nome', str(item))} no inventário.")
            return

        if isinstance(item, Arma):
          
            if self.arma_equipada is not None:
                antiga = self.arma_equipada
                self.ataque -= antiga.bonus_ataque
                self.inventario.append(antiga)
                print(f"{self.nome} desequipou {antiga.nome}.")
         
            self.arma_equipada = item
            self.ataque += item.bonus_ataque
            try:
                self.inventario.remove(item)
            except ValueError:
                pass
            print(f"{self.nome} equipou {item.nome}. Ataque atual: {self.ataque}")

        elif isinstance(item, Armadura):
            if self.armadura_equipada is not None:
                antiga = self.armadura_equipada
                self.defesa -= antiga.bonus_defesa
                self.inventario.append(antiga)
                print(f"{self.nome} desequipou {antiga.nome}.")
            self.armadura_equipada = item
            self.defesa += item.bonus_defesa
            try:
                self.inventario.remove(item)
            except ValueError:
                pass
            print(f"{self.nome} equipou {item.nome}. Defesa atual: {self.defesa}")

        else:
            print(f"{getattr(item, 'nome', str(item))} não pode ser equipado.")

    def desequipar_arma(self):
        if self.arma_equipada:
            antiga = self.arma_equipada
            self.ataque -= antiga.bonus_ataque
            self.inventario.append(antiga)
            self.arma_equipada = None
            print(f"{self.nome} desequipou {antiga.nome}.")

    def desequipar_armadura(self):
        if self.armadura_equipada:
            antiga = self.armadura_equipada
            self.defesa -= antiga.bonus_defesa
            self.inventario.append(antiga)
            self.armadura_equipada = None
            print(f"{self.nome} desequipou {antiga.nome}.")

    def descartar_item(self, nome_item):
        encontrados = [i for i in self.inventario if i.nome.lower() == nome_item.lower()]
        if encontrados:
            item = encontrados[0]
            try:
                self.inventario.remove(item)
                print(f"{self.nome} descartou {item.nome} do inventário.")
                return True
            except ValueError:
                return False
   
        if self.arma_equipada and self.arma_equipada.nome.lower() == nome_item.lower():
            antiga = self.arma_equipada
            self.ataque -= antiga.bonus_ataque
            self.arma_equipada = None
            print(f"{self.nome} descartou a arma equipada {antiga.nome}.")
            return True
        if self.armadura_equipada and self.armadura_equipada.nome.lower() == nome_item.lower():
            antiga = self.armadura_equipada
            self.defesa -= antiga.bonus_defesa
            self.armadura_equipada = None
            print(f"{self.nome} descartou a armadura equipada {antiga.nome}.")
            return True
        print(f"Item {nome_item} não encontrado no inventário nem equipado.")
        return False

    def atacar(self, alvo):
        """
        Ataque do herói aplica um aumento permanente de dano baseado no nível.
        Assunção: cada nível além do nível 1 concede +5% de dano permanente.
        O cálculo aplica o multiplicador sobre o ataque atual (que inclui bônus de armas).
        """
       
        multiplicador = 1.0 + 0.05 * (self.nivel - 1)
        dano_bruto = int(self.ataque * multiplicador)
        defesa_pct = getattr(alvo, 'defesa', 0) / 100.0
        defesa_pct = min(0.95, max(0.0, defesa_pct))
        dano = int(max(0, dano_bruto * (1.0 - defesa_pct)))
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano (base {dano_bruto}, defesa alvo {int(defesa_pct*100)}%).")