
from typing import Union
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from constants import HOME_PAGE_HTML


NUM_OF_FILES = 2
quotes_df = None


app = FastAPI()


def load_quotes_df():
    global quotes_df
    dfs = []
    for i in range(NUM_OF_FILES):
        df = pd.read_csv(f"quotes-500k-webscrapped-{i+1}.csv")
        dfs.append(df)
    quotes_df = pd.concat(dfs, ignore_index=True)
    print("Quotes 500k DF Loaded to serve")


load_quotes_df()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return HOME_PAGE_HTML


@app.get("/quote")
def get_random_quote(num_quotes: int = 1):
    # /quote?num_quotes=10
    global quotes_df
    data = {
        "quotes": []
    }

    for index, row in quotes_df.sample(num_quotes).iterrows():
        data["quotes"].append({
            "id": index,
            "quote": row["quote"],
            "author": row["author"],
            "category": row["category"],
        })
    return data


if __name__ == "__main__":
    print("We will create fast api to generate quotes")
