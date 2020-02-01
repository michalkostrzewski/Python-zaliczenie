dni_w_roku = {"Styczeń": 31, "Luty": 28,"Marzec": 31,
              "Kwiecien":30, "Maj":31, "Czerwiec":30,
              "Lipiec":31, "Sierpien":31, "Wrzesien":30,
              "Pazdziernik": 30, "Listopad":30, "Grudzien":31}

def ile_dni_w_roku(miesiac):
    return dni_w_roku[miesiac]
