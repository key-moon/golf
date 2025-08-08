def p(m):
    s=len(m)
    return[[m[i%s][j%s]if m[i//s][j//s]else 0for j in range(s*s)]for i in range(s*s)]
