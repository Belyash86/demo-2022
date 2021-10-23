from functools import lru_cache
def moves(h):
    return h+1, h*2

@lru_cache(None)
def game(h):
    if h >= 29: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'P1'
    if all(game(x) == 'P1' for x in moves(h)): return 'V1'
    if any(game(x) == 'V1' for x in moves(h)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(h)): return 'V2'

for s in range(1, 28+1):
    g = game(s)
    if g != None:
        print(s, g)