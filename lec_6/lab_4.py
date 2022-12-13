import matplotlib.pyplot as plt
import numpy as np

# def log_spiral(b):
#     fi = np.arange(0, 8 * np.pi, 0.01)
#     r = np.e ** (b * fi)
#     x = r * np.cos(fi)
#     y = r * np.sin(fi)
    	
#     plt.plot(x, y, label='my log_spiral')
#     plt.xlabel('coord - x')
#     plt.ylabel('coord - y')
#     #plt.title(title)
#     plt.legend()
#     plt.savefig('pic_4.png')

# def archimed_spiral(k):
#     fi = np.arange(0, 8 * np.pi, 0.01)
#     r = k * fi
#     x = r * np.cos(fi)
#     y = r * np.sin(fi)

#     plt.plot(x, y, label='my archimed_spiral')
#     plt.xlabel('coord - x')
#     plt.ylabel('coord - y')
#     #plt.title(title)
#     plt.legend()
#     plt.savefig('pic_5.png')

def wand(k):
    fi = np.arange(0.1, 8 * np.pi, 0.01)
    r = k / np.sqrt(fi)
    x = r * np.cos(fi)
    y = r * np.sin(fi)

    plt.plot(x, y, label='my wand')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    #plt.title(title)
    plt.legend()
    plt.savefig('pic_6.png')

def rose(k):
    fi = np.arange(0, 8 * np.pi, 0.01)
    r = np.sin(k * fi)
    x = r * np.cos(fi)
    y = r * np.sin(fi)

    plt.plot(x, y, label='my wand')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    #plt.title(title)
    plt.legend()
    plt.savefig('pic_7.png')


k = float(input())
rose(k)
