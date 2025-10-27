def p(m):
    w=len(m[0])
    f=sum(m,[])
    d,e,b,c=sorted({*f},key=f.count)
    i=f.index(d)
    o=[f[Y+X]for Y,X in[(i,1),(i,-1),(i+w,0),(i-w,0)]if w>i%w+X>=0<=Y<w*len(m)].count
    for p,v in[*enumerate(f)]:
        for Y,X in(w,1),(w,-1),(-w,-1),(-w,1):
            i=p
            x=p%w
            while v in[d,e]and w>x>=0<=i<w*len(m):
                if f[i]==b:f[i]=[e,d][o(b)>o(c)]
                if f[i]==c:f[i]=[d,e][o(b)>o(c)]
                i+=Y+X
                x+=X
    return[*zip(*w*[iter(f)])]