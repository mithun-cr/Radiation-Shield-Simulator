import csv

def loaded_csv_data(filepath):
    material_data = {}
    with open(filepath, 'r',encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            material = row['Material'].strip()
            mu = float(row['Mu'])
            density = float(row['Density'])
            material_data[material] = (mu, density)
    return material_data
