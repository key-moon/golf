# def p(g):
#  R=range;F=sum(g,l:=[]);G=[];P=[[]];W=15
#  for x in R(16):
#   if(5in F[x::W])>x/W:G+=[x]
#   elif G:A=[z for z in R(150)if z%W in G*(F[z]&5)];l+=[[z-A[0]for z in A]];G=[];P=[c+[a]for c in P for a in R(45)if F[a]<1]
#  for c in P:
#   O=[any(z-x in h*(x%W-z%W<6)for x,h in zip(c,l))|F[z]%5for z in R(150)]
#   if all(O[:45])&(O.count(0)==F.count(0)):return[O[i*W:][:W]for i in R(10)]

def p(p):
 a=sum(p,e:=[]);p=[];n=[[]];r=15
 for i in range(16):
  if(5in a[i::r])>i/r:p+=[i]
  elif p:i=[n for n in range(150)if a[n]>4and n%r in p];e+=[[n-i[0]for n in i]];p=[];n=[i+[n]for i in n for n in range(45)if 1>a[n]]
 for i in n:
  i=[any(n-i in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in range(150)]
  if all(i[:45])*(i.count(0)==a.count(0)):return[i[n*r:][:r]for n in range(10)]