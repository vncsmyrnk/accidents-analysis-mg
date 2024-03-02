import pandas as pd

df = pd.read_csv('https://dados.mg.gov.br/dataset/89a808ae-aa89-4e3c-a804-db58e822a72a/resource/51c9d227-5ac8-44d5-9b8b-fc894df8032a/download/dados_acidentes_terrestres.csv', delimiter=';');

df['ano_obito'] = pd.to_datetime(df['dt_obito'], format='%d/%m/%Y').dt.year

print(df.info())
print(df['dt_obito'].value_counts())
print(df.groupby('co_municipio_ibge_ocorrencia').mean('nu_idade'))
