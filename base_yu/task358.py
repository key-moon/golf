# best: 96(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 97(ox jam), 102(Code Golf International), 102(4atj sisyphus luke Seek mukundan), 111(jacekw Potatoman nauti natte), 111(JRKX)
# ============================================= 96 =============================================
# p=lambda g,c=-1:c*g or p([1<(t:=len(s)-s.count(0))and[sum(s[i%t::t])for i in range(len(s))]or s for s in zip(*g)],c+1)
# p=lambda g,c=-1:c*g or p([[s,[sum(s[i%(t:=~s.count(0)%len(s)+1)::t])for i in range(len(s))]][t>1]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or[1<(t:=sum(map(bool,s)))and[sum(s[i%t::t])for i in range(len(s))]or s for s in zip(*p(g,c+1))]
