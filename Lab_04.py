import numpy as np

Data = np.array([[15.84, 15.87, 15.89, 15.84, 15.88, 0.46, 0.41, 0.39, 0.47, 0.42],
                 [19.06, 19.06, 19.07, 18.99, 19.05, 0.30, 0.33, 0.32, 0.30, 0.29],
                 [22.26, 22.24, 22.20, 22.27, 22.22, 0.42, 0.41, 0.43, 0.43, 0.41]])

Mass = np.array([[0.54], [0.58], [1.07]])

Diameter = np.zeros((3, 1))
for i in range(0,3):
    for j in range(0,1):
        Diameter[i,j] = np.mean(Data[i,0:5])

Thickness = np.zeros((3, 1))
for i in range(0,3):
    for j in range(0,1):
        Thickness[i,j] = np.mean(Data[i,6:10])
        
Volume = 0.001 * 0.25 * np.pi * Thickness * Diameter**2

Density = np.divide(Mass, Volume)

d = np.mean(Density)
d_std = np.std(Density)
print("Average Density: ", d, " g/cm^3")
print("Density Std Dev: ", d_std, " g/cm^3")