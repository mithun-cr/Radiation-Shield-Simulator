import math

def calculate_attenuation(mu, thickness):
    return math.exp(-mu * thickness)

def simulate_all_materials(material_data, thickness_cm=5):
    results = {}
    for material, (mu, _) in material_data.items():
        transmission = calculate_attenuation(mu, thickness_cm)
        results[material] = transmission
    return results
