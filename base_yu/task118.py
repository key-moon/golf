# best: 271(jailctf merger) / others: 277(4atj sisyphus luke Seek mukundan), 280(kdmitrie), 280(Ali), 280(garrymoss), 285(jacekwl Potatoman nauti)
def p(g):
 B={(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]&2}
 S=3
 while 1:
  c,s,i,j=max((sum((i+~-abs(k-1)*l,j+~-abs(k-2)*l)in B for k in range(4)for l in range(k>0,s)),-s,i,j)for s in range(S,5)for i in range(len(g))for j in range(len(g[0])))
  S=-s
  if c<1:return g
  for k in range(4):
   for l in range(k>0,-s):
    if(i+~-abs(k-1)*l,j+~-abs(k-2)*l)in B:
     B-={(i+~-abs(k-1)*l,j+~-abs(k-2)*l)}
    elif len(g)>i+~-abs(k-1)*l>-1<j+~-abs(k-2)*l<len(g[0]):
     g[i+~-abs(k-1)*l][j+~-abs(k-2)*l]=8
 

# def p(g):
#  h,w=len(g),len(g[0])
#  B=[(i,j)for i in range(h)for j in range(w)if g[i][j]&2]
#  S=3
#  while True:
#   c,s,i,j=max((sum((i+(abs(k-1)-1)*l,j+(abs(k-2)-1)*l)in B for k in range(4)for l in range(k!=0,s)),-s,i,j) for s in range(S,5)for i in range(h)for j in range(w))
#   if c<2:break
#   if s==-4:S=4
#   for k in range(4):
#    for l in range(k!=0,-s):
#     if (i+(abs(k-1)-1)*l,j+(abs(k-2)-1)*l)in B:
#      B.remove((i+(abs(k-1)-1)*l,j+(abs(k-2)-1)*l))
#     elif 0<=i+(abs(k-1)-1)*l<h and 0<=j+(abs(k-2)-1)*l<w:
#      g[i+(abs(k-1)-1)*l][j+(abs(k-2)-1)*l] = 8
#  return g
