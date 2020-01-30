try:
    numb = int(input("Введите целое число: "))
    print(numb + 10)
except ValueError as error:
    print("Неверное число")
    print(error)
    print(dir(error))