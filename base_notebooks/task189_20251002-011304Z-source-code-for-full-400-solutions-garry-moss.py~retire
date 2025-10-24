a=range
f=len
def p(i):
 for s in a(4):
  i=list(map(list,zip(*i[::-1])))
  if i[0][2]==8and i[2][0]==8:
   for s in a(3,f(i)):
    for p in a(3,f(i[0])):
     if i[s][p]>0:
      i[s][p]=i[(s-2)//4][(p-2)//4]
   i=[s[3:] for s in i[3:]]
 return i