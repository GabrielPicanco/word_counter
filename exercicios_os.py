import os

caminho = r'C:\Users\gabri\Área de Trabalho\arquivos'
os.chdir(caminho)


def linha():
    print('-'*50)


def ver_arquivos():
    linha()
    print('Você está aqui: {}'.format(os.getcwd()))
    '''Essa função mostra todos os arquivos que existem dentro da pasta base do computador.'''
    contador = 1
    for raiz, pasta, arquivo in os.walk(os.getcwd()):
        lista = arquivo
        if len(lista) > 0:
            linha()
            print('Os arquivos que estão dentro da pasta "{}" são: '.format(os.path.basename(os.getcwd())))
            for c in lista:
                print('{} >>> {}'.format(contador,c))
                contador += 1
            linha()
        else:
            print('\033[31mNão existem arquivos dentro da pasta "{}".\033[m'.format(os.path.basename(os.getcwd())))


def adicionar_diretorio(nome_diretorio):
    os.mkdir(nome_diretorio)
    print('\033[32mVocê adicionou um novo diretório a: "{}"\033[m'.format(os.getcwd()))


def verificar_existencia(caminho):

    if os.path.exists(caminho) == True:
        print('Essa pasta existe.')
    else:
        print('Essa pasta não existe.')


def renomear(nomeantigo,nomenovo):
    try:
        os.rename(nomeantigo,nomenovo)
    except FileNotFoundError:
        print('\033[31mERRO >>> Esse arquivo não foi encontrado, veja se esqueceu do ".txt"\033[m')
    else:
        print('\033[32mVocê mudou o nome do arquivo "{}" para "{}".\033[m'.format(nomeantigo,nomenovo))


def remover_arquivo(nome_do_arquivo):
    try:
        os.remove(nome_do_arquivo)
    except FileNotFoundError:
        print('\033[31mERRO >>> Esse arquivo não foi encontrado, veja se esqueceu do ".txt"\033[m')
    else:
        print('\033[32mVocê deletou "{}" com sucesso.'.format(nome_do_arquivo))


def remover_diretorio(nome_diretorio):
    try:
        os.rmdir(nome_diretorio)
    except FileNotFoundError:
        print('\033[31mERRO >>> Não foi encontrado um diretório com o nome "{}"\033[m'.format(nome_diretorio))
    else:
        print('\033[32mVocê removeu o diretório "{}" com sucesso!\033[m'.format(nome_diretorio))


def mudar_caminho(caminho_novo):
    os.chdir(caminho_novo)
    print('Agora você está em: {}'.format(caminho_novo))

def ver_caminho():
    print('Atualmente você está nesse caminho: {}'.format(os.getcwd()))

