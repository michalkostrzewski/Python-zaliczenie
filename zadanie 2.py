def przelicznik():
    t = float(input('Wprowadź temperaturę: '))
    j = str(input('Podaj jednostkę: '))
    if j == "C":
        return(t * (9/5) + 32)
    if j == "F":
        return((t - 32) * (5/9))