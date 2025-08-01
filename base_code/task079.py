def p(g):
    m={}
    for i in range(len(g)-2):
        for j in range(len(g[0])-2):
            b={g[i+x][j+y] for x in range(3) for y in range(3) if g[i+x][j+y]}
            if len(b)==1:
                v=b.pop()
                s=tuple((x,y) for x in range(3) for y in range(3) if g[i+x][j+y]==v)
                m[(v,s)]=m.get((v,s),0)+1
    (v,s),_ = max(m.items(), key=lambda t:(t[1],t[0][0]))
    return [[v if (i,j) in s else 0 for j in range(3)] for i in range(3)]
