import logging
from numpy import prod
logging.basicConfig(level=logging.INFO)


def inputs() -> list:
    try:
        operation = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
        if (operation in list(range(1, 5, 1))):
            pass
        else:
            print("Niepoprawny typ operacji")
            return inputs()
    except ValueError:
        print("Niepoprawny typ operacji")
        return inputs()

    def num_input(counter) -> float:
        try:
            if counter > 2:
                this_input = input(f'Podaj składnik {counter} lub "N" jeżeli nie chcesz dodawać więcej składników. ')
            else:
                this_input = input(f'Podaj składnik {counter}. ')
            if this_input == "N":
                return True
            num = float(this_input)
        except ValueError:
            print("Wprowadź poprawną liczbę.")
            return num_input(counter)
        return num

    if operation in [2, 4]:
        num1 = num_input(1)
        num2 = num_input(2)
        return [operation, num1, num2]
    else:
        args = [operation]
        counter = 1
        while True:
            number = num_input(counter)
            if number is True:
                break
            args.append(number)
            counter += 1
        return args


def calculator(*args) -> None:

    def text_to_log(args):
        to_log = ''
        for arg in args[1:]:
            to_log += '{:.2f}, '.format(arg)
        return to_log[:-2]

    if args[0] == 1:
        logging.info("Dodaję {}".format(text_to_log(args)))
        result = sum(args[1:])
        print('Wynik to: {:.2f}'.format(result))
    if args[0] == 2:
        logging.info("Odejmuję {:.2f} od {:.2f} ".format(args[2], args[1]))
        result = args[1] - args[2]
        print('Wynik to: {:.2f}'.format(result))
    if args[0] == 3:
        logging.info("Mnożę {}".format(text_to_log(args)))
        result = prod(args[1:])
        print('Wynik to: {:.2f}'.format(result))
    if args[0] == 4:
        logging.info("Dzielę {:.2f} przez {:.2f} ".format(args[1], args[2]))
        result = args[1] / args[2]
        print('Wynik to: {:.2f}'.format(result))


if __name__ == '__main__':
    args = inputs()
    calculator(*args)
