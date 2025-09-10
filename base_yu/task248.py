# best: 72(jailctf merger) / others: 79(4atj sisyphus luke Seek mukundan), 79(intgrah jimboko awu macaque sammyuri), 79(xsot ovs att joking mewheni), 81(jonas ryno kg583), 82(Yuchen20)
# ================================= 72 =================================
# p=lambda g:(u:=[[0]*i+[1]+[0]*(len(g[0])-i-1)for i in range(len(g[0]))])and((u+u[-2:0:-1])*9)[:len(g)][::-1]
# p=lambda g:(((u:=[[0]*i+[1]+[0]*(len(g[0])-i-1)for i in range(len(g[0]))])+u[-2:0:-1])*9)[:len(g)][::-1]
# p=lambda g:(((u:=[[0]*i+[1]+[0]*(len(g[0])-i-1)for i in range(len(g[0]))])+u[-2:0:-1])*9)[len(g)-1::-1]
# p=lambda g:(((v:=[u:=[1]+[0]*~-len(g[0])]+[u:=[0]+u[:-1]for _ in u[1:]])+v[-2:0:-1])*9)[len(g)-1::-1]
def p(g,i=0,d=1):
 for r in g[::-1]:r[i]=1;i+=d;d*=1|-(i%~-len(r)<1)
 return g











