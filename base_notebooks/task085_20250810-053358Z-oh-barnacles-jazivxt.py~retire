def p(g):
    r=[row[:]for row in g]
    v=set()
    for i in range(len(g)-2):
        for j in range(len(g[0])):
            if g[i][j]and(i,j)not in v:
                c=g[i][j]
                if all(g[i+k][j]==c for k in range(3)):
                    j2=j
                    while j2<len(g[0])and all(g[i+k][j2]==c for k in range(3)):
                        for k in range(3):v.add((i+k,j2))
                        j2+=1
                    for x in range(j,j2):
                        if(x-j)%2==1:r[i+1][x]=0
    return r
