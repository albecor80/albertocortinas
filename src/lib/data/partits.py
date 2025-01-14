import pandas as pd
import json
df = pd.read_csv('raw/partits.csv',sep=";")

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

def calculate_stats_team(df):
    '''
    calcula les estadístiques per equip
    '''



    # Agrupar por equipo para sumar puntos hechos y recibidos
    equip_stats = df.groupby("equip").sum().reset_index()
    print(equip_stats.loc[:,['T2']].head())
    #result_json = equip_stats.to_json(orient="records")
    #return result_json


            
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
calculate_stats_team(df_melted)
