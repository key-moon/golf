# best: 55(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, HETHAT, natte, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 56(JRKX), 56(dbdr), 56(JRKXK), 56(MasukenSamba), 56(Yuchen20)
# 72
# p=lambda g:[[(t:=sum({*r,*s}))and[t,2][10<t]for s in zip(*g)]for r in g]
# 56
p=lambda g:[[sum({*r,*s})%13for s in zip(*g)]for r in g]
