import os

from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta do dispositivo:')
os.chdir(caminho)


def line():
    print('-'*60)


print('Você está neste caminho: \033[32m{}\033[m'.format(caminho))
formatos = ['.txt']
while True:
    line()
    nome_arquivo = str(input('Digite o nome do arquivo .txt: '))
    if os.path.exists(nome_arquivo):
        print('\033[32mEsse arquivo existe nesse caminho\033[m')
        line()
        nome, formato = os.path.splitext(nome_arquivo)
        if formato in formatos:
            opcoes = [1,2]
            while True:
                try:
                    ask = int(input('''Digite 1 para contar todas as palavras do texto
Digite 2 para contar quantas vezes aparece uma palavra específica
Digite sua opção: '''))
                except ValueError:
                    line()
                    print('\033[31mErro: Essa opção não existe\033[m')
                else:
                    if ask in opcoes:
                        break
                    else:
                        line()
                        print('\033[31mErro: Essa opção não existe\033[m')

            if ask == opcoes[0]:
                with open(nome_arquivo, 'r') as arquivo:
                    string = str(arquivo.read())
                    pontuacao = [',','.',':','!','?','-','_']
                    for caractere in string:
                        if caractere in pontuacao:
                            string = string.replace(caractere, ' ')
                    lista_palavras = string.split()
                    line()
                    print('O arquivo de texto "{}" tem um total de {} palavras.'.format(nome_arquivo,len(lista_palavras)))
                    break
            if ask == opcoes[1]:
                line()
                palavra = str(input('Digite a palavra que quer contar no texto: '))
                with open(nome_arquivo, 'r') as arquivo:
                    string = str(arquivo.read())
                    lista_palavras = string.split()
                    line()
                    print('A palavra "{}" aparece {} vezes no arquivo "{}".'.format(palavra,lista_palavras.count(palavra), nome_arquivo))
                    print(lista_palavras)
                    break
        else:
            print('\033[31mMas esse não é um arquivo txt, tente novamente.\033[m')
    else:
        print('Esse arquivo não existe nesse caminho.')

