import json

dicionario = {'Nome': 'Nino',
                   'Idade': 2,
                   'Racao': 'Whiskas',
                   'Habilidades': ['Comer','Dormir','Miar'],
                   'Caracteristicas': [{'Superior': 'Olhos azuis'}, {'Inferior': 'Bucho rosa'}]
                   }


dicionario = json.dumps(dicionario)
print(dicionario)