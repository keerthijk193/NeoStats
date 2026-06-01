import pandas as pd


def remove_failed_transactions(df):
    return df[df["payment_status"] == "successful"]


def remove_duplicates(df):
    return df.drop_duplicates(subset=["transaction_id"])


def fix_quantity_price(df):
    df = df[df["quantity"] > 0]

    df["price"] = df["price"].astype(float)
    df = df[df["price"] > 0]

    return df


def standardize_columns(df):
    CATEGORY_MAP = {
        "elec": "electronics",
        "electronics": "electronics",
        "cloth": "clothing",
        "clothing": "clothing",
        "furn": "furniture",
        "furniture": "furniture",
        "home": "home appliances",
        "home appliances": "home appliances",
    }

    df["category"] = df["category"].str.lower().map(CATEGORY_MAP)
    df["product_name"] = df["product_name"].str.lower().str.strip()
    df["city"] = df["city"].str.title()

    return df


def fix_dates(df):
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
    return df


def save_silver(df):
    df.to_csv("data/silver/retail_cleaned.csv", index=False)
