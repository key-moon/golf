# best: 97(intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 105(4atj sisyphus luke Seek mukundan), 105(jailctf merger), 118(natte), 132(jacekwl Potatoman nauti), 189(MasukenSamba)
# ============================================== 97 =============================================
# p=lambda g,c=-1:c*g or p([1<(t:=len(s)-s.count(0))and[sum(s[i%t::t])for i in range(len(s))]or s for s in zip(*g)],c+1)
# p=lambda g,c=-1:c*g or p([[s,[sum(s[i%(t:=~s.count(0)%len(s)+1)::t])for i in range(len(s))]][t>1]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([1<(t:=sum(map(bool,s)))and[sum(s[i%t::t])for i in range(len(s))]or s for s in zip(*g)],c+1)

