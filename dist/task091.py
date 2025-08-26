A=zip
p=lambda g:(a:=sum([(c:=0)or[*A(*[(x,y)for(x,y)in A(s,t)if c+(c:=c^(x==5or y==5))])]for(s,t)in A([[]]+g,g)],[]))and a[:1]+a[1::2]