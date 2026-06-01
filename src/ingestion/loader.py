import pandas as pd


def load_data(file_path):
    df = pd.read_excel(file_path, sheet_name="retail_data1")
    prod = pd.read_excel(file_path, sheet_name="product_details")
    return df, prod


def save_bronze(df):
    df.to_csv("data/bronze/retail_raw.csv", index=False)
