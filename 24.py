f = open('files/Задание 24/24.txt').readline()
# k_max = 0
# k = 1
# for s in range(len(f)-1):
#     if f[s] == 'P' and f[s+1] == 'P':
#         k_max = max(k_max, k)
#         k = 1
#     else:
#         k += 1
# print(k_max)


f = f.replace('PP','P P')
k_max = 0
for s in f.split():
    k_max = max(k_max,len(s))
print(k_max)