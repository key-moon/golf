L=len
R=range
B=[1,4,9,16,25,36,49,64,81]
S=[-1,0,1]
P=[[x,y]for x in S for y in S]
Z=[264,246,236,194,285,134,156,66,104]
def p(g):
 h,w=L(g),L(g[0])
 X=[[0]*9 for _ in R(9)]
 for r in R(1,h-1):
  for c in R(1,w-1):
    M=[g[r+y][c+x]for y,x in P]
    f=sum([B[i]for i in R(9)if M[i]==5])
    if f in Z and 0 not in M:
     j=Z.index(f)
     for y in R(3):
      for x in R(3):X[y+(j//3*3)][x+(j%3*3)]=g[r-1+y][c-1+x]
 return X