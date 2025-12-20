import pandas as pd
import numpy as np


def compute_basic_stats(df: pd.DataFrame) -> dict:
    """
    Compute basic summary statistics for key numeric columns.
    """
    stats = {}
    for col in ["cost_of_the_order", "food_preparation_time", "delivery_time", "rating"]:
        if col in df.columns:
            desc = df[col].describe()
            stats[col] = {
                "count": float(desc["count"]),
                "mean": float(desc["mean"]),
                "std": float(desc["std"]),
                "min": float(desc["min"]),
                "25%": float(desc["25%"]),
                "50%": float(desc["50%"]),
                "75%": float(desc["75%"]),
                "max": float(desc["max"]),
            }
    return stats


def get_rating_missing_count(df: pd.DataFrame) -> int:
    """
    Number of orders with missing rating (NaN).
    """
    if "rating" not in df.columns:
        return 0
    return int(df["rating"].isna().sum())


def get_top_restaurants(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Top n restaurants by number of orders.
    """
    if "restaurant_name" not in df.columns:
        return pd.DataFrame()
    vc = df["restaurant_name"].value_counts().head(n)
    out = vc.reset_index()
    out.columns = ["restaurant_name", "order_count"]
    return out


def get_top_cuisines(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Top n cuisines by number of orders.
    """
    if "cuisine_type" not in df.columns:
        return pd.DataFrame()
    vc = df["cuisine_type"].value_counts().head(n)
    out = vc.reset_index()
    out.columns = ["cuisine_type", "order_count"]
    return out


def get_weekday_weekend_split(df: pd.DataFrame) -> pd.Series:
    """
    Order counts by weekday/weekend flag.
    """
    if "day_of_the_week" not in df.columns:
        return pd.Series(dtype=int)
    return df["day_of_the_week"].value_counts()


def get_top_customers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Top n customers by number of orders.
    """
    if "customer_id" not in df.columns:
        return pd.DataFrame()
    vc = df["customer_id"].value_counts().head(n)
    out = vc.reset_index()
    out.columns = ["customer_id", "order_count"]
    return out


def get_percentage_cost_above(df: pd.DataFrame, threshold: float) -> float:
    """
    Percentage of orders whose cost_of_the_order is greater than threshold.
    """
    if "cost_of_the_order" not in df.columns or len(df) == 0:
        return 0.0
    mask = df["cost_of_the_order"] > threshold
    return round(mask.mean() * 100, 2)


def compute_time_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Correlation matrix among cost, preparation time, delivery time, and rating.
    Helpful for understanding how service attributes relate to satisfaction.
    """
    cols = [
        "cost_of_the_order",
        "food_preparation_time",
        "delivery_time",
        "rating",
        "total_time",
    ]
    cols = [c for c in cols if c in df.columns]
    if not cols:
        return pd.DataFrame()
    return df[cols].corr()


def cuisine_performance_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate metrics by cuisine:
    - order_count
    - avg_cost
    - avg_rating
    - avg_prep_time
    - avg_delivery_time
    - avg_total_time
    """
    required = ["cuisine_type", "cost_of_the_order", "rating",
                "food_preparation_time", "delivery_time"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        return pd.DataFrame()

    df_local = df.copy()
    if "total_time" not in df_local.columns:
        df_local["total_time"] = (
            df_local["food_preparation_time"] + df_local["delivery_time"]
        )

    grp = df_local.groupby("cuisine_type", dropna=False)
    summary = grp.agg(
        order_count=("order_id", "count"),
        avg_cost=("cost_of_the_order", "mean"),
        avg_rating=("rating", "mean"),
        avg_prep_time=("food_preparation_time", "mean"),
        avg_delivery_time=("delivery_time", "mean"),
        avg_total_time=("total_time", "mean"),
    ).reset_index()

    return summary.sort_values("order_count", ascending=False)


def restaurant_service_score(df: pd.DataFrame, min_orders: int = 20) -> pd.DataFrame:
    """
    Compute a simple service score per restaurant combining:
    - mean rating (normalized 0-1)
    - mean total_time (inverted, faster is better)
    Only restaurants with at least min_orders are included.[web:26]
    """
    needed = ["restaurant_name", "rating",
              "food_preparation_time", "delivery_time"]
    if any(c not in df.columns for c in needed):
        return pd.DataFrame()

    df_local = df.copy()
    df_local["total_time"] = df_local["food_preparation_time"] + df_local["delivery_time"]

    grp = df_local.groupby("restaurant_name")
    agg = grp.agg(
        order_count=("order_id", "count"),
        avg_rating=("rating", "mean"),
        avg_total_time=("total_time", "mean"),
    ).reset_index()

    agg = agg[agg["order_count"] >= min_orders]

    # Normalize rating (3–5 usually) and time
    rating_min, rating_max = 3.0, 5.0
    agg["rating_norm"] = (agg["avg_rating"] - rating_min) / (rating_max - rating_min)

    t_min = agg["avg_total_time"].min()
    t_max = agg["avg_total_time"].max()
    if t_max == t_min:
        agg["time_norm"] = 1.0
    else:
        # lower total_time -> higher score
        agg["time_norm"] = 1 - (agg["avg_total_time"] - t_min) / (t_max - t_min)

    # Weighted score
    agg["service_score"] = 0.6 * agg["rating_norm"] + 0.4 * agg["time_norm"]

    return agg.sort_values("service_score", ascending=False)


def orders_over_total_time_threshold(df: pd.DataFrame, threshold_minutes: int = 60) -> dict:
    """
    Percentage of orders whose total_time exceeds a threshold (e.g., > 60 min).[web:14]
    """
    if "food_preparation_time" not in df.columns or "delivery_time" not in df.columns:
        return {"count_above": 0, "percentage_above": 0.0}

    df_local = df.copy()
    df_local["total_time"] = df_local["food_preparation_time"] + df_local["delivery_time"]
    mask = df_local["total_time"] > threshold_minutes
    count_above = int(mask.sum())
    if len(df_local) == 0:
        perc = 0.0
    else:
        perc = round(mask.mean() * 100, 2)

    return {
        "threshold": threshold_minutes,
        "count_above": count_above,
        "percentage_above": perc,
    }


def rating_bucket_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bucket ratings and compute average cost and time metrics per bucket.
    """
    if "rating" not in df.columns:
        return pd.DataFrame()

    df_local = df.copy()
    if "total_time" not in df_local.columns and \
       {"food_preparation_time", "delivery_time"}.issubset(df_local.columns):
        df_local["total_time"] = (
            df_local["food_preparation_time"] + df_local["delivery_time"]
        )

    df_local["rating_bucket"] = pd.cut(
        df_local["rating"],
        bins=[2.5, 3.5, 4.0, 4.5, 5.0],
        labels=["3.0–3.5", "3.5–4.0", "4.0–4.5", "4.5–5.0"],
        include_lowest=True,
    )

    grp = df_local.groupby("rating_bucket", dropna=True).agg(
        order_count=("order_id", "count"),
        avg_cost=("cost_of_the_order", "mean"),
        avg_prep_time=("food_preparation_time", "mean"),
        avg_delivery_time=("delivery_time", "mean"),
        avg_total_time=("total_time", "mean"),
    ).reset_index()

    return grp


def compute_basic_stats(df: pd.DataFrame) -> dict:
    stats = {}
    for col in ["cost_of_the_order", "food_preparation_time", "delivery_time", "rating"]:
        if col in df.columns:
            desc = df[col].describe()
            stats[col] = {
                "count": float(desc["count"]),
                "mean": float(desc["mean"]),
                "min": float(desc["min"]),
                "max": float(desc["max"]),
            }
    return stats


def get_rating_missing_count(df: pd.DataFrame) -> int:
    if "rating" not in df.columns:
        return 0
    return df["rating"].isna().sum()


def get_top_restaurants(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    if "restaurant_name" not in df.columns:
        return pd.DataFrame()
    vc = df["restaurant_name"].value_counts().head(n)
    out = vc.reset_index()
    out.columns = ["restaurant_name", "order_count"]
    return out


def get_top_cuisines(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    if "cuisine_type" not in df.columns:
        return pd.DataFrame()
    vc = df["cuisine_type"].value_counts().head(n)
    out = vc.reset_index()
    out.columns = ["cuisine_type", "order_count"]
    return out


def get_weekday_weekend_split(df: pd.DataFrame) -> pd.Series:
    if "day_of_the_week" not in df.columns:
        return pd.Series(dtype=int)
    return df["day_of_the_week"].value_counts()


def get_top_customers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    if "customer_id" not in df.columns:
        return pd.DataFrame()
    vc = df["customer_id"].value_counts().head(n)
    out = vc.reset_index()
    out.columns = ["customer_id", "order_count"]
    return out


def get_percentage_cost_above(df: pd.DataFrame, threshold: float) -> float:
    if "cost_of_the_order" not in df.columns or len(df) == 0:
        return 0.0
    mask = df["cost_of_the_order"] > threshold
    return round(mask.mean() * 100, 2)
