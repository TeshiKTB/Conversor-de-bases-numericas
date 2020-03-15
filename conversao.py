# coding: utf-8

"""Programa para conversão entre bases, converte apenas inteiros não negativos"""

numbers = "0123456789ABCDEF"

def eh_num( n ):
	"""Verifica se n é um número inteiro"""
	try:
		int(n)
		return True
	except:
		return False


def eh_num_base( n, b ):
	"""Verifica se n é um número de base b""" 
	for l in n:
		if l not in numbers[:b]:
			return False
	return True


def base_valida( n ):
	print(int(n))
	return True if 2 <= int(n) and int(n) <= 16 else False


def converte_p_decimal( n_str, b ):
	"""Recebe um numero n_str na base b e o converte para decimal"""
	f = 0
	n_str = n_str[::-1]
	for i in range(len(n_str)):
		f += numbers.find(n_str[i]) * (b ** i)
	return f


def decimal_p_base( dec, b ):
	"""Converte o inteiro decimal dec para o inteiro na base b"""
	final = ""
	if dec == 0:
		return "0"

	while dec > 0:
		final += numbers[dec % b]
		dec = dec // b

	return final[::-1]


# Início do programa
while True:

	"""Pedindo e verificando base inicial"""
	b_inicial = input("De qual base deseja converter? Digite o inteiro correspondente (Máximo 16): ")
	while not eh_num(b_inicial) or not base_valida(b_inicial):
		print("Base inválida.")
		print("\n\n")
		b_inicial = input("De qual base deseja converter? Digite o inteiro correspondente (Máximo 16): ")
	b_inicial = int(b_inicial)

	"""Pedindo e verificando numero inicial"""
	num_inicial = input("Qual número será convertido? Digite o inteiro correspondente: ")
	while not eh_num_base(num_inicial, b_inicial):
		print("Número inválido.")
		print("\n\n")
		num_inicial = input("Qual número será convertido? Digite o inteiro correspondente: ")

	"""Pedindo e verificando base final"""
	b_final = input("Para qual base deseja converter? Digite o inteiro correspondente: ")
	while not eh_num(b_final) or not base_valida(b_final):
		print("Base inválida.")
		print("\n\n")
		b_final = input("Para qual base deseja converter? Digite o inteiro correspondente: ")
	b_final = int(b_final)

	"""Processo de conversão -> b_inicial para decimal e decimal para b_final, nessa ordem"""
	num_final = decimal_p_base(converte_p_decimal(num_inicial, b_inicial), b_final)
	
	"""Mostra resposta"""
	print("=" * 50)
	print("Convertendo o número {} ({}) para a base ({}), obtemos: {}".format(num_inicial, b_inicial, b_final, num_final))

	"""Verifica se o usuário deseja converter outro número"""
	resp = input("Deseja converter outro número? [S/N] ").lower()
	while resp not in "sn":
		print("Resposta inválida.")
		resp = input("Deseja converter outro número? [S/N] ").lower()

	if resp == 'n':
		print("Encerrando programa.")
		break
	else:
		print("\n" * 15)