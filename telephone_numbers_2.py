class NumberError(Exception):
    pass


class NumberBracketError(NumberError):
    pass


class NumberStartError(NumberError):
    pass


class NumberTireError(NumberError):
    pass




def start(tel):
    out = "error"
    tel = ''.join(tel.strip().split())
    if tel.find("+7") != 0 and tel.find("8") != 0:
        return out
    if "--" in tel or tel[-1] == "-":
        return out
    else:
        tel = tel.replace('-', '')
    left_bracket = tel.find('(')
    right_bracket = tel.find(')')
    if left_bracket > -1:
        if right_bracket < left_bracket or not tel.count('(') == 1 or not tel.count(")") == 1:
            return out
    else:
        if right_bracket > -1:
            return out
    tel = tel.replace("(", '')
    tel = tel.replace(")", '')

    if tel.find('8') == 0:
        tel = "+7" + tel[1:]
    if not (len(tel[1:]) == 11) or not tel[1:].isdigit():
        return out

    return tel



def process():
    while True:
        try:
            number = get_card_number()
            if luhn_algorithm(number):
                print("Ваша карта обрабатывается...")
                break
        except CardError as e:
            print("Ошибка! %s" % e)

print(start(input()))
