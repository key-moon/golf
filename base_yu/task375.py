# best: 53(ShadowPrompt Labs, kabutack, Tony Li, JRKKX, THUNDER THUNDER, jailctf merger, natte, JRKXK, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, JRKX, ox jam, intgrah jimboko awu macaque sammyuri, jacekwl Potatoman nauti, adakoda, jacekw Potatoman nauti, import itertools) / others: 57(MasukenSamba), 58(jonas ryno kg583), 58(JRK), 58(jonas ryno kg583 kabutack), 59(Yuchen20)
# ======================== 53 =======================
# p=lambda g,E=enumerate:[[v*((i-j)*(i+j-len(g)+1)!=0)for j,v in E(s)]for i,s in E(g)]
# p=lambda g:[[1for s[i],s[~i]in[(0,0)]]for i,s in enumerate(g)]and g

def p(g,i=0):
 for s in g:s[i]=s[~i]=0;i+=1
 return g
# p=lambda g:exec("for i,s in enumerate(g):s[i]=s[~i]=0")or g
