#CAPÍTULO 7
#projeto: desenvolvimento de um jogo

#JOGO DA FORCA

#Import
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

	#windows
	if name =='nt':
		_ = system('cls')

	#mac ou linux
	else:
		_ = system('clear')

#Função recebe o conteúdo do game
def game():

	limpa_tela()
	print("\nBem-vindo(a) ao jogo da forca!")
	print("Adivinha a palavra abaixo:\n")

	#Lista de palavras
	palavras=['banana', 'abacate', 'uva', 'morango', 'laranja']

	#Escolhe a palavra randomicamente
	palavra=random.choice(palavras)

	#List comprehension
	letras_descobertas=['_' for letra in palavra] #coloque tracinho para cada letra da palavra

	#Número de chances
	chances=6

	#Lista para letras erradas
	letras_erradas=[]

	#Loop enquanto o número de chances for maior do que zero
	while chances>0:

		#print
		print(" ".join(letras_descobertas))
		print("\nChances restantes:", chances)
		print("Letras erradas:", " ".join(letras_erradas))

		#Tentativa
		tentativa=input("\nDigite uma letra: ").lower()

		#Condicional
		if tentativa in palavra:
			index=0
			for letra in palavra:
				if tentativa==letra:
					letras_descobertas[index]=letra
				index+=1
		else:
			chance-=1
			letras_erradas.append(tentativa)

		#Condicional
		if "_" not in letras_descobertas:
			print("\nVocê veneu, a palavra era:", palavra)

	#Condicional

	if "_" in letras_descobertas:
		print("\nVocê perdeu, a palavra era:", palavra)

#Bloco main (indica ao interpretador que é um módulo python)
if __name__ == "__main__":
	game()
	print("\nParabéns. Você está aprendendo programação em python com a dsa. :)\n")
