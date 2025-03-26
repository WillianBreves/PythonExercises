#A teacher wants to randomly select one of his four students to erase the board. Write a program that will help him by reading the students' names and writing the name of the chosen one on the screen.

import random
nom1 = str (input('Primeiro aluno: '))
nom2 = str (input('Segundo aluno: '))
nom3 = str (input('Terceiro aluno: '))
nom4 = str (input('Quarto aluno: '))
lista = [nom1, nom2 ,nom3 ,nom4]

print ('O aluno(a) escolhido(a) foi {}'.format(random.choice(lista)))
