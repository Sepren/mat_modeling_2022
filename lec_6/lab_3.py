import matplotlib.pyplot as plt
import numpy as np
 
def ellips(a, b):
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-15, 15, 0.01)

    X, Y = np.meshgrid(x, y)

    fxy = X ** 2 / a ** 2 + Y ** 2 / b ** 2 - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.savefig('pic_3.png')

a, b = int(input()), int(input())
ellips(a, b)