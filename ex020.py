#The same teacher from challenge 19 wants to draw lots for the order in which the students will present their work. Write a program that reads the names of the four students and shows the order drawn.

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str (input('Quarto aluno: '))
lista = [n1 , n2 , n3 , n4]
shuffle(lista)
print ('A ordem de apresentação será ')
print(lista)
