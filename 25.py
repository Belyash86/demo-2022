def get_sum(x):
    min_del = max_del = 0
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            min_del = i
            max_del = x // i
            break
    return min_del+max_del

k = 0
chislo = 700001
while k < 5:
    g = get_sum(chislo)
    if g % 10 == 8:
        print(chislo, g)
        k += 1
    chislo += 1