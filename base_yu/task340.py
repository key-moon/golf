# best: 119(4atj sisyphus luke Seek mukundan) / others: 122(xsot ovs att joking mewheni), 137(jailctf merger), 162(jacekwl Potatoman nauti), 163(natte), 166(MasukenSamba)
# ======================================================== 119 ========================================================

p=lambda g,c=-3:c*(g[:2]+[s[:2]+[0]*(len(s)-4)+s[-2:] for s in g[2:-2]]+g[-2:])or p([[s[0],max({*s[:2]}&{*s[2:]}),*s[2:]]for s in zip(*g[::-1])],c+1)

# def p(g):
#  for _ in range(4):
#   # g=g[:1]+[[v or max(g[0])*(max(g[0])in s)for*s,v in zip(*g[1:],g[1])]]+g[2:]
#   # g=g[:1]+[[v or(t:=max(g[0]))*(t in s)for*s,v in zip(*g[1:],g[1])]]+g[2:]
#   # g=g[:1]+[[v|max({*g[0]}&{*s})for*s,v in zip(*g[1:],g[1])]]+g[2:]
#   # g=[[s[0],s[1]|(s[0]in s[2:])*s[0],*s[2:]]for s in zip(*g[::-1])]
#   g=[[s[0],max({*s[:2]}&{*s[2:]}),*s[2:]]for s in zip(*g[::-1])]
#  return g[:2]+[s[:2]+[0]*(len(s)-4)+s[-2:] for s in g[2:-2]]+g[-2:]

# def p(g):
#  for _ in(u:=[0])*4:
#   for s in g[1:-1]:
#    if s[0]in s[1:]:s[s.index(s[0],1)],s[1]=0,s[0]
#    u+=[s[0]]
#   *g,=map(list,zip(*g[::-1]))
#  for s in g:
#   for j in range(len(s)):
#    if s[j]not in u:s[j]=0
#  return g


# def p(g):
#  u={0}
#  for _ in[0]*4:
#   for s in g[1:-1]:
#    if s[0]in s[1:]:s[s.index(s[0],1)],s[1]=0,s[0]
#    u|={s[0]}
#   *g,=map(list,zip(*g[::-1]))
#  for s in g:
#   for j in range(len(s)):
#    if not{s[j]}&u:s[j]=0
# #    if u-{s[j]}==u:s[j]=0
#  return g









