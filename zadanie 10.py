import numpy as np

n = int(input('Podaj ile elementów chcesz wprowadzić: '))

l = ([])

for i in range(1, n+1):
    p = float(input('Podal liczbę: '))
    l.append(p)
    
##########################   FUNNKCJE WŁASNE   ################################
    
def srednia(l):
    sr =  sum(l) / len(l)
    return sr

print('Średnia wynosi: {0}'.format(srednia(l)))


def od_sd(l):
    mean = sum(l)/len(l)
    tot = 0.0
    for x in l:
        tot = tot + (x - mean)**2
    return (tot/len(l))**0.5

print('Odchylenie sttandardowe wynosi: {0}'.format(od_sd(l)))


################################# numpy #######################################


print('Średnia Numpy', np.mean(l))
print('Odchylenie standardowe Numpy', np.std(l))