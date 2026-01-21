import math
import os
from data_loader import loaded_csv_data

def main():
    # Build the correct path to your CSV file
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'shielding_materials.csv')
    materials = loaded_csv_data(filepath)

    print("\nSelect Simulation Mode:")
    print("1️⃣  Simulate all materials")
    print("2️⃣  Simulate single material\n")

    mode = input("Enter 1 or 2: ").strip()

    if mode == "1":
        print("\nMaterial-wise Radiation Transmission (for 10 cm):\n")
        for material, (mu, density) in materials.items():
            mu = float(mu)
            transmission = math.exp(-mu * 10)
            print(f"{material:20s} → {transmission * 100:.4f}% passes through")

    elif mode == "2":
        material_name = input("Enter material name: ").strip().lower()

        # Normalize keys for case-insensitive matching
        matched = None
        for name in materials.keys():
            if name.lower() == material_name:
                matched = name
                break

        if not matched:
            print(f"❌ '{material_name}' not found in database!")
            return

        try:
            thickness = float(input("Enter thickness (cm): "))
        except ValueError:
            print("❌ Invalid thickness! Must be a number.")
            return

        mu, density = materials[matched]
        mu = float(mu)

        transmission = math.exp(-mu * thickness)
        percent = transmission * 100

        print(f"\n📊 Material: {matched}")
        print(f"μ (attenuation coefficient): {mu}")
        print(f"Density: {density} g/cm³")
        print(f"Thickness: {thickness} cm")
        print(f"➡  {percent:.4f}% of radiation passes through")

    else:
        print("❌ Invalid selection! Please choose 1 or 2.")

if __name__ == "__main__":
    main()
