import matplotlib.pyplot as plt



x_with_shift = []

sigma11=[]

countline=1
with open('sigma_eps.txt') as f:
    for line in f:
        if countline > 1:
            data = list(map(float, line.split()))
            x_with_shift.append(data[0])
            sigma11.append(data[3]/10**4)
        countline = countline + 1
print(x_with_shift, sigma11)
#for i in range(len(x_with_shift)):
 #   angle.append(atan2(y_with_shift[i], x_with_shift[i]))

fig1, ax1 = plt.subplots()
ax1.scatter(x_with_shift, sigma11, s=8, color='green')


ax1.grid()

plt.show()