from pathlib import Path

import pandas as pd
from django.shortcuts import render

from .dashboard import cars_sold_over_50000, frequency_table, total_price_by_manufacturer


def dashboard_view(request):
    data_path = Path(__file__).resolve().parent.parent / "dummy_data" / "vehicles_ml_dataset.csv"
    df = pd.read_csv(data_path)
    expensive_cars = cars_sold_over_50000(df)
    manufacturer_totals = total_price_by_manufacturer(df)
    return render(
        request,
        "vehicles/index.html",
        {
            "frequency_table": frequency_table(df),
            "cars_over_50000": expensive_cars.to_html(
                classes="table table-bordered table-striped table-sm",
                index=False,
            ),
            "manufacturer_totals": manufacturer_totals.to_frame().to_html(
                classes="table table-bordered table-striped table-sm",
            ),
        },
    )
