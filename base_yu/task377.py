# best: 55(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, biz, intgrah jimboko awu macaque sammyuri) / others: 57(ox jam), 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 59(import itertools), 59(HIMAGINE THE FUTURE.), 65(cubbus)
# ========================= 55 ========================
f=lambda x:[t for s,t in zip([0]+x,x)if s!=t]
p=lambda g:f([*zip(*f(g))])

# p=lambda g,c=1:c and p([*zip(*p(g,0))],0)or[[*t]for s,t in zip([0]+g,g)if s!=t]
# p=lambda g,c=2:c and [*map(list,p([*zip(*[t for s,t in zip([0]+g,g)if s!=t])],c-1))]or g
# p=lambda g,c=2:(x:=[[*t]for s,t in zip([0]+g,g)if s!=t])*c and p([*zip(*x)],c-1)or x
