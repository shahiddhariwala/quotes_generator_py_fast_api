
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from constants import HOME_PAGE_HTML
from Quotes import Quotes

app = FastAPI()
quotes = Quotes()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return HOME_PAGE_HTML


@app.get("/quote")
def get_random_quote(num_quotes: int = 1):
    # /quote?num_quotes=10
    global quotes_df
    data = {
        "quotes": quotes.get_quotes(num_quotes)
    }

    return data


if __name__ == "__main__":
    print("We will create fast api to serve random quotes")
