# best: 56(jailctf merger) / others: 59(4atj sisyphus luke Seek mukundan), 59(4atj sisyphus luke Seek), 60(mukundan), 63(xsot ovs att joking mewheni), 69(intgrah jimboko awu macaque sammyuri)
# lambda g:[[a[a[0]==4]for a in zip(a,b[::-1])]for a,b in zip(g,g[::-1])]
# lambda g,R=range(16):[[[g[i][j],g[~i][~j]][g[i][j]==4]for j in R]for i in R]
# lambda g,E=enumerate:[[[v,g[~i][~j]][v==4]for j,v in E(s)]for i,s in E(g)]
# lambda g:[[[x,y][x==4]for x,y in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# lambda g:[[c[c[0]==4]for c in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# lambda g:(a:=sum(g,[]))and[[[v,a.pop()][v==4]for v in s]for s in g]
# f p(g):return(b:=[(a:=g.pop())+[[v,a.pop()][v==4]for v in s]for s in g])+b[::-1]
# ========================= 56 =========================
# lambda g:[(t:=g.pop()*1)and[[a,t.pop()][a==4]for a in s]for s in g*1]
# ↓左右反転だと1ケースだけ中心軸が残る 色は違うからズルできない
# lambda g:[[[a,b][a==4]for a,b in zip(s,s[::-1])]for s in g]
# ↓回転は 2 ケース残る
# lambda g:[[[a,t.pop()][a==4]for a in s]for*t,s in zip(*g,g)]
# lambda g:[[[*{a,b,t.pop()}-{4}][0]for a,b in zip(t,s)]for*t,s in zip(*g,*g,g)]
# lambda g:[[[*{a,t.pop(0),t.pop()}-{4}][0]for a in s]for*t,s in zip(*g,*g,g)]
# lambda g:[[[a,t.pop()][a==4]for a in s]for*t,s in zip(*g,g)]
# lambda g:[[min(*a,key=b"4".find)for a in zip(s,s[::-1])]for s in g]

# lambda g,h=[]:[h,g][h==4]if h*0==0else[*map(p,g,(g+h)[::-1])]
# lambda g,h=[]:h*0==0and[h,g][h==4]or[*map(p,g,(g+h)[::-1])]
# lambda*g:(a:=g[0])*0==0and g[a==4]or[*map(p,a,g[-1][::-1])]
# p=lambda g,h=[]:h*0==0and[h,g][h==4]or[*map(p,g[::-1],h+g)]
# lambda g,h=[]:h*-1and[h,g][h==4]or[*map(p,g[::-1],h+g)]
p=lambda g,h=[]:[h*-1*-1,g][h==4]or[*map(p,g[::-1],h+g)]

# [*{4,h,g}-{4}][0]
# sum({4,h,g})-4
# [h,g][h==4]
