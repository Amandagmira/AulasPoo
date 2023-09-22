'''Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo.'''
num1 = int(input("Escreve um ínicio:"))
num2 = int(input("Escreve um fim:"))
num3 = int(input("Escreva um número:"))
if num3 >= num1 and num3 <= num2:
    print("Está dentro do intervalo!")
else:
    print("Está fora do intervalo :c")