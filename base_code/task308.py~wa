def p(g):
    # find background = most frequent color
    val_bg = max({c for r in g for c in r},
                 key=lambda c: sum(row.count(c) for row in g))
    # dims and integer center
    val_h, val_w = len(g), len(g[0])
    val_cy, val_cx = val_h//2, val_w//2
    # collect all non-bg cells with their offsets
    val_ds = [(y - val_cy, x - val_cx, g[y][x])
              for y in range(val_h) for x in range(val_w)
              if g[y][x] != val_bg]
    if not val_ds:
        return [[val_bg]]
    # radius = max distance in either direction
    val_K = max(max(abs(dy), abs(dx)) for dy,dx,_ in val_ds)
    # build & fill
    val_o = [[val_bg] * (2*val_K+1) for _ in range(2*val_K+1)]
    for dy, dx, c in val_ds:
        val_o[dy+val_K][dx+val_K] = c
    return val_o
