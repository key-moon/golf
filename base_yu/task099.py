# best: 131(jailctf merger) / others: 140(4atj sisyphus luke Seek), 150(xsot ovs att joking mewheni), 184(Potatoman), 186(natte), 196(Jonas)
# ============================================================== 131 ==============================================================
def p(g):
 w=1-any(g[1])
 u=g[w:]
 return(len(g)<6)*(g[:w]+[[v or any(t)*max(sum(g,[]))for*t,v in zip(*u,s)]for s in u])or p(g[:5])+p(g[5:])

# def q(g):
#  w=1-any(g[1])
#  u=g[w:]
#  return g[:w]+[[v or any(t)*max(sum(u,[]))for*t,v in zip(*u,s)] for s in u]
# def p(g):
#  return q(g[:5])+q(g[5:])
