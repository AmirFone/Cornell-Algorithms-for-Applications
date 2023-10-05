import sys
sys.path.append(".")

import numpy as np
import math
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from challenge import reference_multiply, karatsuba, fft


def timeit(fn, *args):
    n_trials = 5
    times = []
    for _ in range(n_trials):
        start = time.time()
        fn(*args)
        times.append(time.time() - start)
    return np.mean(times)


if __name__ == "__main__":
    x = [2,4,8,16,32,64,128,256,512]

    y1 = [timeit(reference_multiply, [0 for _ in range(i)], [0 for _ in range(i)]) for i in x]
    y2 = [timeit(karatsuba, [0 for _ in range(i)], [0 for _ in range(i)]) for i in x]
    y3 = [timeit(fft, [0 for _ in range(i)], [0 for _ in range(i)]) for i in x]

    xs = x + x + x
    ys = y1 + y2 + y3
    algorithms = ["Reference"] * len(x) + ["Karatsuba"] * len(x) + ["FFT"] * len(x)

    df = pd.DataFrame({"n": xs, "time": ys, "algos": algorithms})
    sns.lineplot(data = df, x="n", y="time", hue="algos")

    plt.xlabel('Array size')
    plt.ylabel('Time (s)')
    plt.title('Empirical analysis of integer multiplication')
    plt.legend()

    plt.savefig("challenge_empirical_analysis.png", bbox_inches="tight")



