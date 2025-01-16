import pandas as pd

df = pd.read_csv('raw/players.csv',sep=";", encoding='utf-8')

def print_list_filenames(path:str):
    '''
    prints the file names for a given directory
    '''
    result = []
    import os
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            name = filename.split('.')[0].split('_')[0][0]
            surname = filename.split('.')[0].split('_')[1]
            name = name.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
            result.append(name + '. ' + surname)
            dicti  ={
                'name': name + '. ' + surname,
                'img': filename
            }
            result.append(dicti)
    
    return result


'''
names_in_images = print_list_filenames('../../../static/img/jugadors/fotos_jugadores/')
names_in_stats = df['nom'].unique().tolist()

'''

def compare_lists(list1, list2):
    '''
    returns a list with the elements that are in list1 but not in list2
    '''
    return [item for item in list2 if item not in list1]

'''
print(names_in_images)
print(compare_lists(names_in_images, names_in_stats))
import json
players = json.dumps(names_in_images, ensure_ascii=False)
with open('players.json', 'w') as f:
    f.write(players)

'''

def calcular_estadisticas_equip(df):
    '''
    remove NAN values and calculate the mean, min and max for each player
    return as json
    '''
    df = df.loc[df['fase'] == 'Lliga regular',:]
    # Fusionem les dues columnes 'equip' i 'rival' per obtenir tots els equips que han jugat
    equipos = pd.concat([df['equip'], df['rival']])

    # Obtenim el conjunt d'equips únics
    equips_unics = equipos.unique()

    # Inicialitzem un diccionari per guardar la suma de les estadístiques
    estadistiques = {equip: {'punts': 0, 'rebots': 0, 'assistencies': 0, 'recuperacions' : 0, 'faltes': 0, 'taps': 0, 'valoracio': 0} for equip in equips_unics}
    cols = ['punts', 'rebots', 'assistencies', 'recuperacions', 'faltes', 'taps', 'valoracio']
    # Sumem les estadístiques per cada equip
    for equip in equips_unics:
        for col in cols:
            estadistiques[equip][col] = (df[df['equip'] == equip][col].sum())


    # Convertim el diccionari a un DataFrame per veure els resultats
    resultat = pd.DataFrame.from_dict(estadistiques, orient='index')
    resultat.reset_index(inplace=True)
    resultat.rename(columns={'index': 'equip'}, inplace=True)

    # convertim a JSON
    result_json = resultat.to_json(orient="records")
    return result_json

print(calcular_estadisticas_equip(df))