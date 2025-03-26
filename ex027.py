#Make a program that reads a person's full name, then displays the first and last name separately.

name = str(input('Digite aqui seu nome completo:')).strip().split()
lista = [name]
print('Prazer em te conhecer, {}'.format(name[0]))
print('O seu primeiro nome é {}'.format(name[0]))
print('E seu último nome é {}'.format(name[len(name)-1]))
