# Useful methods to translate some columns of the main
# dataframe
# Yet in development

import traffic_accidents_mg as tamg
from googletrans import Translator


translator = Translator()


def translate():
    df = tamg.get_main_dataframe()
    translate_cause(df)


def translate_cause(df):
    """
    df_cause = df["cause"].values_count().reset_index()
    df["translated_cause"] = df["cause"].apply(
            lambda x: translator.translate(x, dest="en").text)
    @TODO Finish this method
    """
    return None


if __name__ == "__main__":
    translate()
