letters = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', "sdf", "dfg",
           "fgh", 'ghj', 'hjk', 'jkl', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm', "йцу", "цук", "уке",
           "кен", "енг", "нгш", "гшщ", "шщз", "щзх", "зхъ", "фыв", "ыва", "вап", "апр", "про",
           "рол", "олд", "лдж", "джэ", "ячс", "чсм", "сми", "мит", "ить", "тьб," "ьбю", 'жэё']


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check(password):
    if len(password) <= 8:
        raise LengthError
    if password == password.lower() or password.isupper():
        raise LetterError
    if password.isalpha():
        raise DigitError
    if not any([i.isdigit() for i in password]):
        raise DigitError
    if any([i in password.lower() for i in letters]):
        raise SequenceError
    else:
        return 'ok'


def check_password(password):
    try:
        return check(password)
    except LengthError:
        return "LengthError"
    except LetterError:
        return "LetterError"
    except DigitError:
        return "DigitError"
    except SequenceError:
        return "SequenceError"


