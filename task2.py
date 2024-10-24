from math import sin, cos, sqrt, tan, factorial, pi, atan2
import numpy as np
import matplotlib.pyplot as plt

mu1 = -0.7084 - 0.7055j
mu2 = 0.7084 - 0.7055j
sigma_inf = 40
a = 36.15 / 2
r = 15


def f1_11(k, theta):
    return (mu2**2 * mu1 ** (((-1) ** (k + 1) + 1) / 2) * (cos(theta) + mu2 * sin(theta)) ** (k / 2 - 1) - mu1 ** 2 * mu2 ** (((-1) ** (k + 1) + 1) / 2) *
            (cos(theta) + mu1 * sin(theta)) ** (
                    k / 2 - 1)) * 1j ** ((k + 1) ** 2) / (mu1 - mu2) * 2


def f1_12(k, theta):
    return (-mu2 * mu1 ** (((-1) ** (k + 1) + 1) / 2) * (cos(theta)
                                                         + mu2 * sin(theta)) ** (
                    k / 2 - 1) + mu1 * mu2 ** (((-1) ** (k + 1) + 1) / 2) *
            (cos(theta) + mu1 * sin(theta)) ** (
                    k / 2 - 1)) * 1j ** ((k + 1) ** 2) / (mu1 - mu2) * 2


def f1_22(k, theta):
    return (mu1 ** (((-1) ** (k + 1) + 1) / 2) * (cos(theta)
                                                  + mu2 * sin(theta)) ** (
                    k / 2 - 1) - mu2 ** (((-1) ** (k + 1) + 1) / 2) *
            (cos(theta) + mu1 * sin(theta)) ** (
                    k / 2 - 1)) * 1j ** ((k + 1) ** 2) / (mu1 - mu2) * 2

def coef_A(k, thet = pi/2):
    if k == 1:
        return sqrt(2*a)/4 * sigma_inf *sin(thet)**2
    elif k == 2:
        return sigma_inf * (cos(thet) ** 2 + ((mu1*mu2).real*sin(thet)**2) + (mu1+mu2).real)/2/(mu1+mu2).imag
    elif k == 3:
        return 3/8 / sqrt(2*a)*sigma_inf*sin(thet)**2
    elif (k % 2 == 0) and (k > 2) :
        return 0
    else:
        n = int((k-3)/2)
        return (-1)**(n+1)*sigma_inf * sin(thet)**2*(-4*factorial(2*n-1)/factorial(2*n)+factorial(2*n+1)/factorial(2*n+2))/(8*(2*a)**(n+1/2))
def sigma11(num_terms, theta):
    res_sum = 0
    for k in range(1, num_terms+1):
        res_sum += coef_A(k)*r**(k/2-1)*f1_11(k, theta)
    return 2 * res_sum.real
def sigma22(num_terms, theta):
    res_sum = 0
    for k in range(1, num_terms + 1):
        res_sum += coef_A(k) * r ** (k / 2 - 1) * f1_22(k, theta)
    return 2 * res_sum.real
def sigma12(num_terms, theta):
    res_sum = 0
    for k in range(1, num_terms + 1):
        res_sum += coef_A(k) * r ** (k / 2 - 1) * f1_12(k, theta)
    return 2 * res_sum.real

angles = np.linspace(-np.pi, np.pi, 500)
num_terms1 = 25
fig11, ax11 = plt.subplots()
ax11.scatter(angles, [sigma11(num_terms1, angle_i) for angle_i in angles], s=8, color='green')
fig22, ax22 = plt.subplots()
ax22.scatter(angles, [sigma22(num_terms1, angle_i) for angle_i in angles], s=8, color='blue')
fig12, ax12 = plt.subplots()
ax12.scatter(angles, [sigma12(num_terms1, angle_i) for angle_i in angles], s=8, color='red')



x_with_shift = []
y_with_shift = []
sigma11_=[]
sigma12_=[]
sigma22_=[]
countline=1
with open('123') as f:
    for line in f:
        if countline > 9:
            data = list(map(float, line.split()))
            x_with_shift.append(data[0]-198)
            y_with_shift.append(data[1]-182)
            sigma11_.append(data[2]/10**4)
            sigma22_.append(data[3] / 10 ** 4)
            sigma12_.append(data[4] / 10 ** 4)
        countline = countline + 1
angle = []
for i in range(len(x_with_shift)):
    angle.append(atan2(y_with_shift[i], x_with_shift[i]))


ax11.scatter(angle, sigma11_, s=8, color='green')


ax22.scatter(angle, sigma22_, s=8, color='blue')


ax12.scatter(angle, sigma12_, s=8, color='red')

plt.show()
