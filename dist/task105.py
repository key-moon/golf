A=zip
p=lambda g,c=-31:(c-2)*g or c>0and p([*A(*[[v or(s[1:-1].count(1)>1or i%(len(g)-1)<1)*2for v in s]for(i,s)in enumerate(g)])],c+1)or[*A(*p([*A(*g[any(g[-1])-2::-1])],c+1))][::-1]+g[-1:]