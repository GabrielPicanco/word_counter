import os

os.chdir(r'C:/Users/gabri/Área de Trabalho/arquivos')
arquivos = (os.listdir())
print(arquivos)
files = []

for arquivo in arquivos:
    if os.path.isfile(arquivo):
        files.append(arquivo)


print(files)