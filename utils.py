import pandas as pd


def split_csv(num_splits=2):
    csv_df = pd.read_csv("quotes-500k-webscrapped.csv")
    bucket_len = len(csv_df) // num_splits

    for i in range(num_splits):
        print(f"{i*bucket_len}- {i*bucket_len + bucket_len}")
        df = csv_df[ i*bucket_len:i*bucket_len +
                         bucket_len]
        df.to_csv(f"quotes-500k-webscrapped-{i+1}.csv")


split_csv(2)
