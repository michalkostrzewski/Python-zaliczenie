import matplotlib.pyplot as plt


def wykres(w):
    x = []
    y = []
    print("Proszę pojedyńczo wpisywać argumenty i wartości.")
    for i in range(0, w):
        x.append(float(input('Podaj argument: ')))
        y.append(float(input('Podaj wartość: ')))
    
    plt.plot(x,y)
    plt.title(input("Podaj nazwę wykresu: "))
    
    # e = int(input("Ile elementów chesz wpisać w wykresie? "))
    # for i in range(0, e):
    #     print("zw")
    plt.legend([input("Nazwij linię: ")])
    