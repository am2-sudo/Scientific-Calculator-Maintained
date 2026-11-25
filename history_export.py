import csv
from pathlib import Path

def export_history(entries, destination):
    """Export calculation history entries to a UTF-8 CSV file."""
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Calculation"])
        writer.writerows([[entry] for entry in entries])
    return destination
