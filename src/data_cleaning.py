import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load the FoodHub orders dataset from CSV.
    """
    df = pd.read_csv(path)
    return df


def clean_ratings(df: pd.DataFrame, missing_label: str = "Not given") -> pd.DataFrame:
    """
    Convert rating column to numeric and handle 'Not given' as NaN.
    """
    df = df.copy()
    if "rating" in df.columns:
        df["rating"] = df["rating"].replace(missing_label, pd.NA)
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    return df


def cast_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    To ensure correct data types for numeric and categorical columns.
    """
    df = df.copy()

    numeric_cols = [
        "order_id",
        "customer_id",
        "cost_of_the_order",
        "food_preparation_time",
        "delivery_time",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    cat_cols = ["restaurant_name", "cuisine_type", "day_of_the_week"]
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")

    return df


def add_total_time(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adding a total_time column: preparation + delivery.
    """
    df = df.copy()
    if "food_preparation_time" in df.columns and "delivery_time" in df.columns:
        df["total_time"] = df["food_preparation_time"] + df["delivery_time"]
    return df
