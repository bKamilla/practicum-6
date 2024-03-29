a, b, c = map(int, input('Введите кол-во малышей,кол-во мест в карусели,длительность сеанса:').split())
times = a // b
if a%b > 0:
    times += 1
times = times*2
time = times * c
print(time)
