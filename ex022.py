#Create a program that reads a person's full name and displays: – The name with all upper and lower case letters. – How many letters in total (without considering spaces). – How many letters are in the first name.

nome = str(input('Digite seu nome completo:')).strip()
print('Analisanto seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0] , len(separa[0])))
