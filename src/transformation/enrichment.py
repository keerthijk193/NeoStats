def join_product(df, prod):
    return df.merge(prod, on="product_id", how="left", suffixes=("", "_prod"))


def calculate_revenue(df):
    df["discount"] = df["discount"].fillna(0)

    df["revenue"] = df["price"] * df["quantity"] * (1 - df["discount"])

    return df


def save_gold(df):
    df.to_csv("data/gold/retail_curated.csv", index=False)
