def p(y):
 def e(l,r):
  try:
   if y[l][r]<1:y[l][r]=1;e(l+1,r);e(l-1,r);e(l,r+1);e(l,r-1)
  except:0
 for l in range(len(y)):e(l,0);e(l,-1);e(0,l);e(-1,l)
 return[[(4,0,0,3)[e]for e in e]for e in y]