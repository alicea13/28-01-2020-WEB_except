letters = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', "sdf", "dfg",
           "fgh", 'ghj', 'hjk', 'jkl', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm', "йцу", "цук", "уке",
           "кен", "енг", "нгш", "гшщ", "шщз", "щзх", "зхъ", "фыв", "ыва", "вап", "апр", "про",
           "рол", "олд", "лдж", "джэ", "ячс", "чсм", "сми", "мит", "ить", "тьб," "ьбю", 'жэё']


def check(password):
    out = "error"
    if len(password) <= 8:
        return out
    if password == password.lower() or password.isupper():
        return out
    if password.isalpha():
        return out
    if not any([i.isdigit() for i in password]):
        return out
    if any([i in password.lower() for i in letters]):
        return out
    return "ok"


print(check(input()))
