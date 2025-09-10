# best: 92(jailctf merger) / others: 94(intgrah jimboko awu macaque sammyuri), 106(4atj sisyphus luke Seek mukundan), 107(jonas ryno kg583), 107(JRK), 109(xsot ovs att joking mewheni)
# =========================================== 92 ===========================================
# lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[x|y for x,y in zip(g[0],g[-1])if x|y]])*len(a[0])
# p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[*filter(int,map(max,zip(g[0],g[-1])))]])*len(a[0])
# p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[v for s in zip(*g)if(v:=max({*s}-{5}))]])*len(a[0])
# lambda g:any(min(g))and(a:=[[x|y for x,y in zip(g[0],g[-1])if x|y]])*len(a[0])or[*zip(*p([*zip(*g)]))]
p=lambda g:any(min(g))*[a:=[*filter(int,max(g[0],g[-1]))]]*len(a)or[*zip(*p([*zip(*g)]))]

# lambda g:5in(a:=max(g,key=set))and[*zip(*p([*zip(*g[::-1])]))][::-1]or[a:=[*filter(int,a)]]*len(b)









