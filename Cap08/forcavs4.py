#POO Capitulo 8 - hangman

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

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

#Classe
class Hangman:

   #método construtor
   def __init__(self, palavra):
      
      self.palavra = palavra
      self.letras_escolhidas = []
      self.letras_erradas = []

   #método para adivinhar a letra
   def guess(self, letra):

      if letra in self.palavra and letra not in self.letras_escolhidas:
         self.letras_escolhidas.append(letra)

      elif letra not in self.palavra and letra not in self.letras_erradas:
         self.letras_erradas.append(letra)

      else:
         return False

      return True

   #método para verificar se o jogo terminou
   def hangman_over(self):
      return self.hangman_won() or (len(self.letras_erradas)==6)

   #método para verificar se o jogador venceu
   def hangman_won(self):
      if "_" not in self.hide_palavra():
         return True
      return False

   #método para não mostrar a letra no tabuleiro
   def hide_palavra(self):
      rtn=''

      for letra in self.palavra:
         if letra not in self.letras_escolhidas:
            rtn+='_'
         else:
            rtn+=letra
      return rtn

   #método para checar o status do game e imprimir o board na tela
   def print_game_status(self):
      print(board[len(self.letras_erradas)])
      print('\nPalavra: '+self.hide_palavra())
      print('\nLetras erradas: ',)

      for letra in self.letras_erradas:
         print(letra,)

      print()
      print('Letras corretas: ',)

      for letra in self.letras_escolhidas:
         print(letra,)
      
      print()

#método para ler uma palavra de forma aleatória
def rand_palavra():
   arquivo=open("frutas.txt", "r")
   palavras=arquivo.read().split('\n')
   arquivo.close()

   #Escolhe a palavra randomicamente
   palavra=random.choice(palavras)

   return palavra

#método para checar se usuário digitou uma letra
#Checa se é letra
def askstr(user_input):
   while True:
      if user_input.isalpha():
         break
      else:
         print("Isso não é uma letra. Tente novamente")
         user_input=input('\nDigite uma letra: ')

#método main de execução do programa
def main():

   limpa_tela()

   #cria o objeto e seleciona uma palavra randomicamente
   game=Hangman(rand_palavra())

   #enquento o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caractere
   while not game.hangman_over():

      #status do game
      game.print_game_status()

      #recebe input do terminal
      user_input=input('\nDigite uma letra: ')

      #checa se é letra
      askstr(user_input)

      #verifica se a letra faz parte da palavra
      game.guess(user_input)

   #verifica o status do jogo
   game.print_game_status()

   #de acordo com o status, imprime mensagem na tela para o usuário
   if game.hangman_won():
      print('\nParabéns! Você venceu!!')
   else:
      print('Game over! Você perdeu!!')
      print('A palavra era '+game.palavra)
   print('\nFoi bom jogar com você! Agora vá estudar\n')

#executa o programa
if __name__=="__main__":
   main()


