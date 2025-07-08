import numpy as np
import matplotlib.pyplot as plt

I0 = 100  # Initial intensity

materials = {
    "Lead": 1.24,
    "Concrete": 0.12,
    "Water": 0.09,
    "Polyethylene": 0.06,
    "Steel": 0.50
}

thickness = np.linspace(0, 30, 300)

plt.figure(figsize=(10, 6))

for material, mu in materials.items():
    I = I0 * np.exp(-mu * thickness)
    plt.plot(thickness, I, label=f"{material} (μ={mu})")

plt.title("Radiation Intensity vs Shield Thickness")
plt.xlabel("Thickness (cm)")
plt.ylabel("Remaining Radiation Intensity")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("assets/graph.png")
plt.show()
