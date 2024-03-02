![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
<br>
<br>

# Accidents Analysis in Minas Gerais

Data analysis on accidents that occurred in the state of "Minas Gerais", Brazil

## Run

- Using docker:

```bash
docker run --rm -it --name aamg --workdir /var/app -v ./src:/var/app python:3-alpine sh
pip install -r requirements.txt # Inside container
python accidents_analysis_mg.py # Inside container
```
