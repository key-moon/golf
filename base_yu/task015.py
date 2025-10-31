# best: 87(jailctf merger) / others: 92(Code Golf International), 92(ox jam), 93(4atj sisyphus luke Seek mukundan), 97(intgrah jimboko awu macaque sammyuri), 104(jacekw Potatoman nauti natte)
# ========================================= 87 ========================================
p=lambda g,c=-3:c*g or p([[(y or(0<x%8<3)and(40//x%11))%(9+(c<0))for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([[(s[i]or(0<s[i-1]%8<3)and(40//s[i-1]%11))%(9+(c<0))for i in range(9)]for s in zip(*g[::-1])],c+1)
