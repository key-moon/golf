M=max
m=min
R=range
def p(g):
    from collections import Counter,deque
    b=Counter(x for r in g for x in r).most_common(1)[0][0]
    U,C=len(g),len(g[0])
    S={}
    for i in R(U):
        for j in R(C):
            v=g[i][j]
            if v!=b:S.setdefault(v,set()).add((i,j))
    def cp(T):
        V=set();L=[]
        for s in T:
            if s in V:continue
            q=deque([s]);V.add(s);W={s}
            while q:
                x,y=q.popleft()
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    t=(x+dx,y+dy)
                    if t in T and t not in V:V.add(t);q.append(t);W.add(t)
            L.append(W)
        return L
    def box(T):
        rs=[r for r,c in T];cs=[c for r,c in T]
        return m(rs),m(cs),M(rs),M(cs)
    def nm(T):
        r0,c0,_,_=box(T);return {(r-r0,c-c0)for r,c in T}
    def h(T):
        r0,_,r1,_=box(T);s=r0+r1;return {(s-r,c)for r,c in T}
    def v(T):
        _,c0,_,c1=box(T);s=c0+c1;return {(r,s-c)for r,c in T}
    def d(T):
        r0,c0,_,_=box(T);return {(c-c0+r0,r-r0+c0)for r,c in T}
    def c(T):return v(d(v(T)))
    def cn(T):
        C=[v(T),d(T),c(T),h(T)]
        return m(C,key=lambda U:sorted(nm(U)))
    def man(a,b):return m(abs(x-u)+abs(y-v)for x,y in a for u,v in b)
    def key(v):
        L=cp(S[v])
        W=M((M(c for r,c in w)-m(c for r,c in w)+1 for w in L),default=0)
        ds=[man(L[i],L[j])for i in R(len(L))for j in R(i+1,len(L))]
        G=(m(ds)-1) if ds else -2
        return -(2*W+G)
    cols=sorted(S,key=key)
    shp={v:nm(cn(S[v])) for v in cols}
    n=len(cols)
    D=n if any(len(S[v])==1 for v in cols)else n+1
    s=2*D-1
    o=[[b]*s for _ in R(s)]
    E=[(v,(r+i,c+i))for i,v in enumerate(cols)for r,c in shp[v]]
    def rt(a):return [list(x) for x in zip(*a[::-1])]
    def pa(a):
        for v,(r,c) in E:
            if 0<=r<s and 0<=c<s:a[r][c]=v
        return a
    for _ in R(3):o=pa(o);o=rt(o)
    return pa(o)