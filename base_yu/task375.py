# best: 53(mukundan, 4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, kabutack, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 57(MasukenSamba), 58(jonas ryno kg583), 58(JRK), 61(Yuchen20), 62(jacekwl Potatoman)
# ======================== 53 =======================
# p=lambda g,E=enumerate:[[v*((i-j)*(i+j-len(g)+1)!=0)for j,v in E(s)]for i,s in E(g)]
# p=lambda g:[[1for s[i],s[~i]in[(0,0)]]for i,s in enumerate(g)]and g

def p(g,i=0):
 for s in g:s[i]=s[~i]=0;i+=1
 return g
# p=lambda g:exec("for i,s in enumerate(g):s[i]=s[~i]=0")or g
