# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!



#apresentar a calculadora e opções 1- soma; 2 - subtração; 3- multiplicação; e 4- divisão
#perguntar a operação
#perguntar o primeiro número
#perguntar o segundo número
#mostrar o resultado
print("\n******************* Calculadora em Python *******************")
print("1- SOMA")
print("2- SUBTRAÇÃO")
print("3- MULTIPLICAÇÃO")
print("4- DIVISÃO")

#poderia ter criado as 4 funções para as operações
#se não quiser usar int no input de opção, pode colocar como string no bloco opcao=="1"
opcao=int(input("Digite qual operação desejada: "))

if opcao==1:
	n1=float(input("Digite o primeiro número: "))
	n2=float(input("Digite o segundo número: "))
	resultado=n1+n2
	print("O resultado da soma é: ", resultado)

elif opcao==2:
	n1=float(input("Digite o primeiro número: "))
	n2=float(input("Digite o segundo número: "))
	resultado=n1-n2
	print("O resultado da subtração é: ", resultado)

elif opcao==3:
	n1=float(input("Digite o primeiro número: "))
	n2=float(input("Digite o segundo número: "))
	resultado=n1*n2
	print("O resultado da multiplicação é: ", resultado)

elif opcao==4:
	n1=float(input("Digite o primeiro número: "))
	n2=float(input("Digite o segundo número: "))
	while n2==0:
		print("Operação inválida pois não existe divisão por zero")
		n2=float(input("Digite o segundo número: "))
	resultado=n1/n2
	print("O resultado da divisão é: ", resultado)

else:
	while opcao !=1 or opcao !=2 or opcao !=3 or opcao !=4:
		print("Operação inválida")
		opcao=int(input("Digite a operação desejada: "))
