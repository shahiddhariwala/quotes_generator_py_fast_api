
from typing import Union
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

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
    print(quotes_df.sample(1))


load_quotes_df()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
<html>
<head>
<title>Quotes Worlds</title>
<style>
body {
  background-image: linear-gradient(to right, #4CAF50, #00BCD4);
  transition: background-image 1s ease-in-out;
}

.button {
  background-color: transparent;
  border: 1px solid #fff;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.button:hover {
  background-color: #fff;
  color: #4CAF50;
}
</style>
</head>
<body>
<h1>Welcome to Quotes Worlds!</h1>
<p>Hit the button below to get a random quote.</p>
<a href="/quote?num_quotes=1" class="button">Get Quote</a>
</body>
</html>
"""

# /quote?num_quotes=10


@app.get("/quote")
def get_random_quote(num_quotes: int = 1):
    global quotes_df

    print(quotes_df.sample(num_quotes), type(quotes_df.sample(num_quotes)))
    return quotes_df.sample(num_quotes)


if __name__ == "__main__":
    print("We will create fast api to generate quotes")
