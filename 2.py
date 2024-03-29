a, b = map(float,input('Введите размер отверстия в стене:').split('x'))
c, d, e = map(float,input('Введите размер кирпичей:').split('x'))
if (a >= c and b >= d) or (a >= d and b >= c) or (a >= c and b >= e) or (a >= e and b >= c) or (a >= d and b >= e) or (a >= e and b >= d):
    print('да')
else:
    print('нет')