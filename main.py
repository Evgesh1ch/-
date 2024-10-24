import matplotlib.pyplot as plt
from math import atan2


x_with_shift = []
y_with_shift = []
sigma11=[]
sigma12=[]
sigma22=[]
countline=1
with open('123') as f:
    for line in f:
        if countline > 9:
            data = list(map(float, line.split()))
            x_with_shift.append(data[0]-198)
            y_with_shift.append(data[1]-182)
            sigma11.append(data[2]/10**4)
            sigma22.append(data[3] / 10 ** 4)
            sigma12.append(data[4] / 10 ** 4)
        countline = countline + 1
angle = []
for i in range(len(x_with_shift)):
    angle.append(atan2(y_with_shift[i], x_with_shift[i]))

fig1, ax1 = plt.subplots()
ax1.scatter(angle, sigma11, s=8, color='green')

fig2, ax2 = plt.subplots()
ax2.scatter(angle, sigma22, s=8, color='blue')

fig3, ax3 = plt.subplots()
ax3.scatter(angle, sigma12, s=8, color='red')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
