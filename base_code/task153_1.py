def p(val_g):
    vs={c for r in val_g for c in r if c}
    a=min(vs,key=lambda z:min(i+j for i,r in enumerate(val_g) for j,c in enumerate(r) if c==z))
    b=(vs-{a}).pop()
    S=[(i,j)for i,r in enumerate(val_g) for j,c in enumerate(r) if c==a]
    mr=min(i for i,j in S); mc=min(j for i,j in S)
    R=[[b]*3 for _ in[0]*3]
    for i,j in S: R[i-mr][j-mc]=a
    return R
