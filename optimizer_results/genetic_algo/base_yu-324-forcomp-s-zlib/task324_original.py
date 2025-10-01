C=len
B=range
A=sum
def p(g):
 c=sorted({*A(g,[])},key=A(g,[]).count);m={};a=set();b=set()
 for _ in B(2):
  for i in B(C(g)):
   for j in B(C(g[i])):
    if _*g[i][j]in c[:2]:a|={j-i};b|={j+i}
   d={*g[i]}
   if C(d)==2and d&{*c[:2]}:m[A(d&{*c[:2]})]=m[A(d&{*c[2:]})]=A(d&{*c[:2]});d^={*c};m[A(d&{*c[:2]})]=m[A(d&{*c[2:]})]=A(d&{*c[:2]})
  g=[*zip(*g)]
 return[[[g[i][j],m[g[i][j]]][i-j in a or i+j in b]for j in B(C(g[i]))]for i in B(C(g))]