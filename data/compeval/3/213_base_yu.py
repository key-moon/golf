# best: 106(4atj sisyphus luke Seek, sisyphus) / others: 111(mukundan), 111(joking MeWhenI), 113(ovs), 113(xsot ovs), 113(biz)
# ================================================= 106 ==================================================
p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[x|y for x,y in zip(g[0],g[-1])if x|y]])*len(a[0])
# p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[*filter(int,map(max,zip(g[0],g[-1])))]])*len(a[0])
# p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[v for s in zip(*g)if(v:=max({*s}-{5}))]])*len(a[0])
