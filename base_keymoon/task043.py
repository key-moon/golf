# best: 57(4atj, att) / others: 58(joking+MWI), 58(Seek64), 58(luke), 58(xsot), 58(sisyphus)
# lambda g:[[[c*a*.08,5][b>4]for b,c in zip(_,g[0][:-1])]+[a]for*_,a in g]
# lambda g:[b:=g[0]]+[[c*a*.08 for c in b[:-1]]+[a]for*_,a in g[1:]]
# lambda g:g[:1]+[[c*a*.08for c in g[0][:9]]+[a]for*_,a in g[1:]]
# ========================== 57 =========================
# lambda g:g[:1]+[[c*a*2&2for c in g[0][:9]]+[a]for*_,a in g[1:]]
# lambda g:[[v+l*t*2%4for l,v in zip(g[0],s)]+[t]for*s,t in g]
# lambda g:[[v+l*t*2%4for l,v in zip(g[0],s)]+[t]for*s,t in g]
p=lambda g:[[v+l*s[9]*2%4for l,v in zip(g[0],s)]for s in g]

# mapping = {(0,0):0, (0,5):0, (5,0):0, (5,5):2, (5,5):2}
