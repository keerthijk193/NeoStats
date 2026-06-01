from src.ingestion.loader import load_data, save_bronze

from src.validation.quality import validate_schema

from src.transformation.cleaning import (
    remove_failed_transactions,
    remove_duplicates,
    fix_quantity_price,
    standardize_columns,
    fix_dates,
    save_silver,
)

from src.utils.masking import apply_masking

from src.transformation.enrichment import join_product, calculate_revenue, save_gold


def run_pipeline():

    file_path = "data/raw/USECASE - Data Engineering.xlsx"

    # INGESTION
    df, prod = load_data(file_path)
    save_bronze(df)

    # VALIDATION
    validate_schema(df)

    # CLEANING (SILVER)
    df = remove_failed_transactions(df)
    df = remove_duplicates(df)
    df = fix_quantity_price(df)
    df = standardize_columns(df)
    df = fix_dates(df)
    df = apply_masking(df)

    save_silver(df)

    # ENRICHMENT (GOLD)
    df = join_product(df, prod)
    df = calculate_revenue(df)

    save_gold(df)

    print("✅ Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
