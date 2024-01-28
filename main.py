import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')





type_calc = int(input("Podaj dzialanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie : "))
first_arg = float(input("Podaj składnik 1. "))
second_arg = float(input("Podaj składnik 2. "))


# Sprawdza czy dana wartosc jest liczba

def is_float(self):
    if type(self) is float:
        return True
    else:
        return False

logging.debug("Czy Pierwszy argument jest liczba: %s " % is_float(first_arg))
logging.debug("Czy Drugi argument jest liczba: %s " % is_float(second_arg))



# Kalkulator


def calc(type,first,second):
    if type == 1:
        logging.info("Dodaje %.2f i %.2f" % (first, second))
        return float(first) + float(second)
    elif type == 2:
        logging.info("Odejmuje %.2f i %.2f" % (first, second))
        return float(first) - float(second)
    elif type == 3:
        logging.info("Mnożę %.2f i %.2f"  % (first, second))
        return float(first) * float(second)
    elif type == 4:
        logging.info("Dzielę %.2f i %.2f"  % (first, second))
        return float(first) / float(second)
    else:
        return "Błąd"

    
if __name__ == "__main__":
    print("Wynik to %.2f" % calc(type_calc, first_arg, second_arg))



