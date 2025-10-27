# best: 83(intgrah jimboko awu macaque sammyuri) / others: 84(Code Golf International), 84(4atj sisyphus luke Seek mukundan), 84(jailctf merger), 84(ox jam), 84(biz)
# ======================================= 83 ======================================
# p=lambda g,c=4:c and p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
