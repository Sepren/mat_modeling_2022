import matplotlib.pyplot as plt
import numpy as np

def hyperbola_minus(N, k = 1, title = 'hyperbola plotter'):
    x = np.arange(-0.1, -N, -0.01)
    y = k / x
    plt.plot(x, y, label='my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig('pic_2.png')
    
def hyperbola_plus(N, k = 1, title = 'hyperbola plotter'):
    x = np.arange(0.1, N, 0.01)
    y = k / x
    plt.plot(x, y, label='my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig('pic_2.png')

n = int(input())
hyperbola_minus(n)
hyperbola_plus(n)