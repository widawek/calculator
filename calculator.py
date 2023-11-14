import logging
logging.basicConfig(level=logging.INFO)

operation = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
num1 = float(input('Podaj składnik 1. '))
num2 = float(input('Podaj składnik 2. '))


def calculator(operation, num1, num2):
    if operation == 1:
        logging.info("Dodaję {:.2f} i {:.2f} ".format(num1, num2))
        result = num1 + num2
        print('Wynik to: {:.2f}'.format(result))
    if operation == 2:
        logging.info("Odejmuję {:.2f} i {:.2f} ".format(num2, num1))
        result = num1 - num2
        print('Wynik to: {:.2f}'.format(result))
    if operation == 3:
        logging.info("Mnożę {:.2f} i {:.2f} ".format(num1, num2))
        result = num1 * num2
        print('Wynik to: {:.2f}'.format(result))
    if operation == 4:
        logging.info("Dzielę {:.2f} i {:.2f} ".format(num1, num2))
        result = num1 / num2
        print('Wynik to: {:.2f}'.format(result))


if __name__ == '__main__':
    calculator(operation, num1, num2)
