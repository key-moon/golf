def p(g):
 pat=[r[:2]for r in g[:2]]
 res=[]
 for i in range(2):
  row=[]
  for j in range(2):
   row.append(pat[i%2][j%2])
  res.append(row)
 return res
