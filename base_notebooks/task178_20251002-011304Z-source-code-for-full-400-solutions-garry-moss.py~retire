def p(g):
 p=range;t,f=len(g),len(g[0]);e=[]
 for y in p(t):
  if y==0 or g[y]!=g[y-1]:e.append([g[y][0]])
 y=[];i=-1
 for f in p(f):
  if f==0 or any(g[y][f]!=g[y][f-1]for y in p(t)):y.append(g[0][f])
 if len(e)>1:return e
 else:return[y]