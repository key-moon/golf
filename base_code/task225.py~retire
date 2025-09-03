def p(g):
    # Locate the 2×2 nonzero block
    for y in range(5):
        for x in range(5):
            if g[y][x] and g[y][x+1] and g[y+1][x] and g[y+1][x+1]:
                sy, sx = y, x
                break
        else:
            continue
        break
    # Corners of the found block
    a = g[sy][sx]       # top‐left → goes to bottom‐right
    b = g[sy][sx+1]     # top‐right → goes to bottom‐left
    c = g[sy+1][sx]     # bot‐left → goes to top‐right
    d = g[sy+1][sx+1]   # bot‐right → goes to top‐left
    # Fill the four quadrants with 2×2 copies of those corners
    for i, j in (0,0),(0,1),(1,0),(1,1):
        y2, x2 = sy-1-i, sx-1-j
        if 0<=y2<6 and 0<=x2<6 and g[y2][x2]==0:
            g[y2][x2] = d
    for i, j in (0,0),(0,1),(1,0),(1,1):
        y2, x2 = sy-1-i, sx+2+j
        if 0<=y2<6 and 0<=x2<6 and g[y2][x2]==0:
            g[y2][x2] = c
    for i, j in (0,0),(0,1),(1,0),(1,1):
        y2, x2 = sy+2+i, sx-1-j
        if 0<=y2<6 and 0<=x2<6 and g[y2][x2]==0:
            g[y2][x2] = b
    for i, j in (0,0),(0,1),(1,0),(1,1):
        y2, x2 = sy+2+i, sx+2+j
        if 0<=y2<6 and 0<=x2<6 and g[y2][x2]==0:
            g[y2][x2] = a
    return g
