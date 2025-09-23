def p(g):
 a=[[*row]for row in zip(*g[::-1])]
 for i in range(len(a)):
  if a[i][0]:q=sum(a[i])//a[i][0];w=a[i][0];a[i]=[0]*15;a[i][q:q+q]=[w]*q
 return [[*row]for row in zip(*a)][::-1]