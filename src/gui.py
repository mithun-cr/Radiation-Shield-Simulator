import tkinter as tk
from data_loader import loaded_csv_data
from plotter import plot_intensity
import numpy as np

def start_gui():
    root = tk.Tk()
    root.title("Radiaation Shielding Simulator")
    materials=loaded_csv_data("../data/shielding_materials.csv")
    
    tk.Label(root, text="Choose Material:").pack()
    material_var = tk.StringVar(root)
    material_var.set("Lead")
    dropdown = tk.OptionMenu(root, material_var, *materials.keys())
    dropdown.pack()

    tk.Label(root, text="Max Thickness (cm):").pack()
    thickness_entry = tk.Entry(root)
    thickness_entry.insert(0, "10")
    thickness_entry.pack()

    def on_plot():
        material = material_var.get()
        mu = materials[material]
        try:
            max_thickness = float(thickness_entry.get())
            thickness_values = np.linspace(0, max_thickness, 100)
            plot_intensity(mu, thickness_values)
        except:
            print("Invalid input.")
    def reload():
        nonlocal materials
        materials = loaded_csv_data("../data/shielding_materials.csv")
        material_var.set(next(iter(materials)))
        menu = dropdown["menu"]
        menu.delete(0, "end")
        for mat in materials:
            menu.add_command(label=mat, command=lambda v=mat: material_var.set(v))
            
    tk.Button(root, text="Plot Graph", command=on_plot).pack()
    tk.Button(root, text="Reload Data", command=reload).pack()
    root.mainloop()
if __name__ == "__main__":
    start_gui()
