# best: 77(ox jam) / others: 80(Code Golf International), 80(ALE-Agent), 80(jailctf merger), 81(4atj sisyphus luke Seek mukundan), 81(HIMAGINE THE FUTURE.)
# ==================================== 77 ===================================
# lambda g:(n:=len(g)//2)and[[v and g[0][n]for v in s[:n]+s[n-1::-1]]for s in g[:n]+g[n-1::-1]]
# f p(g):;n=len(g)//2;return[[v and g[0][n]for v in s[:n]+s[n-1::-1]]for s in g[:n]+g[n-1::-1]]
# lambda g,c=-1:c*g or(a:=[*zip(*p([*zip(*g[:len(g)//2])],c+1))])+a[::-1] <- 色変えなし
# lambda g,c=0:g*0!=0and(a:=[*map(p,g[:(i:=len(g)//2)],[g[i]]*9)])+a[::-1]or(g>0)*c
p=lambda g,c=0:g and(c*-1*-1or(a:=[*map(p,g[:(i:=len(g)//2)],[g[i]]*9)])+a[::-1])
