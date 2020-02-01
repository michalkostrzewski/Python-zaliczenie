import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression

x = []
y = []

d = int(input("Podaj ile elementów jest w liście: "))

for i in range(0, d):
    x.append(int(input("Podaj wartość elementu x: ")))
    y.append(int(input("Podaj wartość elementu y: ")))
    
xnlist = np.asarray(x)
ynlist = np.asarray(y)
xnlist.reshape(-1,1)

model = LinearRegression()
model.fit(xnlist, ynlist)
model = LinearRegression().fit(x, y)
# plt.scatter(x,y)

# #m = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y)) / (len(x)*np.sum(x*x) - np.sum(x) ** 2)

# sumax = 0
# sumay = 0


 
# for i in range(0, d):
#     wartosc = x[i]
#     sumax = sumax + wartosc
    
# for i in range(0, d):
#     wartosc = y[i]
#     sumay = sumay + wartosc

# # mianownik =

# # a = licznik / mianownik
# # b = np.mean(y) / (a*np.mean(x))


""""""""""""""""Nie rozumiem""""""""""""""""