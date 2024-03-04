import pandas as pd
import matplotlib.pyplot as plt


def generate_stats():
    """
    Calculate and display the accident stats
    """
    df = build_full_dataframe()
    generate_mean_age_per_year_in_bh_plot(df)
    generate_percentages_of_traffic_accidents_per_city(df)
    generate_traffic_accidents_by_month_plot(df)
    df.to_csv("./output/traffic-accidents-mg.csv", index=False)


def build_full_dataframe():
    """
    Completes all operations to build the final dataframe
    """
    df_main = get_main_dataframe()
    df_loc = get_city_localization_dataframe()
    df_merged = df_main.merge(df_loc, how="inner", on="city")
    df_merged = df_merged.drop_duplicates().reset_index(drop=True)
    return df_merged


def get_main_dataframe():
    """
    Get the accidents data and return a pandas dataframe of it
    """
    file_url = "https://dados.mg.gov.br/dataset" \
               "/89a808ae-aa89-4e3c-a804-db58e822a72a/resource" \
               "/51c9d227-5ac8-44d5-9b8b-fc894df8032a/download" \
               "/dados_acidentes_terrestres.csv"
    df = pd.read_csv(file_url, delimiter=";")
    return clean_main_df_data(df)


def get_city_localization_dataframe():
    """
    Get the localization of cities in MG data
    and return a pandas dataframe of it
    """
    file_url = "https://raw.githubusercontent.com" \
               "/alanwillms/geoinfo/master/latitude-longitude-cidades.csv"
    df = pd.read_csv(file_url, delimiter=";")
    return clean_city_localization_df_data(df)


def clean_main_df_data(df):
    """
    Clean the main dataframe data
    """
    # Create formatted columns
    df["date"] = pd.to_datetime(df["dt_obito"], format="%d/%m/%Y")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["date_birth"] = pd.to_datetime(df["dt_nascimento"], format="%d/%m/%Y")
    df["age"] = df["nu_idade"]
    df["sex"] = df["sg_sexo"].replace(
            {"Masculino": "Male", "Feminino": "Female"})
    df["city"] = df["co_municipio_ibge_ocorrencia"]
    df["id_accident_cause"] = df["co_cid_causa_basica"]
    df["desc_accident_cause"] = df["desc_cid_causa_basica"]
    df = df[["date", "year", "month", "date_birth", "age", "sex",
             "city", "id_accident_cause", "desc_accident_cause"]]

    # Removes null rows
    df = df[~df["city"].isnull()]
    df = df[~df["date_birth"].isnull()]
    df = df[~df["sex"].isnull()]

    df = df.drop_duplicates().reset_index(drop=True)

    return df


def clean_city_localization_df_data(df):
    """
    Clean the city localization dataframe data
    """
    df["city"] = df["municipio"]
    df["city_code"] = df["id_municipio"]
    df["city_latitude"] = df["latitude"]
    df["city_longitude"] = df["longitude"]
    df = df[df["uf"] == "MG"]
    df = df[["city", "city_code", "city_latitude", "city_longitude"]]

    df = df.drop_duplicates().reset_index(drop=True)

    return df


def generate_mean_age_per_year_in_bh_plot(df):
    """
    Generate the "Average age of people who died in traffic
    accidents in Belo Horizonte" plot
    """
    data = df[df["city"] == "Belo Horizonte"].groupby(["year"])
    data = data.mean("age").sort_values(by="year").reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(data["year"], data["age"])
    add_labels_on_bars(data["year"], data["age"])
    plt.title("Average age of people who died"
              " in traffic accidents in Belo Horizonte")
    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.xticks(rotation=45, horizontalalignment="right")
    plt.savefig("./output/mean_age_per_year_in_bh.png")


def generate_percentages_of_traffic_accidents_per_city(df):
    """
    Generate the "Percentages of accidents per city" plot
    """
    data = round(df["city"].value_counts(normalize=True).head(10) * 100, 2)
    data = data.sort_values().reset_index()

    plt.figure(figsize=(12, 8))
    plt.barh(data["city"], data["proportion"])
    add_labels_on_bars_inverted(data["city"], data["proportion"])
    plt.title("Percentages of accidents per city")
    plt.xlabel("Percentage (%)")
    plt.ylabel("City")
    plt.yticks(rotation=45, horizontalalignment="right")
    plt.savefig("./output/percentages_of_traffic_accidents_per_city.png")


def generate_traffic_accidents_by_month_plot(df):
    """
    Generate the "Traffic accidents by month" plot
    """
    data = round(df["month"].value_counts(normalize=True) * 100, 2)
    data = data.sort_values().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(data["month"], data["proportion"])
    add_labels_on_bars(data["month"], data["proportion"])
    plt.title("Traffic accidents by month")
    plt.xlabel("Month")
    plt.ylabel("Percentage (%)")
    plt.xticks(rotation=45, horizontalalignment="right")
    plt.savefig("./output/traffic_accidents_by_month_plot.png")


# Utils #

def add_labels_on_bars(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha="center")


def add_labels_on_bars_inverted(x, y):
    for i in range(len(x)):
        plt.text(y[i], i, y[i], va="center")


if __name__ == "__main__":
    generate_stats()
