# best: 110(jailctf merger) / others: 117(4atj sisyphus luke Seek mukundan), 117(4atj sisyphus luke Seek), 120(xsot ovs att joking mewheni), 154(mukundan), 197(natte)
# =================================================== 110 ====================================================

# p=lambda g,c=-7:c*g or (d:=min(u:=sum(g,g[0]),key=u.count))and p([*zip(*[(l:=0)or[((x+(d==x>0<l==y)*(l-x))*(c<0 or x!=d),l:=x)[0]for x,y in zip(s,t)]for s,t in zip(g,g[:1]+g)][::-1])],c+1)
# p=lambda g,c=-7:c*g or (d:=min(u:=sum(g,g[0]),key=u.count))and p([*zip(*[(l:=0)or[((c<0 or x!=d)*(x+(d==x>0<l==y)*(l-x)),l:=x)[0]for x,y in zip(s,t)]for s,t in zip(g,g[:1]+g)][::-1])],c+1)
# p=lambda g,c=-7:c*g or (d:=min(u:=sum(g,g[0]),key=u.count))and p([*zip(*[(l:=0)or[((d==x>0<l==y)*(l-x)+(l:=x))*(c<0 or x!=d)for x,y in zip(s,t)]for s,t in zip(g,g[:1]+g)][::-1])],c+1)

# p=lambda g,c=-7:c*g or (d:=min(u:=sum(g,g[0]),key=u.count))and p([*zip(*[(l:=0)or[((x+(0<l==y!=x>0)*(l-x))*(c<0 or x!=d),l:=x)[0]for x,y in zip(s,t)]for s,t in zip(g,g[:1]+g)][::-1])],c+1)
# p=lambda g,c=-7:c*g or (d:=min(u:=sum(g,g[0]),key=u.count))and p([*zip(*[(l:=0)or[((x+(0<l==y!=x>0)*(l-x))*(c<0 or x!=d),l:=(x==y)*x)[0]for x,y in zip(s,t)]for s,t in zip(g,g[:1]+g)][::-1])],c+1)
# p=lambda g,c=-7:c*g or p([*zip(*[(l:=0)or[(((0<l==t[i]!=s[i]>0)*l or s[i])*(c+1<0 or max([0,*s,0][i:i+3:2])>0),l:=(s[i]==t[i])*s[i])[0]for i in range(len(s))]for s,t in zip(g,g[:1]+g)][::-1])],c+1)
p=lambda g,c=-7:c*g or p([*zip(*[[((s[i]>0<t[i-1]==t[i])*t[i]or s[i])*(c<-1 or max([0,*s,0][i:i+3:2])>0)for i in range(len(s))]for s,t in zip(g,g[:1]+g)][::-1])],c+1)

# import re
# def p(g):
#  c,b,a=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for _ in range(4):
#   g=eval(re.sub(f"{c}(?=, {b}.{{{len(g)*3-2}}}{b})",str(b),str([*zip(*g[::-1])])))
#  g=eval(str(g).replace(str(c),"0"))
#  return g

# def p(g):
#  c,b,a=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for i in range(len(g)):
#   for j in range(len(g[0])):
#    if g[i][j]==c:
#     u=0
#     for k in range(9):
#      if len(g)>(y:=i+k//3-1)>-1<(x:=j+k%3-1)<len(g[0]) and g[y][x]!=a:
#       u+=k%2+1
#       u|=(k%6==1)*16|(k in(3,5))*32
#     g[i][j]=[a,b][u>52]
#  return g


# no compress
# def p(g):
#  G=sum(g,[])
#  (_,c),(_,b),(_,a)=sorted((G.count(v),v)for v in{*G})
#  h,w=len(g),len(g[0])
#  for I in range(h*w):
#   if g[i:=I//w][j:=I%w]==c:
#    u=0
#    for k in range(9):
#     if-1<(y:=i+k//3-1)<h and-1<(x:=j+k%3-1)<w and g[y][x]!=a:
#      u+=k%2+1
#      u|=(k%6==1)*16|(k in(3,5))*32
#    g[i][j]=[a,b][u>52]
#  return g


# def p(g):
#  (a,_),(b,_),(c,_)=__import__("collections").Counter(sum(g,[])).most_common()
#  h,w=len(g),len(g[0])
#  for i in range(h):
#   for j in range(w):
#    if g[i][j]==c:
#     u=s=t=0
#     for k in range(9):
#      y=i+k//3-1
#      x=j+k%3-1
#      if-1<y<h and-1<x<w and g[y][x]!=a:
#       u+=k%2+1
#       s|=k%6==1
#       t|=k in (3,5)
#     g[i][j]=[a,b][(u>4)*s*t]
#  return g
