# Data analysis of accidents in Minas Gerais
# Data sources:
# [Dados abertos da Policia Rodoviaria Federal]
# (https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes)

import pandas as pd


def generate_stats():
    """
    Calculate and display the accident stats
    """
    df = get_main_dataframe()
    df.to_csv("./output/csv/traffic-accidents-mg.csv", index=False)


def get_main_dataframe():
    """
    Get the accidents data and return a pandas dataframe of it
    """
    combined_df = None
    file_names = ["datatran2017.csv", "datatran2018.csv", "datatran2019.csv",
                  "datatran2020.csv", "datatran2021.csv", "datatran2022.csv"]
    for file_name in file_names:
        df = pd.read_csv("./data/" + file_name,
                         delimiter=";", encoding="latin-1")
        combined_df = pd.concat([combined_df, df], axis=0)
    return clean_main_df_data(combined_df)


def clean_main_df_data(df):
    """
    Clean the main dataframe data
    """
    df["date"] = pd.to_datetime(df["data_inversa"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["state"] = df["uf"]
    df["km"] = pd.to_numeric(df["km"].str.replace(",", "."))
    df["city"] = df["municipio"]
    df["cause"] = df["causa_acidente"]
    df["type"] = df["tipo_acidente"]
    df["victim_type"] = df["classificacao_acidente"]
    df["day_part"] = df["fase_dia"]
    df["road_slope"] = df["sentido_via"]
    df["weather"] = df["condicao_metereologica"]
    df["track_type"] = df["tipo_pista"]
    df["road_type"] = df["tracado_via"]
    df["area"] = df["uso_solo"]
    df["people_involved"] = df["pessoas"]
    df["dead"] = df["mortos"]
    df["slightly_injured"] = df["feridos_leves"]
    df["seriously_injured"] = df["feridos_graves"]
    df["uninjured"] = df["ilesos"]
    df["injured"] = df["ilesos"]
    df["ingnored_individuals"] = df["ignorados"]
    df["vehicles"] = df["veiculos"]
    df["accident_occurred"] = 1

    df["victim_type"] = df["victim_type"].replace(
            {"Com Vítimas Feridas": "Injured victims",
             "Sem Vítimas": "No victims",
             "Com Vítimas Fatais": "Fatal injured victims"})

    df = df[["date", "year", "month", "state", "km", "city",
             "cause", "type", "victim_type", "day_part", "road_slope",
             "weather", "track_type", "road_type", "area",
             "people_involved", "dead", "slightly_injured",
             "seriously_injured", "uninjured", "injured",
             "ingnored_individuals", "vehicles", "accident_occurred"]]

    df = df.drop_duplicates().reset_index(drop=True)
    return df


if __name__ == "__main__":
    generate_stats()
