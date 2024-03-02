import pandas as pd
import matplotlib.pyplot as plt


def generate_stats():
    """
    Calculate and display the accident stats
    """
    df = get_dataframe()
    df = clean_data(df)
    generate_mean_age_per_year_in_bh_graphic(df)


def get_dataframe():
    """
    Get the accidents data and return a pandas dataframe of it
    """
    file_url = "https://dados.mg.gov.br/dataset" \
               "/89a808ae-aa89-4e3c-a804-db58e822a72a/resource" \
               "/51c9d227-5ac8-44d5-9b8b-fc894df8032a/download" \
               "/dados_acidentes_terrestres.csv"
    df = pd.read_csv(file_url, delimiter=";")
    return df


def clean_data(df):
    """
    Clean the dataframe data
    """
    df["date"] = pd.to_datetime(df["dt_obito"], format="%d/%m/%Y")
    df["year"] = df["date"].dt.year
    df["date_birth"] = pd.to_datetime(df["dt_nascimento"], format="%d/%m/%Y")
    df["age"] = df["nu_idade"]
    df["sex"] = df["sg_sexo"].replace(
            {"Masculino": "Male", "Feminino": "Female"})
    df["city"] = df["co_municipio_ibge_ocorrencia"]
    df["id_accident_cause"] = df["co_cid_causa_basica"]
    df["desc_accident_cause"] = df["desc_cid_causa_basica"]
    df = df[["date", "year", "date_birth", "age", "sex",
             "city", "id_accident_cause", "desc_accident_cause"]]
    return df


def generate_mean_age_per_year_in_bh_graphic(df):
    grouped = df[df["city"] == "Belo Horizonte"].groupby(["year"]).mean("age").sort_values(by="year")
    plt.bar(grouped.index, grouped["age"])
    plt.title("Bar plot of average age of people who died in traffic accidents (from sample)")
    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.savefig("./output/mean_age_per_year_in_bh.png")
    return grouped


if __name__ == "__main__":
    generate_stats()
