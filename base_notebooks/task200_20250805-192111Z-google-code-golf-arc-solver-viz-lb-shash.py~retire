def p(m,R=range):
 s,n=next((j,v)for j,v in enumerate(m[-1])if v);o=[[0]*10 for _ in R(10)]
 for i in R(10):
  for j in R(s,10):
   d=j-s
   if d%2==0:o[i][j]=n
   elif(i==0and d%4==1)or(i==9and d%4==3):o[i][j]=5
 return o