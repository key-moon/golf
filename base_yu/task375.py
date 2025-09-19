# best: 53(natte, ox jam, 4atj sisyphus luke Seek mukundan, kabutack, jailctf merger, intgrah jimboko awu macaque sammyuri, jacekwl Potatoman nauti, xsot ovs att joking mewheni) / others: 57(MasukenSamba), 58(jonas ryno kg583), 58(JRK), 59(Yuchen20), 61(sekken)
# ======================== 53 =======================
# p=lambda g,E=enumerate:[[v*((i-j)*(i+j-len(g)+1)!=0)for j,v in E(s)]for i,s in E(g)]
# p=lambda g:[[1for s[i],s[~i]in[(0,0)]]for i,s in enumerate(g)]and g

def p(g,i=0):
 for s in g:s[i]=s[~i]=0;i+=1
 return g
# p=lambda g:exec("for i,s in enumerate(g):s[i]=s[~i]=0")or g
