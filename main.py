import pandas as pd

data_url = "https://raw.githubusercontent.com/mateuspestana/datasets_aulas/main/ukraine.csv"
data = pd.read_csv(data_url)

print(data)
