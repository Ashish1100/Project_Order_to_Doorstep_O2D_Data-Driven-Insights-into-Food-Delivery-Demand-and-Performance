import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import sweetviz as sv
import numpy as np
import warnings


def generate_sweetviz_report(df: pd.DataFrame, output_path: str = "reports/o2d_eda_report.html") -> None:
    """
    Generate an automated EDA report using Sweetviz.
    Silently skips report generation if Sweetviz is incompatible with NumPy.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Some Sweetviz versions expect np.VisibleDeprecationWarning; define a stub if missing.
        if not hasattr(np, "VisibleDeprecationWarning"):
            class VisibleDeprecationWarning(UserWarning):
                pass
            np.VisibleDeprecationWarning = VisibleDeprecationWarning 

        report = sv.analyze(df)
        report.show_html(output_path)
        print(f"Sweetviz report saved to {output_path}")

    except Exception as e:
        warnings.warn(
            f"Sweetviz report generation failed and will be skipped: {e}",
            RuntimeWarning,
        )




def plot_univariate_numeric(df: pd.DataFrame, column: str) -> None:
    if column not in df.columns:
        print(f"{column} not in DataFrame.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    sns.boxplot(x=df[column], ax=axes[0], color="skyblue")
    axes[0].set_title(f"Boxplot of {column}")

    sns.histplot(df[column], kde=True, ax=axes[1], color="steelblue")
    axes[1].axvline(df[column].mean(), color="green", linestyle="--", label="Mean")
    axes[1].axvline(df[column].median(), color="black", linestyle="-", label="Median")
    axes[1].set_title(f"Histogram of {column}")
    axes[1].legend()

    plt.tight_layout()
    plt.show()


def plot_categorical_counts(df: pd.DataFrame, column: str, top_n: int | None = None) -> None:
    if column not in df.columns:
        print(f"{column} not in DataFrame.")
        return

    if top_n is not None:
        order = df[column].value_counts().head(top_n).index
    else:
        order = df[column].value_counts().index

    plt.figure(figsize=(10, 4))
    sns.countplot(
        data=df,
        x=column,
        hue=column,
        order=order,
        palette="Paired",
        legend=False,
    )
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Count of {column}")
    plt.tight_layout()
    plt.show()


def plot_prep_vs_delivery(df: pd.DataFrame) -> None:
    cols = {"food_preparation_time", "delivery_time"}
    if not cols.issubset(df.columns):
        print("Required columns missing.")
        return

    plt.figure(figsize=(6, 6))
    sns.scatterplot(
        data=df,
        x="food_preparation_time",
        y="delivery_time",
        alpha=0.6,
    )
    plt.title("Food Preparation Time vs Delivery Time")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Correlation heatmap for numeric variables relevant to cost/time/ratings.
    """
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        print("No numeric columns found.")
        return

    plt.figure(figsize=(8, 6))
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def plot_cuisine_vs_total_time(df: pd.DataFrame) -> None:
    """
    Barplot of average total_time by cuisine (no FutureWarnings).
    """
    needed = {"cuisine_type", "food_preparation_time", "delivery_time"}
    if not needed.issubset(df.columns):
        print("Required columns missing.")
        return

    df_local = df.copy()
    df_local["total_time"] = (
        df_local["food_preparation_time"] + df_local["delivery_time"]
    )

    # explicitly set observed to keep current behaviour
    grp = (
        df_local
        .groupby("cuisine_type", dropna=False, observed=False)["total_time"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(10, 4))
    sns.barplot(
        data=grp,
        x="cuisine_type",
        y="total_time",
        hue="cuisine_type",  
        palette="viridis",
        dodge=False,
        legend=False,
    )
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Average total time (minutes)")
    plt.title("Average Total Time by Cuisine Type")
    plt.tight_layout()
    plt.show()

    



# ---------- Interactive Plotly plots ----------

def plotly_cost_distribution(df: pd.DataFrame) -> go.Figure:
    """
    Interactive distribution of order cost with differently colored bars,
    compatible with older Plotly versions.
    """
    if "cost_of_the_order" not in df.columns:
        raise ValueError("cost_of_the_order column missing")

    df_local = df.copy()

    # create coarse cost bins as categories
    df_local["cost_bin"] = pd.cut(
        df_local["cost_of_the_order"],
        bins=10,  
        include_lowest=True,
    )

    fig = px.histogram(
        df_local,
        x="cost_of_the_order",
        nbins=30,
        title="Order Cost Distribution",
        marginal="box",
        opacity=0.8,
        color="cost_bin",              
    )

    fig.update_layout(
        bargap=0.05,
        template="plotly_white",
        title_font=dict(size=18, family="Segoe UI, Arial, sans-serif"),
        font=dict(size=12, family="Segoe UI, Arial, sans-serif"),
        xaxis_title="Order cost",
        yaxis_title="Number of orders",
        legend_title_text="Cost bin",
    )

    fig.update_traces(marker_line_color="white", marker_line_width=0.3)

    return fig





def plotly_cuisine_demand(df: pd.DataFrame, top_n: int = 10) -> go.Figure:
    """
    Interactive bar chart of top N cuisines by number of orders.
    """
    if "cuisine_type" not in df.columns:
        raise ValueError("cuisine_type column missing")

    vc = df["cuisine_type"].value_counts().head(top_n).reset_index()
    vc.columns = ["cuisine_type", "order_count"]

    # custom palette
    palette = [
        "#1f77b4", "#2ca02c", "#17becf", "#9467bd", "#8c564b",
        "#e377c2", "#7f7f7f", "#bcbd22", "#ff7f0e", "#d62728",
    ][: len(vc)]

    fig = px.bar(
        vc,
        x="cuisine_type",
        y="order_count",
        title=f"Top {top_n} Cuisines by Orders",
        text="order_count",
        color="cuisine_type",
        color_discrete_sequence=palette,
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        template="plotly_white",
        xaxis_title="Cuisine type",
        yaxis_title="Number of orders",
        title_font=dict(size=18, family="Segoe UI, Arial, sans-serif"),
        font=dict(size=12, family="Segoe UI, Arial, sans-serif"),
        showlegend=False,  
    )

    return fig



def plotly_prep_delivery_scatter(df: pd.DataFrame) -> go.Figure:
    """
    Interactive scatter: preparation vs delivery time, colored by cuisine.[web:23]
    """
    needed = {"food_preparation_time", "delivery_time"}
    if not needed.issubset(df.columns):
        raise ValueError("Required time columns missing")

    color_col = "cuisine_type" if "cuisine_type" in df.columns else None

    fig = px.scatter(
        df,
        x="food_preparation_time",
        y="delivery_time",
        color=color_col,
        title="Food Preparation Time vs Delivery Time",
        hover_data=["restaurant_name"] if "restaurant_name" in df.columns else None,
        opacity=0.7,
    )
    fig.update_layout(
        xaxis_title="Food preparation time (minutes)",
        yaxis_title="Delivery time (minutes)",
    )
    return fig


def plotly_rating_vs_total_time(df: pd.DataFrame) -> go.Figure:
    """
    Boxplot of total_time across rating values (3–5 only), with a distinct
    color per rating.
    """
    needed = {"rating", "food_preparation_time", "delivery_time"}
    if not needed.issubset(df.columns):
        raise ValueError("Required columns missing")

    df_local = df.copy()

    # ensure numeric and remove missing / invalid ratings
    df_local["rating"] = pd.to_numeric(df_local["rating"], errors="coerce")
    df_local = df_local[df_local["rating"].between(3, 5)].dropna(subset=["rating"])

    if df_local.empty:
        raise ValueError("No valid ratings between 3 and 5 to plot")

    df_local["total_time"] = (
        df_local["food_preparation_time"] + df_local["delivery_time"]
    )

    # palette for ratings 3, 4, 5 (up to 4 buckets)
    palette = ["#d62728", "#ff7f0e", "#1f77b4", "#2ca02c"]

    fig = px.box(
        df_local,
        x="rating",
        y="total_time",
        color="rating",                  # different color per rating
        title="Total Fulfilment Time by Rating",
        points="all",
        color_discrete_sequence=palette,
    )

    fig.update_layout(
        xaxis_title="Rating",
        yaxis_title="Total time (minutes)",
        template="plotly_white",
        title_font=dict(size=18, family="Segoe UI, Arial, sans-serif"),
        font=dict(size=12, family="Segoe UI, Arial, sans-serif"),
        showlegend=False,               
    )

    fig.update_traces(
        marker=dict(size=5, opacity=0.4),
        line=dict(width=1.5),
    )

    return fig





def plot_univariate_numeric(df: pd.DataFrame, column: str) -> None:
    if column not in df.columns:
        print(f"{column} not in DataFrame.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    sns.boxplot(x=df[column], ax=axes[0], color="skyblue")
    axes[0].set_title(f"Boxplot of {column}")

    sns.histplot(df[column], kde=True, ax=axes[1], color="steelblue")
    axes[1].axvline(df[column].mean(), color="green", linestyle="--", label="Mean")
    axes[1].axvline(df[column].median(), color="black", linestyle="-", label="Median")
    axes[1].set_title(f"Histogram of {column}")
    axes[1].legend()

    plt.tight_layout()
    plt.show()


def plot_categorical_counts(df: pd.DataFrame, column: str, top_n: int | None = None) -> None:
    if column not in df.columns:
        print(f"{column} not in DataFrame.")
        return

    if top_n is not None:
        order = df[column].value_counts().head(top_n).index
    else:
        order = df[column].value_counts().index

    plt.figure(figsize=(10, 4))
    sns.countplot(
        data=df,
        x=column,
        hue=column,
        order=order,
        palette="Paired",
        legend=False,
    )
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Count of {column}")
    plt.tight_layout()
    plt.show()


def plot_prep_vs_delivery(df: pd.DataFrame) -> None:
    cols = {"food_preparation_time", "delivery_time"}
    if not cols.issubset(df.columns):
        print("Required columns missing.")
        return

    plt.figure(figsize=(6, 6))
    sns.scatterplot(
        data=df,
        x="food_preparation_time",
        y="delivery_time",
        alpha=0.6,
    )
    plt.title("Food Preparation Time vs Delivery Time")
    plt.tight_layout()
    plt.show()
