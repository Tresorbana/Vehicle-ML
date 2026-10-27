import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go
import pandas as pd


def cars_sold_over_50000(df):
    """Return rows for cars with a selling price above 20,000."""
    return df.loc[df["selling_price"] > 20000]


def frequency_table(df):
    manufacturer_counts = df["manufacturer"].value_counts().reset_index()
    manufacturer_counts.columns = ["Manufacturer", "Count"]
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format="%.2f",
        justify="center",
    )
    return table_html


def total_price_by_manufacturer(df):
    """Return total selling price for each manufacturer and transmission."""
    return df.groupby(["manufacturer", "transmission"])["selling_price"].sum()
