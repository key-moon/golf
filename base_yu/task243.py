# best: 79(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 80(jacekwl Potatoman nauti), 80(jacekw Potatoman nauti natte), 80(jacekw Potatoman nauti), 80(natte), 81(HETHAT)
# ===================================== 79 ====================================
# p=lambda g,c=80:c and p([*map(list,zip(*(g[:1]+[[y or(x==1)for x,y in zip(s,t)]for s,t in zip(g,g[1:])])[::-1]))],c-1)or g
# p=lambda g,c=80:c and p([*map(list,zip(*[s[:1]+[y or(x==1)for x,y in zip(s,s[1:])]for s in g][::-1]))],c-1)or g
# p=lambda g,c=80:c and p([[s[0]]+[y or(x==1)for x,y in zip(s,s[1:])]for s in zip(*g[::-1])],c-1)or g
# p=lambda g,c=80:c and p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
# lambda g,c=-79:c*g or p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)

p=lambda g,c=-79:c*g or[*zip(*eval(str(p(g,c+1)).replace("1, 0","1,1")))][::-1]
