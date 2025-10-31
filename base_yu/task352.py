# best: 82(Code Golf International, jailctf merger, ox jam) / others: 83(intgrah jimboko awu macaque sammyuri), 84(4atj sisyphus luke Seek mukundan), 84(biz), 88(import itertools), 89(jacekw Potatoman nauti natte)
# ====================================== 82 ======================================
# p=lambda g,c=4:c and p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
