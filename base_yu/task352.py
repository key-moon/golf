# best: 84(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, biz) / others: 88(import itertools), 89(jacekw Potatoman nauti natte), 90(HIMAGINE THE FUTURE.), 91(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 92(natte)
# ======================================= 84 =======================================
# p=lambda g,c=4:c and p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
