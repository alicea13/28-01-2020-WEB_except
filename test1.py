print(''.join('1 2  3   4   '.split()))

def get_card_number():
    card_number = input("Введите номер карты (16 цифр): ")

    card_number = "".join(card_number.strip().split())
    if card_number.isdigit() and len(card_number) == 16:
        return card_number
    else:
        return 404


def double(x):
    res = x * 2
    if res > 9:
        res = res - 9
    return res


def luhn_algorithm(card):
    odd = map(lambda x: double(int(x)), card[::2])
    even = map(int, card[1::2])

    return (sum(odd) + sum(even)) % 10 == 0


def process():
    while True:
        number = get_card_number()
        if number == 404:
            print("Введите только 16 цифр. Допускаются пробелы")
            continue
        if luhn_algorithm(number):
            print("Ваша карта обрабатывается...")
            break
        else:
            print("Номер недействителен. Попробуйте снова.")

process()