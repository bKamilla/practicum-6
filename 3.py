a,b=map(int,input('Введите размер района:').split("x"))
c=int(input('Введите кол-во кварталов:'))
S=a*b
if (c%a==0 or c%b==0) and S>c:
    print("успешно")
else:
    print("неосуществимо")