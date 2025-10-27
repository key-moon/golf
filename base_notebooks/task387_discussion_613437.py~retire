def p(m):
    (a,A),*_,(b,B)=P=[(y,x)for y,r in enumerate(m)for x,v in enumerate(r)if v]
    for t,(y,x)in enumerate(P):
        for u in-1,0,1:
            for v in-1,0,1:
                if u|v:m[y+u][x+v]=m[a][[B,A][0<t<3]]
    for i in range(2,(b-a)//4*2+1,2):m[a+i][A]=m[a+i][B]=m[b-i][A]=m[b-i][B]=5
    for i in range(2,(B-A)//4*2+1,2):m[a][A+i]=m[a][B-i]=m[b][A+i]=m[b][B-i]=5
    return m