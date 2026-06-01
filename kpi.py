import pandas as pd

df = pd.read_csv("data/gold/retail_curated.csv")

print("\nTotal Revenue")
print(df["revenue"].sum())

print("\nRevenue By Category")
print(df.groupby("category")["revenue"].sum())

print("\nRevenue By City")
print(df.groupby("city")["revenue"].sum())
