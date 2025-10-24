e=len
n=range
def p(p):
 f,c=[],0;d,a=e(p),e(p[0])
 for r in n(2):
  p=[r[::-1]for r in p]
  if p[4][0]==2:
   for r in n(d):
    o=0
    for g in n(a):
     if p[r][g]>0and o:p[r][g]=4;o=0
     elif p[r][g]==2and p[r].count(8)>0and p[r].count(4)<1:o=1
     if o and p[r][g]==0:p[r][g]=8
    if p[r][0]==2:
     if p[r].count(4)>0:f+=[1]
     else:f+=[0]
    if p[r][-1]==2:
     if f[c]:p[r]=[8]*(a-1)+[2]
     c+=1
 return p