import pandas as pd

def fetch_tiktok_data():
    data_url = "https://raw.githubusercontent.com/mateuspestana/datasets_aulas/main/ukraine.csv"
    data = pd.read_csv(data_url)
    return data

def display_data(data):
    # Modifc ade acordo com a ordem da coluna
    print("Top 5 TokTok Posts:")
    for index, row in data.head(5).iterrows():
        views = f"{row['views']:,.0f}"  # Format views with commas
        print(f"{index + 1}. Username: {row['user']} | URL: {row['url']} | Views: {views}")

data = fetch_tiktok_data()
display_data(data)

