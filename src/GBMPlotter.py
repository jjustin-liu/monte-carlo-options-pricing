import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

'''
    ### GBMPlotter ###

    Plots a given number of stock paths for a set of given parameters, using Geometric Brownian Motion.
'''

IMAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images')


def GBMStockGenerator(s0, mu, sigma, dt, n=1):
    dt_actual = dt / 365
    times = np.arange(0, n, dt_actual)
    intervals = len(times)
    S = np.zeros(intervals)

    z = np.random.standard_normal(intervals - 1)
    dS_s = mu * dt_actual + sigma * z * math.sqrt(dt_actual)

    S[0] = s0
    for i in range(1, intervals):
        S[i] = S[i-1] * (1 + dS_s[i-1])

    return times, S


def main():
    s0, mu, sigma, dt, n = 100, 0.15, 0.25, 1, 4
    stocks = 12

    plt.figure(figsize=(16, 8))
    for s in range(stocks):
        times, exampleStock = GBMStockGenerator(s0, mu, sigma, dt, n)
        plt.plot(times, exampleStock)

    plt.title('Simulated Stock Path(s) Under GBM')
    plt.xlabel('Time/years')
    plt.ylabel('Price')
    plt.grid()

    os.makedirs(IMAGES_DIR, exist_ok=True)
    plt.savefig(os.path.join(IMAGES_DIR, 'stockpaths.png'), dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()
