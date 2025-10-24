def p(c):
 d=range;c=[e[:]for e in c];f,p=len(c),len(c[0]);e=[(e,i)for e in d(f)for i in d(p)if c[e][i]==8]
 for(i,h)in e:
  for(a,q)in[(0,1),(1,0),(0,-1),(-1,0)]:
   e=1
   while 0<=i+e*a<f and 0<=h+e*q<p:
    if c[i+e*a][h+e*q]==8:
     for e in d(1,e):c[i+e*a][h+e*q]=3
     break
    e+=1
 return c