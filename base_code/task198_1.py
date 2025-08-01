def p(val_g):
    val_v=next(x for r in val_g for x in r if x)
    val_h=[i for i,r in enumerate(val_g) if r.count(val_v)>len(r)/2]
    val_w=len(val_g[0])
    val_c=[j for j in range(val_w) if sum(r[j]==val_v for r in val_g)>len(val_g)/2]
    val_h=[-1]+val_h+[len(val_g)]
    val_c=[-1]+val_c+[val_w]
    for val_i in range(len(val_h)-1):
        for val_j in range(len(val_c)-1):
            val_s=3 if (val_i+val_j)%2==0 else 4
            for val_r in range(val_h[val_i]+1,val_h[val_i+1]):
                for val_k in range(val_c[val_j]+1,val_c[val_j+1]):
                    if val_g[val_r][val_k]==0: val_g[val_r][val_k]=val_s
    return val_g
