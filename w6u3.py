import random as rnd
import statistics as stat

def gaussian_distribution():
    return [rnd.gauss(100, 10) for _ in range(1000)]

x = gaussian_distribution()

print(
    "Mean:", stat.mean(x), "\n",
    "Standard Deviation:", stat.stdev(x)
)