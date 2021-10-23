def f(N):
    R = str(bin(N)[2:])
    for _ in range(2):
        R += str(R.count('1') % 2)
    return(int(R, 2))

for N in range(100):
    if f(N) > 77:
        print(N)
        break