from math import sqrt
a, b = map(float, input('Введите размеры ковровой дорожки:').split('x'))
d = sqrt(a**2 + b**2)
if d > 6.5*2:
    print('нет')
else:
    print('да')