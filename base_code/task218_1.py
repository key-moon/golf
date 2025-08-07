def p(g):
    val_a=[];val_b=[];val_p=None
    for val_i,val_r in enumerate(g):
        for val_j,val_c in enumerate(val_r):
            # is top‐left of a nonzero block?
            if val_c and (val_i<1 or g[val_i-1][val_j]!=val_c) and (val_j<1 or val_r[val_j-1]!=val_c):
                val_a.append((val_i,val_j,val_c))
    val_a.sort()
    for val_y,_,val_c in val_a:
        if val_y!=val_p:
            val_b+=[[]]; val_p=val_y
        val_b[-1]+=[val_c]
    val_m = max(len(r) for r in val_b)
    for val_r in val_b:
        val_r += [val_r[-1]]*(val_m-len(val_r))
    return val_b
