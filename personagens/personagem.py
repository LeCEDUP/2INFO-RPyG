class Personagem:
   

    def __init__(self, nome, vida, ataque, defesa):
       
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
    
        dano_causado = self.ataque - alvo.defesa
        
        if dano_causado < 0:
            dano_causado = 1
        
        alvo.vida -= dano_causado
        
        print(f"{self.nome} ataca {alvo.nome} e causa {dano_causado} de dano!")
        
        if alvo.esta_vivo():
            print(f"Vida de {alvo.nome}: {alvo.vida}")
        else:
            print(f"{alvo.nome} foi derrotado.")

    def esta_vivo(self):
      
        return self.vida > 0