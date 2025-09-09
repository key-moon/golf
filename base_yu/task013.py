# best: 140(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 150(xsot ovs att joking mewheni), 161(2F), 161(biz), 169(duckyluuk), 186(HETHAT)
# ================================================================== 140 ===================================================================

p=lambda g:(t:=[*map(max,*g)])[0]+t[-1]and[*zip(*p([*zip(*g)]))]or[(t[:(x:=(u:=[i for i,v in enumerate(t)if v])[0])]+t[x:2*u[1]-x]*9)[:len(t)]]*len(g)

# def p(g):
#  *t,=map(max,*g)
#  if t[0]+t[-1]:
#   return[*zip(*p([*zip(*g)]))]
#  x,y=[i for i,v in enumerate(t)if v]
#  return[(t[:x]+t[x:2*y-x]*9)[:len(t)]]*len(g)

# def p(g):
#  t=[*map(max,*g)]
#  if t[0]+t[-1]:
#   return[*zip(*p([*zip(*g)]))]
# #  (x,y),c=zip(*[t for t in enumerate(t)if t[1]])
# #  t[x::y-x]=(c*99)[:len(t[x::y-x])]
#  x,y=[i for i,v in enumerate(t)if v]
# #  t[x::y-x]=([t[x],t[y]]*9)[:len(t[x::y-x])]
#  t[x:]=(t[x:2*y-x]*9)[:len(t)-x]
#  return[t]*len(g)
# #  return [t[x:2*y-x]]





