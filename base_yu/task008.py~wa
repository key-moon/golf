# best: 94(ovs, xsot ovs) / others: 95(4atj sisyphus luke Seek), 96(mukundan), 97(att), 98(4atj), 106(joking MeWhenI)
# 143
# S=sorted;p=lambda g:(16<sum(b:=max(g,key=sum))or any(map(sum,g[2+(i:=g.index(b)):])))and[*map(list,zip(*p([*zip(*g[::-1])])))][::-1]or S(g[:i],key=max)+g[i:]
# S=sorted;p=lambda g:sum(b:=max(g,key=sum))<17and S(g[:(i:=g.index(b))],key=max)+S(g[i:],key=max,reverse=True)or[*map(list,zip(*p([*zip(*g)])))]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[i:],key=max,reverse=True)
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[i:][::-1],key=max)[::-1]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
# S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*map(list,zip(*p([*zip(*g)])))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
# ============================================ 94 ============================================
# sorted;p=lambda g:2in(b:=max(g,key=sum))and[*zip(*p([*zip(*g)]))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
