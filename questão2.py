""" Escreva um algoritmo que solicite que o usuário digite o valor de
duas notas e armazene o resultado em duas variáveis diferentes (tipo
real);
Calcule o resultado da média desses valores;
Imprima “Você está em RECUPERAÇÃO!!!” caso o resultado da média
seja maior ou igual a 30 e menor do que 70. """

nota1 = float(input("Dígite o sua primeiro nota:"))
nota2 = float(input("Dígite o sua segundo nota:"))

media = (nota1 + nota2/2)
print(media)
if media >= 30 and media < 70:
    print ("Você está de RECUPERAÇÃO!!!!!")
elif media < 30:
    print ("Você está REPROVADO!!")
else:
    print ("Você está APROVADO!!!")