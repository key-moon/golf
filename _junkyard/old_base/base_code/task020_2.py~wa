def p(g):
    val_m = min(val_j for _ in g for val_j, val_v in enumerate(_) if val_v)
    val_M = max(val_j for _ in g for val_j, val_v in enumerate(_) if val_v)
    val_a = (val_m + val_M)//2
    for _ in g:
        for val_j, val_v in enumerate(_):
            if val_v: _[2*val_a - val_j] = val_v
    return g
