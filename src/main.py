from data_loader import loaded_csv_data
from simulator import simulate_all_materials
import os

def main():
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'shielding_materials.csv')
    materials = loaded_csv_data(filepath)

    thickness = 5        #in cm
    results = simulate_all_materials(materials, thickness)

    print(f"\nRadiation Transmission for {thickness} cm thickness:\n")
    for material, transmission in results.items():
        percent = transmission * 100
        print(f"{material:<10} ➤  {percent:.4f}% of radiation passes through")

if __name__ == "__main__":
    main()
