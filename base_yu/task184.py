# best: 100(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 101(ox jam), 124(intgrah jimboko awu macaque sammyuri), 129(jacekw Potatoman nauti natte), 129(jacekw Potatoman nauti), 130(natte)
# ============================================== 100 ===============================================
# p=lambda g:[t for s in g if (t:=[*filter(int,s)])and(t:=[y for x,y in zip([0]+t,t)if x!=y])]
# p=lambda g,c=-3:g*c or(l:=[0]*len(g[0]))and[l:=[map(max,l,r),r][sum(r)==0] for r in zip(*p(g,c+1))if({*l}!={*r})&any(r)]
# p=lambda g:(l:=[0]*len(g[0]))and[(l:=r)and t for r in g+[l]if (t:=(l:=[*map(max,l,r)])) and not any(r)]
# p=lambda g,c=-1:c*g or p([*zip(*((l:=[0]*len(g[0]))and[(l:=r)and t for r in g+[l]if (t:=(l:=[*map(max,l,r)])) and not any(r)]))],c+1)
# p=lambda g,c=-1:c*g or p(((l:=[0]*len(g))and[(l:=r)and t for r in [*zip(*g)]+[l]if (t:=(l:=[*map(max,l,r)])) and not any(r)]),c+1)
# p=lambda g,c=-1:c*g or p((l:=[0]*len(g))and[(l:=r,t)[1]for r in[*zip(*g)]+[l]if(t:=(l:=[*map(max,l,r)]))and 1-any(r)],c+1)
# p=lambda g,c=-1:c*g or(l:=[0]*len(g))and[(l:=r,t)[1]for r in[*zip(*p(g,c+1))]+[l]if(t:=(l:=[*map(max,l,r)]))and 1-any(r)]
# p=lambda g,c=-1:c*g or(l:=[0]*len(g))and[(l:=r,t)[1]for r in[*zip(*p(g,c+1))]+[l]if(t:=(l:=[*map(max,l,r)]))*(1-any(r))]
p=lambda g,c=-1:c*g or(l:=[0]*len(g))and[(l,l:=r)[0]for r in[*zip(*p(g,c+1)),l]if(l:=[*map(max,l,r)])*(1-any(r))]
