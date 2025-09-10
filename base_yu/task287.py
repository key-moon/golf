# best: 56(jailctf merger) / others: 59(4atj sisyphus luke Seek mukundan), 63(xsot ovs att joking mewheni), 69(intgrah jimboko awu macaque sammyuri), 73(jonas ryno kg583), 75(jacekwl Potatoman nauti)
# ========================= 56 =========================
# p=lambda g,R=range(16):[[[g[i][j],g[~i][~j]][g[i][j]==4]for j in R]for i in R]
# p=lambda g,E=enumerate:[[[v,g[~i][~j]][v==4]for j,v in E(s)]for i,s in E(g)]
# p=lambda g:[[[x,y][x==4]for x,y in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# p=lambda g:[[c[c[0]==4]for c in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# p=lambda g:(a:=sum(g,[]))and[[[v,a.pop()][v==4]for v in s]for s in g]
p=lambda g:(a:=sum(g,[]))+[[[v,a.pop()][v==4]for v in s]for s in g]







