# best: 95(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 96(xsot ovs att joking mewheni), 101(jonas ryno kg583), 111(jacekwl Potatoman nauti), 112(kabutack), 112(JRK)
# p=lambda g:(G:=sum(g,[]),u:=sorted((G.count(c),G.index(c)%10,c)for c in{*G}-{0}))and[[c for k,_,c in u if k==u[-1][0]]]*u[-1][0]
# p=lambda g:(G:=sum(zip(*g),()),u:=[[c]*G.count(c)for c in G if c>0])and[*zip(*[s for s in u if len(s)==max(map(len,u))])]

# f p(g):G=sum(g,[]);u=sorted((G.count(c),G.index(c)%10,c)for c in{*G}-{0});return[[c for k,_,c in u if k==u[-1][0]]]*u[-1][0]
# ============================================= 95 ============================================
# lambda g,c=9:(a:=[*sum(zip(*g),())])and(X:=[*filter(int,eval("(a.count(Y:=a.pop(0))==c)*Y,"*100))])and-~c*[X]or p(g,c-1)
# f p(g,c=9):a=[*sum(zip(*g),())];X=eval("(a.count(Y:=a.pop(0))==c)*Y,"*100);return-~c*any(X)*[*filter(int,X)]or p(g,c-1)
# lambda g,c=9:(a:=[*sum(zip(*g),())])and-~c*[X:=[v for v in a*1if(a.count(a.pop(0))==c)*v]]*any(X)or p(g,c-1)
# lambda g,c=9:(a:=[*sum(zip(*g),())])and(X:=[v for v in a*1if(a.count(a.pop(0))==c-1)*v])and c*[X]or p(g,c-1)
# f p(g,c=9):a=[*sum(zip(*g),())];X=[v for v in a*1if(a.count(a.pop(0))==c)*v];return-~c*any(X)*[X]or p(g,c-1)
# lambda g,c=9:(a:=[*sum(zip(*g),())])and(X:=[v for v in a*1if(a.count(a.pop(0))==c)*v])and-~c*[X]or p(g,c-1)
def p(g,c=9):a=[*sum(zip(*g),())];return(X:=[v for v in a*1if(a.count(a.pop(0))==c)*v])and-~c*[X]or p(g,c-1)










