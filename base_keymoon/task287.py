# best: 56(jailctf merger) / others: 59(luke), 59(4atj sisyphus luke Seek), 60(mukundan), 63(xsot ovs att), 63(att)
# lambda g:[[a[a[0]==4]for a in zip(a,b[::-1])]for a,b in zip(g,g[::-1])]
# lambda g,R=range(16):[[[g[i][j],g[~i][~j]][g[i][j]==4]for j in R]for i in R]
# lambda g,E=enumerate:[[[v,g[~i][~j]][v==4]for j,v in E(s)]for i,s in E(g)]
# lambda g:[[[x,y][x==4]for x,y in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# lambda g:[[c[c[0]==4]for c in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# lambda g:(a:=sum(g,[]))and[[[v,a.pop()][v==4]for v in s]for s in g]
# f p(g):return(b:=[(a:=g.pop())+[[v,a.pop()][v==4]for v in s]for s in g])+b[::-1]
# ========================= 56 =========================
lambda g:(a:=sum(g,[]))+[[[v,a.pop()][v==4]for v in s]for s in g]
