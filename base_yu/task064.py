# best: 152(jailctf merger, xsot ovs att joking mewheni) / others: 155(4atj sisyphus luke Seek mukundan), 163(duckyluuk), 191(jonas ryno kg583), 191(JRK), 200(natte)

import re
def p(g):
 u=sum(g,g[5])
 c,d,e=sorted({*u},key=u.count)
#  for _ in g*8:
#   g=[*zip(*eval(re.sub(r"(?<=%d, )%d(?=(, \d)*, %d)"%(c,e,d),str(c),str(g)))[::-1])]
#   g=[*zip(*eval(re.sub(f"(?<={c}, ){e}(?=(, \d)*, {d})",str(c),str(g)))[::-1])]
 return eval('(g:=[*zip(*eval(re.sub(f"(?<={c}, ){e}(?=(, \d)*, {d})","c",str(g)))[::-1])]),'*80)[-1]
 

# def p(g):
#  b=(g[0][0]-1 or g[0][2]-1)+1
#  for _ in[0]*4:
#   h,w=len(g),len(g[0])
#   for i in range(h*w):
#    c=g[i%h][i//h]
#    G=[k for k in range(w)if g[i%h][k]not in (c,b)]
#    if(c!=b)*(len(G)>2):g[i%h][i//h:G[0]]=[c]*(G[0]-i//h)
#   *g,=map(list,zip(*g[::-1]))
#  return g




