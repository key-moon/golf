# best: 86(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 115(HETHAT), 126(jacekw Potatoman nauti natte), 134(JRKX), 134(JRKKX), 135(JRKXK)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([(u:={0})and[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
p=lambda g,c=-1,u={0}:c*g or p([[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
