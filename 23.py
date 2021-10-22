def f(start, end):
    if start > end: return False
    if start == end: return True
    return f(start+1, end) + f(start*2, end)

print(f(1,10)*f(10,20))