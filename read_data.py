import csv

with open("well_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Depth: {row['depth']} m | GR: {row['GR']} | RHOB: {row['RHOB']} | NPHI: {row['NPHI']}")
