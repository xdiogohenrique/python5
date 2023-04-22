#Exercicio Operadores matemáticos 

import math

a = int(input("Insira o valor de A:"))
b = int(input("Insira o valor de B:"))
c = int(input("Insira o valor de C:"))

delta = b*b - 4*a*c 

x1 = (-b + math.sqrt(delta)) /2*a
x2 = (-b - math.sqrt(delta)) /2*a

print("A primeira raiz é: ", x1)

print("A segunda raiz é: ", x2)