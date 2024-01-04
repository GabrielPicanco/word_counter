import json

dicionario_json = '{"Nome": "Nino", "Idade": 2,"Cidade": "Mora na minha casa"}'

dicionario_json = json.loads(dicionario_json)
dicionario_json['Habilidade'] = ['Comer','Dormir','Abrir Portas']
for k,v in dicionario_json.items():
    print('{} >>> {}'.format(k,v))
print('-'*50)
cont = 1

for c in dicionario_json['Habilidade']:
    print('Habilidade {} >>> {}'.format(cont,c))
    cont += 1


def validar_json(nome_objeto):
    try:
        nome_objeto = json.loads(nome_objeto)
    except TypeError:
        print('\033[31mEsse objeto é um objeto python.')
    else:
        print('\033[32mEsse é um arquivo json\033[m')


validar_json(dicionario_json)

