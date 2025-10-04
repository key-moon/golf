# best: 84(4atj sisyphus luke Seek mukundan) / others: 94(ox jam), 101(jacekw Potatoman nauti natte), 103(natte), 103(jailctf merger), 103(biz)
# S=sorted;p=lambda g:(16<sum(b:=max(g,key=sum))or any(map(sum,g[2+(i:=g.index(b)):])))and[*map(list,zip(*p([*zip(*g[::-1])])))][::-1]or S(g[:i],key=max)+g[i:]
# S=sorted;p=lambda g:sum(b:=max(g,key=sum))<17and S(g[:(i:=g.index(b))],key=max)+S(g[i:],key=max,reverse=True)or[*map(list,zip(*p([*zip(*g)])))]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[i:],key=max,reverse=True)
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[i:][::-1],key=max)[::-1]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*zip(*p([*zip(*g)]))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
# lambda g,c=-35:g*c or p([*zip(*[g.pop((1-any(g[i:=g.index(max(g,key=max))-1]))*(0<i)*i)]+g)][::-1],c+1)
# lambda g,c=-35:g*c or p([*zip(*[g.pop(any(g[i:=g.index(max(g,key=max))-1])**(0<i)*-i+i)]+g)][::-1],c+1)
# lambda g,c=-35:g*c or p([*zip(g.pop((any(g[i:=g.index(max(g,key=max))-1])*99<i)*i),*g)][::-1],c+1)
# ======================================= 84 =======================================
p=lambda g,c=-35:g*c or p([*zip(g.pop((max(g[i:=g.index(max(g,key=max))-1])*9<i)*i),*g)][::-1],c+1)
# lambda g,c=-35:g*c or p([*zip(g.pop(                             ),*g)][::-1],c+1)

# max([8,2,1]+g,key=max)
