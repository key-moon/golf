E=enumerate
def p(m):
    f=sum(m,[]);Y,X=divmod(f.index(*[c for c in{*f}if"2, 1, 2"in str([r.count(c)for r in m])!=f.count(c)<6]),len(m))
    for y,r in E(m):
        for x,v in E(r):
            if v:m[a:=2*Y+2-y][b:=2*X+2-x]=m[y][b]=m[a][x]=v
    return m