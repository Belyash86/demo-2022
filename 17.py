f = open('files/Задание 17/17.txt')
max_sum = 0
k = 0
p1 = int(f.readline())
for i in range(4999):
    p2 = int(f.readline())
    if p1%3 == 0 or p2%3 == 0:
        k += 1
        max_sum = max(max_sum,p1+p2)
    p1 = p2 #для p2 будем брать новое значение из файла, старое запишем в предыдущи элемент пары
print(k, max_sum)