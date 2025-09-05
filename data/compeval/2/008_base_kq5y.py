# best: 89(mukundan) / others: 94(xsot ovs att joking mewheni), 95(4atj sisyphus luke Seek), 103(natte), 103(jailctf merger), 126(biz)
# ========================================== 89 =========================================

#S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*zip(*p([*zip(*g)]))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*zip(*p([*zip(*g)]))]or S(g[:(i:=g.index(b))],key=max)+S(g[i:],key=max,reverse=1)
