def apagar_linha(numero_da_linha):
    try:
        with open('teste.txt','r') as arquivo:
            lista_de_linhas = arquivo.readlines()

        linhadel = numero_da_linha

        del lista_de_linhas[linhadel - 1]

        with open('teste.txt','w') as arq:
            arq.writelines(lista_de_linhas)
    except IndexError:
        print('\033[31mERRO: A linha {} não existe ou já foi deletada de seu arquivo\033[m'.format(numero_da_linha))
    else:
        print('Linha {} apagada.'.format(numero_da_linha))


def exibir_arquivo():
    with open('teste.txt','r') as arquivo:
        lista = arquivo.readlines()
        contador = 1
        print('-'*50)
        print('Aqui está seu arquivo:'.center(50))
        print('-'*50)
        for linha in lista:
            print(f'Linha {contador} >>> {linha}')
            contador += 1


def add_ao_arquivo(texto):
    string = str(texto)
    with open('teste.txt','a') as arquivo:
        arquivo.write('\n{}'.format(string))
    print('\033[32mVocê adicionou "{}" ao arquivo.\033[m'.format(string))
