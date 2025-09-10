# best: 55(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 57(intgrah jimboko awu macaque sammyuri), 57(xsot ovs att joking mewheni), 73(jacekwl Potatoman nauti), 75(natte), 92(jonas ryno kg583)
# ========================= 55 ========================
f=lambda x:[t for s,t in zip([0]+x,x)if s!=t]
p=lambda g:f([*zip(*f(g))])

# p=lambda g,c=1:c and p([*zip(*p(g,0))],0)or[[*t]for s,t in zip([0]+g,g)if s!=t]
# p=lambda g,c=2:c and [*map(list,p([*zip(*[t for s,t in zip([0]+g,g)if s!=t])],c-1))]or g
# p=lambda g,c=2:(x:=[[*t]for s,t in zip([0]+g,g)if s!=t])*c and p([*zip(*x)],c-1)or x












