
import pandas as pd


NUM_OF_FILES = 2


def load_quotes_df():
    dfs = []
    for i in range(NUM_OF_FILES):
        df = pd.read_csv(f"quotes-500k-webscrapped-{i+1}.csv")
        dfs.append(df)
    quotes_df = pd.concat(dfs, ignore_index=True)
    print("Quotes 500k DF Loaded to serve")

    return quotes_df


load_quotes_df()


class Quotes:

    def __init__(self) -> None:
        self.quotes_factory = load_quotes_df()
        self.category_set = None
        print("Quotes Factory Initialised")

    def get_quotes(self, num_of_quotes):
        quotes = []

        for index, row in self.quotes_factory.sample(num_of_quotes).iterrows():
            quotes.append({
                "id": index,
                "quote": row["quote"],
                "author": row["author"],
                "category": row["category"],
            })
        return quotes

    def get_categories(self):

        if self.category_set is None:
            category_set = {"a"}

            for each in self.quotes_factory["category"].unique():
                if type(each) == str:
                    category_set.update(each.split(", "))
            self.category_set = category_set
        return self.category_set
