import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def func(x, a, d, b, c):
    return a + d * x + b * x ** 2 + c * x ** 3


deform = []
energy = []
volume = []

with open('AL_2') as f:
    for line in f:
        data = list(map(float, line.split()))
        deform.append(data[3])
        energy.append(data[2])
        volume.append(data[4])

popt, pcov = curve_fit(func, deform, energy)

energy_res = []
for i in range(len(deform)):
    energy_res.append(func(deform[i], *popt))


print(popt)
volOld = np.mean(volume)

C11 = 2 * popt[2] * 1.602 * 10 ** (-19) / (volOld * (10 ** (-10)) ** 3) / 10 ** 9
print('C11 =', C11, 'ГПа')

fig1, graphic1 = plt.subplots()
graphic1.scatter(deform, energy, color="r")
graphic1.plot(deform, energy_res, 'black')

graphic1.set_xlabel(r'$\delta$', fontsize=11)  # подпись горизонтальной оси
graphic1.set_ylabel('E, Дж', fontsize=11)  # подпись вертикальной оси
graphic1.minorticks_on()
graphic1.grid(which='major', color='grey', linewidth=1)
graphic1.grid(which='minor', color='lightgray', linestyle=':')

fig1.set_figwidth(10)
fig1.set_figheight(7)
plt.show()

if __name__ == "__main__":
    sys.exit()
