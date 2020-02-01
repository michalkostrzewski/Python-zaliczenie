import numpy as np
import matplotlib.pyplot as plt

def macierz(N):
    return np.random.choice([255, 0], N**2, p=[0, 1]).reshape(N, N)



def szybowiec(i, j ,macierz):
    szybowiec = np.array([[0,0,255],[255,0,255],[0,255,255]])
    
    rx = szybowiec.shape[0]
    ry = szybowiec.shape[1]
    
    macierz[i:i+rx, j:j+ry] = szybowiec
    return macierz



def blok(i, j ,macierz):
    blok = np.array([[255,255],[255,255]])
    
    rx = blok.shape[0]
    ry = blok.shape[1]
    
    macierz[i:i+rx, j:j+ry] = blok
    return macierz



def ul(i, j ,macierz):
    ul = np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
    
    rx = ul.shape[0]
    ry = ul.shape[1]
    
    macierz[i:i+rx, j:j+ry] = ul
    return macierz



def bochenek(i, j ,macierz):
    bochenek = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],[0,0,255,0]])
    
    rx = bochenek.shape[0]
    ry = bochenek.shape[1]
    
    macierz[i:i+rx, j:j+ry] = bochenek
    return macierz



def ludka(i, j ,macierz):
    ludka = np.array([[255,255,0],[255,0,255],[255,0,255]])
    
    rx = ludka.shape[0]
    ry = ludka.shape[1]
    
    macierz[i:i+rx, j:j+ry] = ludka
    return macierz



def blinker(i, j ,macierz):
    blinker = np.array([[0,255,0],[0,255,0],[0,255,0]])
    
    rx = blinker.shape[0]
    ry = blinker.shape[1]
    
    macierz[i:i+rx, j:j+ry] = blinker
    return macierz

def zaba(i, j, macierz):
    zaba = np.array([[255,255,255,0],[0,255,255,255]])
    
    rx = zaba.shape[0]
    ry = zaba.shape[1]
    
    macierz[i:i+rx, j:j+ry] = zaba
    return macierz

    
    
    
    
    
    
    
    