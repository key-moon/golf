def p(a):
    n=[]
    f=[divmod(sum(a,[]).index(1),len(a[0]))]
    for y,x in f:
        if 0<=x<len(a[0]) and 0<=y<len(a) and (y,x) not in n and a[y][x]:
            n+=(y,x),
            for i in-1,0,1:
                for j in-1,0,1:f+=(y+i,x+j),
    Y,X=zip(*n)
    o=[]
    H=[r[min(X):max(X)+1]for r in a[min(Y):max(Y)+1]]
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    for y in range(len(a)):
        for x in range(len(a[0])):
            for c in o:
                if all(i+y<len(a) and j+x<len(a[0]) and (a[i+y][j+x]==c[i][j]or c[i][j]%2)for i in range(len(c))for j in range(len(c[0]))):
                    for i in range(len(c)):
                        for j in range(len(c[0])):a[i+y][j+x]=c[i][j]
    return a