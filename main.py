import os
from src.data_visualization import generate_sweetviz_report
from src.data_cleaning import load_data, clean_ratings, cast_dtypes, add_total_time
from src.analysis_helpers import (
    compute_basic_stats,
    get_rating_missing_count,
    get_top_restaurants,
    get_top_cuisines,
    get_weekday_weekend_split,
    get_top_customers,
    get_percentage_cost_above,
    compute_time_correlations,
    cuisine_performance_summary,
    restaurant_service_score,
    orders_over_total_time_threshold,
    rating_bucket_analysis,
)
from src.data_visualization import (
    plot_univariate_numeric,
    plot_categorical_counts,
    plot_prep_vs_delivery,
    plot_correlation_heatmap,
    plot_cuisine_vs_total_time,
    plotly_cost_distribution,
    plotly_cuisine_demand,
    plotly_prep_delivery_scatter,
    plotly_rating_vs_total_time,
)

DATA_PATH = os.path.join("data", "foodhub_order.csv")


def main() -> None:
    # 1. Load and clean data
    print("Loading data...")
    df = load_data(DATA_PATH)
    print(f"Loaded shape: {df.shape}")

    df = clean_ratings(df)
    df = cast_dtypes(df)
    df = add_total_time(df)
    generate_sweetviz_report(df)

    # 2. Basic stats
    print("\n=== Basic stats ===")
    stats = compute_basic_stats(df)
    for col, s in stats.items():
        print(
            f"{col}: count={s['count']}, mean={s['mean']:.2f}, "
            f"min={s['min']:.2f}, max={s['max']:.2f}"
        )

    # 3. Missing ratings
    missing_ratings = get_rating_missing_count(df)
    print(f"\nMissing ratings (NaN): {missing_ratings}")

    # 4. Demand analytics
    print("\n=== Top 5 restaurants ===")
    print(get_top_restaurants(df, n=5))

    print("\n=== Top 5 cuisines ===")
    print(get_top_cuisines(df, n=5))

    print("\n=== Weekday vs Weekend ===")
    print(get_weekday_weekend_split(df))

    print("\n=== Top 5 customers ===")
    print(get_top_customers(df, n=5))

    # 5. Time‑based performance analytics
    print("\n=== Correlation matrix (cost/time/rating) ===")
    print(compute_time_correlations(df))

    print("\n=== Cuisine performance summary ===")
    print(cuisine_performance_summary(df).head(10))

    print("\n=== Restaurant service score (min 20 orders) ===")
    print(restaurant_service_score(df, min_orders=20).head(10))

    print("\n=== Orders taking more than 60 minutes total ===")
    print(orders_over_total_time_threshold(df, threshold_minutes=60))

    print("\n=== Rating bucket analysis ===")
    print(rating_bucket_analysis(df))

    # 6. Static visualizations (matplotlib/seaborn)
    print("\nShowing static plots...")
    plot_univariate_numeric(df, "cost_of_the_order")
    plot_univariate_numeric(df, "food_preparation_time")
    plot_univariate_numeric(df, "delivery_time")

    plot_categorical_counts(df, "cuisine_type", top_n=10)
    plot_cuisine_vs_total_time(df)
    plot_prep_vs_delivery(df)
    plot_correlation_heatmap(df)

    # 7. Interactive Plotly visualizations
    print("\nOpening interactive Plotly figures (use .show())...")
    plotly_cost_distribution(df).show()
    plotly_cuisine_demand(df, top_n=10).show()
    plotly_prep_delivery_scatter(df).show()
    plotly_rating_vs_total_time(df).show()


if __name__ == "__main__":
    main()
