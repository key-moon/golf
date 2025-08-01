def p(g):
    M,N=len(g),len(g[0])
    for i in range(M):
        for j in range(N):
            x=g[i][j]
            if x:
                dr=dc=cnt=0
                for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
                    if 0<=i+di<M and 0<=j+dj<N and g[i+di][j+dj]==x:
                        dr+=di; dc+=dj; cnt+=1
                if cnt==2:
                    t=1
                    while 1:
                        t+=1
                        a,b=i+dr*t,j+dc*t
                        if a<0 or a>=M or b<0 or b>=N: break
                        if not g[a][b]: g[a][b]=x
    return g