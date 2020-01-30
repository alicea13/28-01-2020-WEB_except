def staple_test(number):
    pair = 0
    if number:
        staples = 0
        for i in number:
            if i == '(':
                staples += 1
                pair += 1
            if i == ')':
                staples -= 1
            if staples < 0:
                return False
        if staples == 0 and pair == 1:
            return ''.join([j for j in number if j != ")" and j != "("])
    return False


def space(number):
    return ''.join([i.strip() for i in number])


def dash_test(number):
    if not number or '--' in number or number[0] == '-' or number[-1] == '-':
        return False
    return ''.join(number.split('-'))


def start_plus(number):
    if number and (number[0] == '+' or number[0] == '8'):
        if number[0] != "+":
            return "+7" + number[1:]
    return number


def str_numb(number):
    for l in number:
        if l.isalpha() and l not in '-()+':
            return False
    return number


def start():
    get_numb = input()
    numb = dash_test(staple_test(start_plus(str_numb(space(get_numb)))))
    if numb and len(numb) == 12:
        print(numb)
    else:
        print("error")


start()