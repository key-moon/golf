def p(a):
    V=[]
    q=[divmod(sum(a,[]).index(1),len(a[0]))]
    for y,x in q:
        if 0<=x<len(a[0]) and 0<=y<len(a) and a[y][x]and(y,x)not in V:V+=(y,x),;q+=(y-1,x),(y+1,x),(y,x-1),(y,x+1)
    Y,X=zip(*V)
    t=[r[min(X):max(X)+1]for r in a[min(Y):max(Y)+1]]
    for k in range(1,4):
        s=t
        s=[r for r in zip(*s)for _ in range(k)]
        s=[r for r in zip(*s)for _ in range(k)]
        for y in range(len(a)-len(s)+1):
            for x in range(-2,len(a[0])-len(s[0])+1):
                if all((y+i,x+j)not in V and(a[y+i][x+j]==2)==(s[i][j]==2)for j in range(len(s[0])) for i in range(len(s))):
                    for j in range(len(s[0])):
                        for i in range(len(s)):
                            if 0<=x+j:a[y+i][x+j]=s[i][j]
    return a