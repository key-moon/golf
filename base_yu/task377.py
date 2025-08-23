# best: 55(luke, 4atj, sisyphus) / others: 58(mukundan), 64(joking), 65(ovs), 75(natte), 110(Bulmenisaurus)
# ========================= 55 ========================
f=lambda x:[t for s,t in zip([0]+x,x)if s!=t]
p=lambda g:f([*zip(*f(g))])

# p=lambda g,c=1:c and p([*zip(*p(g,0))],0)or[[*t]for s,t in zip([0]+g,g)if s!=t]
# p=lambda g,c=2:c and [*map(list,p([*zip(*[t for s,t in zip([0]+g,g)if s!=t])],c-1))]or g
# p=lambda g,c=2:(x:=[[*t]for s,t in zip([0]+g,g)if s!=t])*c and p([*zip(*x)],c-1)or x
