import re
def p(g):
 t=""
 t+=str(zip(*(g:=g[::-1])))
 t+=str(zip(*(g:=g[::-1])))
 t+=str(zip(*(g:=g[::-1])))
 t+=str(zip(*(g:=g[::-1])))
 t=re.sub("[[ ,]","",t)
 b=max(t,key=t.count)
 re.findall(f"({b}*){b}",re.sub("[[ ,]","",t))