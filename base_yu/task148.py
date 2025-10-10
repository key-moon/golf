# best: 140(jailctf merger) / others: 148(ox jam), 153(jacekw Potatoman nauti natte), 153(import itertools), 154(4atj sisyphus luke Seek mukundan), 182(natte)
# ================================================================== 140 ===================================================================
def p(g):
 u=[*filter(max,g)]
 r=u[0][0]<1
 for j,s in enumerate(u):
  if r:s.reverse()
  if 8in s:
   a=s.index(8)
   s[1:a+1]=[8]*~-a+[4]
  if 8in u[j-len(u)//2]:
   s[:-1]=[8]*~-len(g[0])
  if r:s.reverse()
 return g

# def p(g):
#  u=[]
#  w=len(g[r:=0])
#  for s in g:
#   r|=0==len(u)and s[-1]==2
#   if r:s.reverse()
#   if s[0]==2:
#    u+=[k:=[*s,8].index(8)]
#    if k<w:s[1:k+1]=[8]*~-k+[4]
#   if s[-1]==2 and u.pop(0)<w:s[:w-1]=[8]*(w-1)
#   if r:s.reverse()
#  return g

# def p(g):
#  u=[]
#  w=len(g[0])
#  r=0
#  for s in g:
#   r|= len(u)==0 and s[-1]==2
#   if r:
#    s.reverse()
#   if s[0]==2:
#    k=[*s,8].index(8)
#    u.append(k)
#    if k<w:
#     s[1:k]=[8]*(k-1)
#     s[k]=4
#   if s[-1]==2:
#    if u.pop(0)<w:
#     s[:w-1]=[8]*(w-1)
#   if r:
#    s.reverse()
#  return g
