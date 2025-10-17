
from personagens.heroi import Heroi
from personagens.monstro import Monstro
from itens.arma import Arma
from itens.armadura import Armadura


class Veiculo:
	def __init__(self, nome, velocidade, preco):
		self.nome = nome
		self.velocidade = velocidade
		self.preco = preco


def criar_heroi():
	nome = input("Escolha o nome do seu personagem: ")
	heroi = Heroi(nome=nome, vida=100, ataque=10, defesa=5)
	# itens iniciais
	faca = Arma("Faca", "Uma faca pequena.", bonus_ataque=3)
	jaqueta = Armadura("Jaqueta", "Jaqueta de couro.", bonus_defesa=1)
	heroi.inventario.append(faca)
	heroi.inventario.append(jaqueta)
	heroi.dinheiro = 100
	heroi.veiculo = None
	return heroi
if monstro(nivel=1, tipo='Bandido'):
	return Monstro(nome=f"{tipo} N{nivel}", vida=20 + nivel * 10, ataque=5 + nivel * 2, defesa=1 + nivel, tipo=tipo)


def mostrar_status(heroi):
	print(f"\n--- STATUS de {heroi.nome} ---")
	print(f"Vida: {heroi.vida} | Ataque: {heroi.ataque} | Defesa: {heroi.defesa} | Nivel: {heroi.nivel} | XP: {heroi.experiencia}")
	print(f"Dinheiro: ${heroi.dinheiro}")
	if heroi.veiculo:
		print(f"Veículo: {heroi.veiculo.nome} (vel {heroi.veiculo.velocidade})")
	print("Inventário:")
	for i, it in enumerate(heroi.inventario, 1):
		print(f"  {i}. {it.nome} - {getattr(it, 'descricao', '')}")


def combate(heroi, monstro):
	print(f"\nComeça o combate: {heroi.nome} vs {monstro.nome}")
	while heroi.esta_vivo() and monstro.esta_vivo():
		scelta = input("Escolha: (a) atacar  (f) fugir: ").strip().lower()
		if scelta == 'a':
			heroi.atacar(monstro)
			if monstro.esta_vivo():
				monstro.atacar(heroi)
		elif scelta == 'f':
			print("Você fugiu do combate!")
			return False
		else:
			print("Entrada inválida. Digite 'a' para atacar ou 'f' para fugir.")
			continue
	if heroi.esta_vivo():
		print(f"{heroi.nome} venceu {monstro.nome}!")
		heroi.ganhar_experiencia(20)
		heroi.dinheiro += 20
		return True
	else:
		print("Você foi derrotado. Voltando ao hospital (vida parcial restaurada).")
		heroi.vida = max(10, heroi.vida)
		heroi.dinheiro = max(0, heroi.dinheiro - 30)
		return False


