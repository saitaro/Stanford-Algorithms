def cellular_automaton(s, n, g):
    j, k = [], ['...', '..x', '.x.', '.xx', 'x..', 'x.x', 'xx.', 'xxx']
    for i in range(0,8)[::-1]:
        j.insert(0, n//2**i)
        if n >= 2**i:
            n -= 2**i
    rules = dict(zip(k,['x' if i == 1 else '.' for i in j]))
    for i in range(g):
        d = ''
        for h in range(len(s)):
            d += rules[s[h-1 % len(s)] + s[(h) % len(s)] + s[(h+1) % len(s)]]
        s = d
    return s