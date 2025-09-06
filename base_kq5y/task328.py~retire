# best: 167(4atj sisyphus luke Seek, 4atj sisyphus luke Seek mukundan) / others: 175(garrymoss), 188(xsot ovs att joking mewheni), 209(jailctf merger), 239(MasukenSamba), 249(jacekwl Potatoman)
# ================================================================================ 167 ================================================================================
#p=lambda g,E=enumerate:(s:=[(i,j,v)for i,r in E(g)for j,v in E(r)if v],[[((d:=[abs(i-x)+abs(j-y)for x,y,_ in s],m:=min(d)),s[d.index(m)][2]*(max(abs(i-s[d.index(m)][0]),abs(j-s[d.index(m)][1]))%2<1)if d.count(m)<2 else 0)[1]for j,_ in E(g[0])]for i,_ in E(g)])[1]
#p=lambda g,E=enumerate:(s:=[(i,j,v)for i,r in E(g)for j,v in E(r)if v],[[((d:=[abs(i-x)+abs(j-y)for x,y,_ in s],m:=min(d)),(c:=s[d.index(m)],c[2]*(max(abs(i-c[0]),abs(j-c[1]))%2<1))[1]if d.count(m)<2 else 0)[1]for j,_ in E(g[0])]for i,_ in E(g)])[1]
#p=lambda g,E=enumerate:(s:=[(i,j,v)for i,r in E(g)for j,v in E(r)if v],[[((d:=[abs(i-x)+abs(j-y)for x,y,_ in s],m:=min(d)),(c:=s[d.index(m)],c[2]*(max(abs(i-c[0]),abs(j-c[1]))%2<1))[1]*(d.count(m)<2))[1]for j,_ in E(g[0])]for i,_ in E(g)])[1]
p=lambda g,E=enumerate,a=abs:[
    [
        (
            s:=[(i,j,v)for i,r in E(g)for j,v in E(r)if v],
            m:=min(d:=[a(i-x)+a(j-y)for x,y,_ in s]),
            c:=s[d.index(m)],
            c[2]*(max(a(i-c[0]),a(j-c[1]))%2+1<2>d.count(m))
        )[3]
        for j,_ in E(r)
    ]
    for i,r in E(g)
]

# def p(g):
#  h,w=len(g),len(g[0]);s=[(i,j,g[i][j])for i in range(h)for j in range(w)if g[i][j]];o=[[0]*w for _ in range(h)]
#  for i in range(h):
#   for j in range(w):
#    d=[abs(i-x)+abs(j-y)for x,y,_ in s];m=min(d)
#    if d.count(m)==1:
#     x,y,v=s[d.index(m)]
#     if max(abs(i-x),abs(j-y))%2<1:o[i][j]=v
#  return o
