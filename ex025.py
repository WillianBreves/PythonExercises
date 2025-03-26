#Create a program that reads a person's name and tells you if they have “SILVA” in their name.

name = str(input('Qual é o seu nome?')).strip()
print('O nome contém Silva? {}'.format('SILVA' in name.upper())) 
