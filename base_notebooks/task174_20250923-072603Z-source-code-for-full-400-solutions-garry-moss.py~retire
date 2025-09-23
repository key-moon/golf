def p(g):
    n=len(g)
    def f(i,j):
        if n>i>=0<=j<n and g[i][j]==k and(i,j)not in s:
            s.add((i,j));[f(i+y,j+x)for y in(-1,0,1) for x in(-1,0,1) if y|x]
    for i in range(n):
        for j in range(n):
            if(k:=g[i][j]):
                s=set();f(i,j);Y,X=zip(*s);a,b=min(Y),max(Y);c,d=min(X),max(X);S=[r[c:d+1]for r in g[a:b+1]]
                if S==[r[::-1]for r in S]:return S