def p(val_g):
    val_a=[c.count(5)for c in zip(*val_g)]
    val_b,max;val_b=max(val_a);val_c=min(val_a)
    return[[(val_v==5)*((val_k==val_b)+(val_k==val_c)*2)
            for val_v,val_k in zip(val_r,val_a)]
           for val_r in val_g]
