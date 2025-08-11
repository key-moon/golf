def p(m,k=range):
 s,n=next((j,v)for j,v in enumerate(m[-1])if v)
 o=[[0]*10 for _ in k(10)]
 for i in k(10):
  for j in k(s,10):
   d=j-s
   if d%2==0:o[i][j]=n
   elif(i==0 and d%4==1)or(i==9 and d%4==3):o[i][j]=5
 return o