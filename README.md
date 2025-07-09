# Radiation-Shield-Simulator
Simulates attenuation of radiation through materials using exponential decay laws.

This project is intended to study the properties of radioactive shielding properties exhibited by various materials (lead, concrete, water, polyethylene, and steel).

Theory:

This project makes use of the Radiation Attenuation Equation, 

I=I0 * e^-(μx), 

where

I= Transmitted radiational intensity
I0= Initial intensity
μ= Linear attenuation coefficient (material-specific, unit: cm⁻¹)
x= Thickness of the absorbing material (in cm)

Attenuation Coefficient Of Materials Used(cm^-1):

Lead= 1.24
Concrete= 0.12
Water= 0.09
Polyethylene= 0.06
Steel= 0.50

Output:

A beautiful, illustrative graph is plotted, which shows how radiation intensity drops with increasing thickness.

*IMPORTANT*- Always run the individual modules such as GUI, Main, etc. under Radiation-Shield-Simulator\src

My code is currently simulating gamma or X-ray radiation shielding, because these types penetrate materials deeply and hey follow Beer’s Law due to interactions like Compton scattering, photoelectric effect, and pair production — all governed by μ.


![GitHub license](https://img.shields.io/github/license/mithun-cr/radiation-shield-simulator)
![GitHub repo size](https://img.shields.io/github/repo-size/mithun-cr/radiation-shield-simulator)



