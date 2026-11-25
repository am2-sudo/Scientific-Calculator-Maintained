import csv
from history_export import export_history

def test_history_export_csv(tmp_path):
    destination = tmp_path / "history.csv"
    entries = ["2 + 3 = 5", "sqrt(16) = 4"]
    export_history(entries, destination)
    with destination.open(encoding="utf-8-sig", newline="") as csv_file:
        rows = list(csv.reader(csv_file))
    assert rows == [["Calculation"], ["2 + 3 = 5"], ["sqrt(16) = 4"]]
