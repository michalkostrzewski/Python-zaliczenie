import numpy as np

l = []
n = int(input('Podaj ile elementów chcesz wprowadzić: '))

for i in range(0, n):
    l.append(float(input("Podaj liczbę: ")))
    
    
srednia = sum(l)/len(l)
print("Zwykła średnia wynosi: ", srednia)

print("Średnia numpy wynosi: ", np.mean(l))