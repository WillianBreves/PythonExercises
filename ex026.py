#Make a program that reads a sentence from the keyboard and shows how many times the letter “A” appears, in which position it appears the first time and in which position it appears the last time.

frase = str(input('Digite aqui uma frase qualquer:')).strip()
print('A frase digitada contém {} letras A'.format(frase.upper().count('A')))
print('E a primeira letra A está na posição {}'.format(frase.find('A')+1))
print('A última letra A está na posição {}'.format(frase.rfind('A')+1))
