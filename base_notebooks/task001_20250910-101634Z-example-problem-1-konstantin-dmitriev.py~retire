def p(inp):
    out = []
    for y in range(9):
        row = []
        for x in range(9):
            z1 = inp[y // 3][x // 3]
            z2 = inp[y % 3][x % 3]
            z = z1 & z2
            row.append(z)
        out.append(row)
    return out
