from pathlib import Path

import pandas as pd
from django.shortcuts import render

from .dashboard import frequency_table


def dashboard_view(request):
    data_path = Path(__file__).resolve().parent.parent / "dummy_data" / "vehicles_ml_dataset.csv"
    df = pd.read_csv(data_path)
    return render(request, "vehicles/index.html", {"frequency_table": frequency_table(df)})