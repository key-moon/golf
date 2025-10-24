# best: 114(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 122(biz), 125(ox jam), 126(2F), 130(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 133(intgrah jimboko awu macaque sammyuri)
# ===================================================== 114 ======================================================
# p=lambda g:max([[s[l%20:[*g[l//20],0].index(0,l%20)]for s in g[l//20:[*[g[k][l%20]for k in range(20)],0].index(0,l//20)]]for l in range(400)],key=lambda t:sum(t,[]).count(2))
# p=lambda g:max([(sum(t:=[s[l%20:[*g[l//20],0].index(0,l%20)]for s in g[l//20:[*[g[k][l%20]for k in range(20)],0].index(0,l//20)]],[]).count(2),~l,t)for l in range(400)])[2]
# p=lambda g:max([(sum(t:=[s[l%20:[*g[l//20],0].index(0,l%20)]for s in g[l//20:[*[*[*zip(*g)][l%20]],0].index(0,l//20)]],[]).count(2),~l,t)for l in range(400)])[2]
# p=lambda g:max((all(y:=sum(x:=[s[l:r]for s in g[u:d]],[])),y.count(2),len(y),x)for r in range(21)for l in range(r)for d in range(21)for u in range(d))[3]
# p=lambda g:max((all(y:=sum(x:=[s[l:t%21]for s in g[u:t//21]],[])),y.count(2),len(y),x)for t in range(441)for l in range(t%21)for u in range(t//21))[3]
p=lambda g,c=-3:c*g or min(("0"in(y:=str(x:=p([*zip(*g[l::-1])],c+1))),-y.count("2"),-len(y),x)for l in range(len(g)))[3]


# def p(g):
#  V=0
#  T=[]
#  for l in range(20):
#   for u in range(20):
#    r=[*g[u],0].index(0,l)
#    d=[*[g[k][l]for k in range(20)],0].index(0,u)
#    t=[s[l:r] for s in g[u:d]]
#    v=sum(t,[]).count(2)
#    if V<v:
#     V=v
#     T=t
#  return T
