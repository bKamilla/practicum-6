k = int(input('Введите кол-во штук:'))
f = k // 2
if k % 7 == 0 or k % 5 == 0:
    print('да')
    exit()
else:
    for i in range(f):
        for y in range(f):
            if i*5+y*7==k:
                print('да')
                exit()
print('нет')