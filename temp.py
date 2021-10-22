# при исходном числе 1 результатом
# является число 17 и при этом траектория
# вычислений содержит число 9?
# +1 +3   1--->9  9--->17

def f(start,end):
    if (start == end): return True
    if (start > end) or start == 31: return False
    return f(start+1,end)+f(start*2,end)

print(f(2,15)*f(15,35))