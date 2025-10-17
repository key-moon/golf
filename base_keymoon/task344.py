# best: 78(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 79(jacekwl Potatoman nauti), 79(jacekw Potatoman nauti natte), 79(jacekw Potatoman nauti), 79(cg-klogw-sekken), 79(natte)
# ==================================== 78 ====================================
# p=lambda g,c=4:c and p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
# import re;p=lambda g,c=4:c and p([*zip(*eval(re.sub("3, 2","8,0",str(g)))[::-1])],c-1)or g
p=lambda g,c=-3:c*g or[*zip(*eval(str(p(g,c+1)).replace("3, 2","8,0"))[::-1])]
