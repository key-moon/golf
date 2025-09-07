# best: 92(jailctf merger) / others: 96(intgrah jimboko awu macaque sammyuri), 106(4atj sisyphus luke Seek mukundan), 106(4atj sisyphus luke Seek), 107(jonas ryno kg583), 107(JRK)
# =========================================== 92 ===========================================
p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[x|y for x,y in zip(g[0],g[-1])if x|y]])*len(a[0])
# p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[*filter(int,map(max,zip(g[0],g[-1])))]])*len(a[0])
# p=lambda g:any(map(all,g))and[*zip(*p([*zip(*g)]))]or(a:=[[v for s in zip(*g)if(v:=max({*s}-{5}))]])*len(a[0])
