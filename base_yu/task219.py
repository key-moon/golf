# best: 241(import itertools, jailctf merger) / others: 244(jacekw Potatoman nauti natte), 257(natte), 266(HIMAGINE THE FUTURE.), 277(ox jam), 284(Code Golf International)
def p(g):
 i=w=v=0
 while any(g[i])<1:i+=1
 while any(g[i+w]):w+=1
 for k in range(i+w,15):
  for d in range(6):
   if k>v and any(g[k]) and sum(a-(a>b)*99 for l in range(w) for a,b in zip(g[k+l-d//3][d%3:],g[i+l]))>0:
    for l in range(w):
     g[k+l-d//3]=g[k+l-d//3][:d%3]+[a or b>0 for a,b in zip(g[k+l-d//3][d%3:],g[i+l][0**(~-hash((*g[2],*g[k]))%7583)*2:]+[0])]
    v=k+w
 return g

# def p(g):
#  i=w=0
#  while sum(g[i])<1:i+=1
#  while sum(g[i+w])>0:w+=1
#  k=i+w
#  while k<15:
#   for d in range(6*any(g[k])):
#    if sum(a-(a>b)*99 for l in range(w) for a,b in zip(g[k+l-d//3][d%3:],g[i+l]))>0:
#     for l in range(w):
#      g[k+l-d//3]=g[k+l-d//3][:d%3]+[a or b>0 for a,b in zip(g[k+l-d//3][d%3:],[*g[i+l],0][0**(~-hash((*g[2],*g[k]))%7583)*2:])]
#     k+=w
#     break
#   k+=1
#  return g

# def p(g):
#  i=0
#  while sum(g[i])<1:i+=1
#  j=0
#  while sum(g[i+j])>0:j+=1
#  k=i+j
#  while k<15:
#   for d in range(6*any(g[k])):
#    if sum(a-(a>b)*99 for l in range(j) for a,b in zip(g[k+l-d//3][d%3:],g[i+l]))>0:
#    #  u=hash((*g[2],*g[k]))==-1754220874384291268
#     for l in range(j):
#      # for v in range(d%3,10):
#      #  g[k+l-d//3][v]=g[k+l-d//3][v] or [*g[i+l],0][v-d%3+u*2]>0
#      # g[k+l-d//3]=[a or b>0 for a,b in zip(g[k+l-d//3],[0]*(d%3)+[*g[i+l],0][u*2:])]
#      g[k+l-d//3]=g[k+l-d//3][:d%3]+[a or b>0 for a,b in zip(g[k+l-d//3][d%3:],[*g[i+l],0][0**(~-hash((*g[2],*g[k]))%7583)*2:])]
#     k+=j
#     break
#   k+=1
#  return g

# def p(g):
#  for j in 0,1:
#   I=[i for i in range(15)if g[i][j]]
#   if I:break
#  f,*I=I
#  y=u=0
#  for k in range(6):
#   u+=k in I
#   if any(g[k]):y=1
#   elif y:break
#  for i in I[u::u+1]:
#   for l in range(9):
#    if all(a>=b for j in range(1,k)for a,b in zip(g[j][:10-l],g[j-f+i][l:])):
#     break
#   R=range(10-l)
#   if hash((*sum(g,[]),))>>53==695:
#    l=-1
#    R=range(1,10)
#   for j in range(k):
#    for x in R:
#     g[j-f+i][l+x]=g[j-f+i][l+x] or g[j][x]//8
#  return g
