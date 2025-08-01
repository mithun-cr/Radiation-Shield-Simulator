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

Instructions:

     -Open Command Prompt
     
     - Run cd /*drivename *drivename:Radiation-Shield-Simulator/src
     #Here the *drivename is the name of the drive where the file is extracted to. If you downloaded it to D drive, then cd /d d:Radiation-Shield-Simulator/src p.s. Here I did cd as I was originally on C drive          and had to change to D drive to access files.

     -Run python gui.py and have fun!

     -To customize existing data, head over to 'data' folder in the project file, and then edit the csv file as you wish.

*IMPORTANT*- Always run the individual modules such as GUI, Main, etc. under Radiation-Shield-Simulator\src

My code is currently simulating gamma or X-ray radiation shielding, because these types penetrate materials deeply and they follow Beer’s Law due to interactions like Compton scattering, photoelectric effect, and pair production — all governed by μ.

References:
           https://www.nrc.gov/docs/ML1126/ML11262A163.pdf

![GitHub license](https://img.shields.io/github/license/mithun-cr/radiation-shield-simulator)
![GitHub repo size](https://img.shields.io/github/repo-size/mithun-cr/radiation-shield-simulator)



