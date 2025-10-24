class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        
        base = self.ataque
        defesa_pct = getattr(alvo, 'defesa', 0) / 100.0
        defesa_pct = min(0.95, max(0.0, defesa_pct))
        dano = int(max(0, base * (1.0 - defesa_pct)))
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano (base {base}, defesa {int(defesa_pct*100)}%).")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0