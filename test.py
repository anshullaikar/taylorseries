import math
import numpy as np
import matplotlib.pyplot as plt

run = True
mains = True


def func_cos(x, n):
    cos_approx = 0
    for k in range(n):
        coef = (-1) ** k
        num = x ** (2 * k)
        denom = math.factorial(2 * k)
        cos_approx += coef * (num / denom)

    return cos_approx


while True:
    angles = np.arange(-2 * np.pi, 2 * np.pi, 0.1).tolist()
    cos = []
    labels = ['cos']
    cos.append(np.cos(angles).tolist())

    plt.figure(figsize=(8, 6))
    plt.ylim([-7, 4])
    plt.plot(angles, cos[0])
    plt.legend(labels, bbox_to_anchor=(1.04, 1), loc="upper left", fontsize=15)
    plt.show()

    while True:
        plt.figure(figsize=(8, 6))
        plt.ylim([-7, 4])

        n = int(input('Enter the number of terms for taylor series or -1 to restart '))
        if n > 0:
            cos.append([func_cos(angle, n) for angle in angles])
            labels.append('n = %a' % n)
            for i in range(len(cos)):
                plt.plot(angles, cos[i])
                plt.legend(labels, bbox_to_anchor=(1.04, 1), loc="upper left", fontsize=15)
            plt.show()

        elif n == -1:
            plt.close()
            break
