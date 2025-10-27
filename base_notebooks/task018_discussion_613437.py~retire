def p(m):
    h=len(m)
    w=len(m[0])
    A,C,V=[],[],[]
    V=[]
    for q in [(z//w,z%w)for z in range(h*w)]:
        Y,X=[],[]
        q=[q]
        for y,x in q:
            if w>x>=0<=y<h and (y,x)not in V and m[y][x]:V+=(y,x),;Y+=y,;X+=x,;q+=(y-1,x),(y+1,x),(y,x-1),(y,x+1)
        if len(X)<4:A+=zip(Y,X)
        else:
            H=[r[min(X):max(X)+1]for r in m[min(Y):max(Y)+1]]
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
    G=[w*[0]for r in m]
    for y,x in [(z//w,z%w)for z in range(h*w)]:
        for c in C:
            if sum(I+y<h>0<w>J+x and m[I+y][J+x]==c[I][J] and (I+y,J+x)in A for I,J in [(z//len(c[0]),z%len(c[0]))for z in range(len(c[0])*len(c))])==3:
                for I,J in [(z//len(c[0]),z%len(c[0]))for z in range(len(c[0])*len(c))]:G[I+y][J+x]=c[I][J]
    return G