import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.stats import skew, kurtosis


randomNums = np.random.normal(scale=3, size=1000)
randomInts = np.round(randomNums)
axis = np.arange(start=min(randomInts), stop = max(randomInts) + 1)
plt.hist(randomInts, bins = axis)

srednia = np.mean(randomInts)
mediana = np.median(randomInts)
dominanta = statistics.mode(randomInts)
od_st = np.std(randomInts)
wariancja = statistics.variance(randomInts)
skosnosc = skew(randomInts)
kurtoza = kurtosis(randomInts)

print("Średnia: ",srednia)
print("Mediana: ",mediana)
print("Dominanta: ",dominanta)
print("Odchylenie ",od_st)
print("Wariancja ",wariancja)
print("Skośność ",skosnosc)
print("Kurtoza ",kurtoza)






