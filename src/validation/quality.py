def validate_schema(df):
    required_columns = [
        "transaction_id",
        "product_id",
        "price",
        "quantity",
        "payment_status",
        "city",
    ]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise Exception(f"Missing columns: {missing}")
