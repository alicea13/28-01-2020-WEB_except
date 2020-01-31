class CardError(Exception):
    pass


class CardFormatError(CardError):
    pass


class CardLuhnError(CardError):
    pass


def get_card_number():
    card_number = input("Введите номер карты (16 цифр): ")
    card_number = "".join(card_number.strip().split())
    if not (card_number.isdigit() and len(card_number) == 16):
        raise CardFormatError("Неверный формат номера")
    return card_number


def double(x):
    res = x * 2
    if res > 9:
        res = res - 9
    return res


def luhn_algorithm(card):
    print(card)
    odd = map(lambda x: double(int(x)), card[::2])
    even = map(int, card[1::2])

    if (sum(odd) + sum(even)) % 10 == 0:
        return True
    else:
        raise CardLuhnError("Недействительный номер карты")


def process():
    while True:
        try:
            number = get_card_number()
            if luhn_algorithm(number):
                print("Ваша карта обрабатывается...")
                break
        except CardError as e:
            print("Ошибка! %s" % e)


process()