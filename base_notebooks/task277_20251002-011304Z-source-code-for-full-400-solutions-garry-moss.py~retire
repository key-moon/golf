def p(j):
 y,y=len(j),len(j[0]);m=[[0]*y for e in j];n=[]
 for e in range(y):
  for t in range(y):
   if j[e][t]==8and not m[e][t]:
    v=[(e,t)];m[e][t]=1;h=[]
    while v:
     e,t=v.pop();h.append((e,t))
     for z in(-1,0,1):
      for o in(-1,0,1):
       if z==o==0:continue
       i,d=e+z,t+o
       if 0<=i<y and 0<=d<y and not m[i][d]and j[i][d]==8:m[i][d]=1;v.append((i,d))
    n.append(h)
 if not n:return[e[:]for e in j]
 def d(i):e=min(e for(e,t)in i);t=min(e for(t,e)in i);return tuple(sorted((i-e,d-t)for(i,d)in i))
 i={}
 for e in n:i.setdefault(d(e),[]).append(e)
 x=min(len(e)for e in i.values());h=[t for(i,e)in i.items()if len(e)==x for t in e]
 def t(i):return min(e for(e,t)in i),min(e for(t,e)in i)
 x=min(h,key=t);i=[e[:]for e in j]
 for e in range(y):
  for t in range(y):
   if i[e][t]==8:i[e][t]=1
 for(e,t)in x:i[e][t]=2
 return i