def loja(heroi):
	carros = [Veiculo("Moto", 60, 80), Veiculo("Carro", 90, 200), Veiculo("Helicóptero", 200, 1000)]
	armas = [Arma("Pistola", "Arma de fogo.", 8), Arma("Rifle", "Rifle automático.", 15)]
	armaduras = [Armadura("Colete", "Proteção leve.", 3), Armadura("Colete Pesado", "Proteção alta.", 6)]

	while True:
		print("\n--- LOJA ---")
		print("1. Comprar veículo")
		print("2. Comprar arma")
		print("3. Comprar armadura")
		print("4. Sair")
		op_raw = input("Escolha: ").strip()
		# parse numeric selection
		try:
			op = int(op_raw)
		except ValueError:
			print("Opção inválida.")
			continue
		if op == 1:
			for i, c in enumerate(carros, 1):
				print(f"{i}. {c.nome} - Vel {c.velocidade} - ${c.preco}")
			idx = input("Escolha veículo (número) ou 0 para cancelar: ")
			if idx.isdigit() and int(idx) > 0:
				sel = int(idx)
				if sel <= len(carros):
					c = carros[sel-1]
					if heroi.dinheiro >= c.preco:
						heroi.dinheiro -= c.preco
						heroi.veiculo = c
						print(f"Você comprou {c.nome}!")
					else:
						print("Dinheiro insuficiente.")
				else:
					print("Seleção inválida.")
		elif op == 2:
			for i, a in enumerate(armas, 1):
				print(f"{i}. {a.nome} - {a.descricao} - Bônus: {a.bonus_ataque} - ${50 + i*30}")
			idx = input("Escolha arma (número) ou 0 para cancelar: ")
			if idx.isdigit() and int(idx) > 0:
				sel = int(idx)
				if sel <= len(armas):
					a = armas[sel-1]
					price = 50 + sel*30
					if heroi.dinheiro >= price:
						heroi.dinheiro -= price
						heroi.inventario.append(a)
						print(f"Você comprou {a.nome}!")
					else:
						print("Dinheiro insuficiente.")
				else:
					print("Seleção inválida.")
		elif op == 3:
			for i, ar in enumerate(armaduras, 1):
				print(f"{i}. {ar.nome} - {ar.descricao} - Bônus: {ar.bonus_defesa} - ${40 + i*25}")
			idx = input("Escolha armadura (número) ou 0 para cancelar: ")
			if idx.isdigit() and int(idx) > 0:
				sel = int(idx)
				if sel <= len(armaduras):
					ar = armaduras[sel-1]
					price = 40 + sel*25
					if heroi.dinheiro >= price:
						heroi.dinheiro -= price
						heroi.inventario.append(ar)
						print(f"Você comprou {ar.nome}!")
					else:
						print("Dinheiro insuficiente.")
				else:
					print("Seleção inválida.")
		elif op == 4:
			break
		else:
			print("Opção inválida.")
			continue


def missao(heroi):
	print("\n--- MISSÃO: Roubar um carro de luxo ---")
	dificuldade = 2
	monstro = criar_monstro(nivel=dificuldade)
	sucesso = combate(heroi, monstro)
	if sucesso:
		print("Missão completada: você conseguiu o carro e ganhou $200")
		heroi.dinheiro += 200
		heroi.ganhar_experiencia(50)


def menu_principal(heroi):
	while True:
		mostrar_status(heroi)
		print("\nO que deseja fazer?")
		print("1. Andar pela cidade (encontrar bandidos)")
		print("2. Fazer missão")
		print("3. Visitar loja")
		print("4. Equipar item do inventário")
		print("5. Sair do jogo")
		escolha_raw = input("Escolha: ").strip()
		# try parse integer choice
		try:
			escolha_num = int(escolha_raw)
		except ValueError:
			escolha_num = None
		try:
			if escolha_num == 1:
				print("Você saiu para andar pela cidade...")
				mon = criar_monstro(nivel=1)
				combate(heroi, mon)
			elif escolha_num == 2:
				print("Iniciando missão...")
				missao(heroi)
			elif escolha_num == 3:
				loja(heroi)
			elif escolha_num == 4:
				if not heroi.inventario:
					print("Inventário vazio.")
					continue
				for i, it in enumerate(heroi.inventario, 1):
					print(f"{i}. {it.nome}")
				idx = input("Escolha item para equipar (número) ou 0 para cancelar: ").strip()
				if idx.isdigit() and int(idx) > 0:
					sel = int(idx)
					if 1 <= sel <= len(heroi.inventario):
						heroi.equipar_item(heroi.inventario[sel-1])
					else:
						print("Seleção inválida.")
			elif escolha_num == 5:
				print("Saindo...")
				break
			else:
				print("Opção inválida. Digite um número entre 1 e 5.")
		except Exception as e:
			print(f"Ocorreu um erro: {e}. Tente novamente.")


def main():
	print("Bem-vindo ao GTA-lite em modo texto!")
	heroi = criar_heroi()
	menu_principal(heroi)


if __name__ == '__main__':
	main()

