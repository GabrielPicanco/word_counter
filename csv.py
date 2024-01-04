import os
from unidecode import unidecode


os.chdir(r"C:\Users\gabri\Área de Trabalho")

with open('texto.txt', 'r') as arquivo:
    pontuacao = [',','.','!','?','-','_']
    string = str(arquivo.read())
    print(string)
    for caractere in string:
        if caractere in pontuacao:
            string = string.replace(caractere, ' ')
    for letra in string:
        string = string.replace(letra, unidecode(letra))
    print(string)

    lista = string.split()
    print(lista)