def Silnia_R(n):
    if (n==1):
        return 1
    else:
        return n * Silnia_R(n-1)
    
    
def Silnia_I(n):
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s


m = input('Jaką metodą chcesz znaleźć silnię? R - rekurencyjna. I - iteracyjna. ')


if (m == 'R'):
    n = int(input('Podaj liczbę: '))
    wynik = Silnia_R(n)
    print(wynik)

if (m == 'I'):
    n = int(input('Podaj liczbę: '))
    wynik = Silnia_I(n)
    print(wynik)

elif(m != 'R', 'I'):
    print("Podano niewłaściwe dane")
