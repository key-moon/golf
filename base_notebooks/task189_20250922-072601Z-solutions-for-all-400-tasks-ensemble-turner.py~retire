e=range
o=len
def p(i):
 for t in e(4):
  i=list(map(list,zip(*i[::-1])))
  if i[0][2]==8 and i[2][0]==8:
   for t in e(3,o(i)):
    for n in e(3,o(i[0])):
     if i[t][n]>0:
      i[t][n]=i[(t-2)//4][(n-2)//4]
   i=[t[3:] for t in i[3:]]
 return i