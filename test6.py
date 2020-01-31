a = 0

while True:
    try:
        a += 1
    except KeyboardInterrupt:
        res = input('Действительно остановить? ')
        if res == 'yes':
            break