![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
<br>
![CI](https://github.com/vncsmyrnk/traffic-accidents-analysis-mg/actions/workflows/ci.yml/badge.svg)
<br>

# Traffic Accident Analysis in Minas Gerais

Data analysis on traffic accidents that occurred in the state of "Minas Gerais", Brazil.

The data source is located on [Portal de Dados Abertos do Estado de Minas Gerais website](https://dados.mg.gov.br/dataset/dados_acidentes_terrestres/resource/51c9d227-5ac8-44d5-9b8b-fc894df8032a).

The purpose of this study is to provide insights for future improvements to traffic legislation, in order to make it safer.

## Results

![Bar plot of mean age of people who died in traffic accidents in Belo Horizonte](https://github.com/vncsmyrnk/traffic-accidents-analysis-mg/blob/main/src/output/mean_age_per_year_in_bh.png)
<br>
![Percentages of traffic accidents per city](https://github.com/vncsmyrnk/traffic-accidents-analysis-mg/blob/main/src/output/percentages_of_traffic_accidents_per_city.png)
<br>
![traffic accidents by month](https://github.com/vncsmyrnk/traffic-accidents-analysis-mg/blob/main/src/output/traffic_accidents_by_month_plot.png)

## Run

- Using docker:

```bash
docker run --rm -it --name aamg --workdir /var/app -v ./src:/var/app python:3-alpine sh
pip install -r requirements.txt # Inside container
python accidents_analysis_mg.py # Inside container
```
