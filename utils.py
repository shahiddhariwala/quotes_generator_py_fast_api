import pandas as pd


def split_csv(num_splits=2):
    csv_df = pd.read_csv("quotes-500k-webscrapped.csv")
    bucket_len = len(csv_df) // num_splits

    for i in range(len(csv_df)):
        csv_df.iloc[:, i*bucket_len:i +
                    bucket_len].to_csv(f"quotes-500k-webscrapped-{i+1}.csv")

    print(bucket_len)


split_csv(2)
