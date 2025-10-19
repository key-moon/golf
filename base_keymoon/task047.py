# best: 55(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, HETHAT, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 56(JRKKX), 56(dbdr), 56(JRKXK), 56(Yuchen20), 56(JRKX)
# 72
# p=lambda g:[[(t:=sum({*r,*s}))and[t,2][10<t]for s in zip(*g)]for r in g]
# 56
p=lambda g:[[sum({*r,*s})%13for s in zip(*g)]for r in g]
