a, b = map(str, input('Введите названия клеток(откуда и куда):').split('-'))
if ord(a[0]) + 1 == ord(b[0]) and int(a[1]) + 2 == int(b[1]):
    print('верно')
elif ord(a[0]) - 1 == ord(b[0]) and int(a[1]) + 2 == int(b[1]):
    print('верно')
elif ord(a[0]) + 2 == ord(b[0]) and int(a[1]) + 1 == int(b[1]):
    print('верно')
elif ord(a[0]) + 2 == ord(b[0]) and int(a[1]) - 1 == int(b[1]):
    print('верно')
elif ord(a[0]) + 1 == ord(b[0]) and int(a[1]) - 2 == int(b[1]):
    print('верно')
elif ord(a[0]) - 1 == ord(b[0]) and int(a[1]) - 2 == int(b[1]):
    print('верно')
elif ord(a[0]) - 2 == ord(b[0]) and int(a[1]) + 1 == int(b[1]):
    print('верно')
elif ord(a[0]) - 2 == ord(b[0]) and int(a[1]) - 1 == int(b[1]):
    print('верно')
else:
    print('ошибка')