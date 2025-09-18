# best: 141(jailctf merger) / others: 148(ox jam), 148(xsot ovs att joking mewheni), 154(4atj sisyphus luke Seek mukundan), 182(natte), 202(intgrah jimboko awu macaque sammyuri)
# =================================================================== 141 ===================================================================
def p(g):
 u=[]
 w=len(g[r:=0])
 for s in g:
  r|=0==len(u)and s[-1]==2
  if r:s.reverse()
  if s[0]==2:
   u+=[k:=[*s,8].index(8)]
   if k<w:s[1:k+1]=[8]*~-k+[4]
  if s[-1]==2 and u.pop(0)<w:s[:w-1]=[8]*(w-1)
  if r:s.reverse()
 return g

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
