#Create a program that reads the name of a city and says whether or not it begins with the name “SANTO”.

city = str(input('Em qual cidade você nasceu?')).strip()
print(city.upper().startswith('SANTO'))
