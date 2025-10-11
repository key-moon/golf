# best: 51(jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 53(4atj sisyphus luke Seek mukundan), 53(biz), 54(import itertools), 55(jonas ryno kg583 kabutack), 55(jacekwl Potatoman nauti)
# ======================= 51 ======================
p=lambda g:[*filter(len,[[*filter(int,s)][::-1]for s in g])]

# p=lambda g:list(filter(len,[[v for v in s if v][::-1]for s in g]))

# S=sorted
# def p(g):
#  h,w=len(g),len(g[0])
#  s=[i for i in range(h*w)if g[i%h][i//h]>0]
#  u,*_,d=S(i%h for i in s)
#  l,*_,r=S(i//h for i in s)
#  return[s[r:l-1:-1]for s in g[u:d+1]]
