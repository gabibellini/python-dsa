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

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

#Função recebe o conteúdo do game
def game():

	limpa_tela()
	print("\nBem-vindo(a) ao jogo da forca!")
	print("Adivinha a palavra abaixo:\n")

	#Lista de palavras de um arquivo txt
	import os
	arquivo=open("frutas.txt", "r") 
	palavras=arquivo.read().split('\n')
	arquivo.close()

	#Escolhe a palavra randomicamente
	palavra=random.choice(palavras)

	# Lista  de letras  da palavra
	lista_letras_palavras = [letra for letra in palavra]

	# Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
	tabuleiro = ["_"] * len(palavra)

	#Número de chances
	chances=6

	#Lista para letras digitadas
	letras_tentativas=[]

	#Loop enquanto o número de chances for maior do que zero
	while chances>0:

		#Print
		print(display_hangman(chances))
		print("Palavra: ", tabuleiro)
		print("\n")

		#Tentativa
		tentativa=input("\nDigite uma letra: ").lower()

		#Checa se é letra
		def askstr():
			while True:
				tentativa = input("\nDigite uma letra: ").lower()
				if tentativa.isalpha():
					break
				else:
					print("Isso não é uma letra. Tente novamente.")

		#Condicional
		if tentativa in letras_tentativas:
			print("Você já tentou essa letras. Escolha outra!")
			continue

		#Lista de tentativas
		letras_tentativas.append(tentativa)

		#Condicional
		if tentativa in lista_letras_palavras:
			print("Você acertou a letra!")

			#Loop
			for indice in range(len(lista_letras_palavras)):
				#condicional
				if lista_letras_palavras[indice]==tentativa:
					tabuleiro[indice]=tentativa

			#Se todos os espaços forem preenchidos, o jogo acabou
			if "_" not in tabuleiro:
				print("\nVocê venceu, a palavra era: {}".format(palavra))
				break
		else:
			print("Ops! Essa letra não está na palavra!")
			chances-=1

	#Condicional

	if "_" in tabuleiro:
		print("\nVocê perdeu, a palavra era: {}.".format(palavra))

#Bloco main (indica ao interpretador que é um módulo python)
if __name__ == "__main__":
	game()
	print("\nParabéns. Você está aprendendo programação em python com a dsa. :)\n")
