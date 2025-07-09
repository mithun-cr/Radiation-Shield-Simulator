import numpy as np
import matplotlib.pyplot as plt

def plot_intensity(mu, thickness_values):
    I0 = 100
    I = I0 * np.exp(-mu * thickness_values)

    HVL = np.log(2) / mu

    plt.plot(thickness_values, I, label="Theoretical")
    plt.axvline(HVL, color='r', linestyle='--', label=f"HVL = {HVL:.2f}")
    plt.xlabel("Thickness (cm)")
    plt.ylabel("Intensity")
    plt.legend()
    plt.title("Radiation Attenuation Curve")
    plt.grid()
    plt.show()
