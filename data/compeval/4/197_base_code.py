def p(g):
    # Find the “template” row: the one with no zeros
    b = next(r for r in g if 0 not in r)
    # Record its two distinct values in left‐to‐right order
    c = []
    for x in b:
        if x not in c:
            c += [x]
    # For each other row that has some zeros but also nonzeros,
    # learn its two nonzero values in order and fill by mapping the template
    for r in g:
        s = []
        for x in r:
            if x and x not in s:
                s += [x]
        if s and 0 in r:
            for i, x in enumerate(b):
                r[i] = s[c.index(x)]
    return g
