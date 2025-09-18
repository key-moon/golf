def p(g):
    n=len(g)
    m=n-1
    out=[row[:] for row in g]
    for i,row in enumerate(g):
        for j,v in enumerate(row):
            if v:
                i2,j2=m-i,m-j
                if v%2:
                    if j<j2:
                        for x in range(j,j2+1,2):
                            out[i][x]=max(out[i][x],v)
                    if i<i2:
                        for y in range(i,i2+1,2):
                            out[y][j]=max(out[y][j],v)
                else:
                    out[i][j]=out[i2][j]=out[i][j2]=out[i2][j2]=max(v,
                        out[i][j],out[i2][j],out[i][j2],out[i2][j2])
    return out