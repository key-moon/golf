# best: 72(jailctf merger) / others: 79(4atj sisyphus luke Seek mukundan), 79(intgrah jimboko awu macaque sammyuri), 79(xsot ovs att joking mewheni), 81(jonas ryno kg583), 82(Yuchen20)
# [1,-1][i in(0,len(r)-1)]
# (1-(i in(0,len(r)-1))*2)
# [1,-1][i%(len(r)-1)<1]
# 1-(i%(len(r)-1)<1)*2
# ================================= 72 =================================
def p(g,i=0,d=1):
 for r in g[::-1]:r[i]=1;i+=d;d*=1-(i%(len(r)-1)<1)*2
 return g












