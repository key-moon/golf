# best: 122(xsot ovs att joking mewheni, jailctf merger) / others: 130(4atj sisyphus luke Seek), 158(natte), 201(MasukenSamba), 204(Jonas), 206(Ali)
# ========================================================= 122 ==========================================================
p=lambda g:len(g)>3and(f:=sorted([(sum(t:=g[i:i+3],g[0]).count(0),t)for i in range(0,len(g),3)]))[-(f[0][0]==f[1][0])][1]or[*zip(*p([*zip(*g)]))]
#  f=sorted([((g[i]+g[i+1]+g[i+2]).count(0),g[i:i+3])for i in range(0,len(g),3)])


# def p(g):
#  if len(g)<4:
#   return[*zip(*p([*zip(*g)]))]
# #  f=sorted([((g[i]+g[i+1]+g[i+2]).count(0),g[i:i+3])for i in range(0,len(g),3)])
#  f=sorted([(sum(t:=g[i:i+3],g[0]).count(0),t)for i in range(0,len(g),3)])
#  return f[-(f[0][0]==f[1][0])][1]
