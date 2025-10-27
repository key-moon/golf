def p(m):
    _,Y,X,t=min([(sum(t:=[r[x:x+3]for r in m[y:y+3]],m).count(0),y,x,t)for y in range(19)for x in range(19)])
    for a in-4,0,4:
        for b in-4,0,4:
            for k in range(1,19):
                y=Y+a*k
                x=X+b*k
                for i in range(3):
                    for j in range(3):
                        if a|b!=0<=x+j<21>y+i>=0:m[y+i][x+j]=t[i][j]and max(max(r[X+b:X+b+3])for r in m[Y+a:Y+a+3])
    return m