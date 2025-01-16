import pandas as pd
import json
df = pd.read_csv('raw/partits.csv',sep=";")
df_players = pd.read_csv('raw/players.csv',sep=";")
df_melted = pd.melt(
    df,
    id_vars = ['id_partit', 'jornada'],
    value_vars = ['local', 'visitant'],
    var_name = 'local_visitant',
    value_name = 'equip'
)
df_melted['punts'] = pd.melt(
    df,
    id_vars = ['id_partit', 'jornada'],
    value_vars = ['resultat_local', 'resultat_visitant'],
    value_name = 'punts'
)['punts']

df_melted = df_melted.sort_values(['jornada','id_partit'])
df_melted = df_melted.reset_index(drop=True)
print(df_melted.head())
def calcular_estadisticas_jornada(df):
    jornadas = []
    for jornada, dades_jornada in df.groupby('jornada'):
        locals = dades_jornada.loc[dades_jornada['local_visitant']=='local',:]
        visitants = dades_jornada.loc[dades_jornada['local_visitant']=='visitant',:]

        victories_locals = sum(locals['punts'].values > visitants['punts'].values)
        percentatge_locals = (victories_locals / len(locals)) * 100 if len(locals)>0 else 0

        promig_local = locals['punts'].mean()
        min_local = locals['punts'].min()
        max_local = locals['punts'].max()

        promig_visitant = visitants['punts'].mean()
        min_visitant = visitants['punts'].min()
        max_visitant = visitants['punts'].max()

        max = dades_jornada['punts'].max()
        min = dades_jornada['punts'].min()

        diferencies = abs(locals['punts'].values - visitants['punts'].values)
        maximadiferencia = diferencies.max() if len(diferencies)>0 else 0

        jornadas.append({
            'jornada': jornada,
            'victories_locals': int(victories_locals),
            'percentatge_locals': float(percentatge_locals),
            'promig_local': float(promig_local),
            'min_local': int(min_local),
            'max_local': int(max_local),
            'promig_visitant': float(promig_visitant),
            'min_visitant': int(min_visitant),
            'max_visitant': int(max_visitant),
            'max': int(max),
            'min': int(min),
            'maximadiferencia': int(maximadiferencia)
        })

    return jornadas


def calcular_punts_equips(df):
    '''
    calcula els punts anotats i rebuts per cada equip
    '''
    locals = df.loc[df['local_visitant']=='local',:].rename(columns={'equip':'equip_local', 'punts':'punts_local'})
    visitants = df.loc[df['local_visitant']=='visitant',:].rename(columns={'equip':'equip_visitant', 'punts':'punts_visitant'})

    merged = pd.merge(locals, visitants, on='id_partit')

    equips = pd.concat([
        merged[["equip_local", "punts_local", "punts_visitant"]].rename(columns={
            "equip_local": "equip", "punts_local": "punts_fets", "punts_visitant": "punts_rebuts"
        }),
        merged[["equip_visitant", "punts_visitant", "punts_local"]].rename(columns={
            "equip_visitant": "equip", "punts_visitant": "punts_fets", "punts_local": "punts_rebuts"
        })
    ])

    # Agrupar por equipo para sumar puntos hechos y recibidos
    equip_stats = equips.groupby("equip").sum().reset_index()

    result_json = equip_stats.to_json(orient="records")
    return result_json

import json


def calculate_stats_team(df):
    '''
    Calcula les estadístiques per equip
    '''

    # Load the JSON data
    with open('equips.json', 'r', encoding='utf-8') as file:
        equips_data = json.load(file)
    nom_to_id = {team['nom']: team['id'] for team in equips_data}

    # Aggregate the necessary columns by 'equip'
    df_agg = df.groupby('equip').agg({
        'madeT2': 'sum',
        'numT2': 'sum',
        'madeT3': 'sum',
        'numT3': 'sum',
        'madeTL': 'sum',
        'numTL': 'sum'
    }).reset_index()
    
    # Calculate percentages
    df_agg['perc_TL'] = df_agg['madeTL'] / df_agg['numTL']
    df_agg['perc_T2'] = df_agg['madeT2'] / df_agg['numT2']
    df_agg['perc_T3'] = df_agg['madeT3'] / df_agg['numT3']
    df_agg['perc_TL'] = round(df_agg['perc_TL'] * 100, 0)
    df_agg['perc_T2'] = round(df_agg['perc_T2'] * 100, 0)
    df_agg['perc_T3'] = round(df_agg['perc_T3'] * 100, 0)

    # Replace infinite values with 0 in place
    df_agg.replace([float('inf'), -float('inf')], 0, inplace=True)
    
    # Fill NaN values with 0 in place
    df_agg.fillna(0, inplace=True)
    df_agg['id'] = df_agg['equip'].map(nom_to_id)
    df_agg.drop(['equip','madeT2', 'madeTL','madeT3','numT2', 'numTL','numT3'], axis=1, inplace=True)
    
    # Save the JSON data
    df_agg.to_json('stats_team.json', orient='records')
    

            
'''
estadistiques = calcular_estadisticas_jornada(df_melted)
estadistiques_json = json.dumps(estadistiques)
with open('estadistiques.json', 'w') as f:
    f.write(estadistiques_json)



punts = calcular_punts_equips(df_melted)

punts_json = json.dumps(punts)
with open('punts.json', 'w') as f:
    f.write(punts_json)


'''
calculate_stats_team(df_players)
