# best: 122(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 130(4atj sisyphus luke Seek mukundan), 141(JRKX), 141(jonas ryno kg583 kabutack), 141(jonas ryno kg583), 158(natte)
# ========================================================= 122 ==========================================================
p=lambda g:len(g)>3and(f:=sorted([(sum(t:=g[i:i+3],g[0]).count(0),t)for i in range(0,len(g),3)]))[-(f[0][0]==f[1][0])][1]or[*zip(*p([*zip(*g)]))]
#  f=sorted([((g[i]+g[i+1]+g[i+2]).count(0),g[i:i+3])for i in range(0,len(g),3)])


# def p(g):
#  if len(g)<4:
#   return[*zip(*p([*zip(*g)]))]
# #  f=sorted([((g[i]+g[i+1]+g[i+2]).count(0),g[i:i+3])for i in range(0,len(g),3)])
#  f=sorted([(sum(t:=g[i:i+3],g[0]).count(0),t)for i in range(0,len(g),3)])
#  return f[-(f[0][0]==f[1][0])][1]
