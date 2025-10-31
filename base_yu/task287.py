# best: 53(Code Golf International) / others: 55(ox jam), 56(jailctf merger), 56(HIMAGINE THE FUTURE.), 58(lv1.dev), 59(4atj sisyphus luke Seek mukundan)
# ======================== 53 =======================
# p=lambda g,R=range(16):[[[g[i][j],g[~i][~j]][g[i][j]==4]for j in R]for i in R]
# p=lambda g,E=enumerate:[[[v,g[~i][~j]][v==4]for j,v in E(s)]for i,s in E(g)]
# p=lambda g:[[[x,y][x==4]for x,y in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# p=lambda g:[[c[c[0]==4]for c in zip(s,t[::-1])]for s,t in zip(g,g[::-1])]
# p=lambda g:(a:=sum(g,[]))and[[[v,a.pop()][v==4]for v in s]for s in g]
p=lambda g:(a:=sum(g,[]))+[[[v,a.pop()][v==4]for v in s]for s in g]
