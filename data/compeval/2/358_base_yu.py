# best: 105(4atj sisyphus luke Seek, att, xsot ovs att, sisyphus) / others: 110(joking MeWhenI), 113(mukundan), 113(joking), 182(nauti), 189(MasukenSamba)
# ================================================= 105 =================================================
# p=lambda g,c=-1:c*g or p([1<(t:=len(s)-s.count(0))and[sum(s[i%t::t])for i in range(len(s))]or s for s in zip(*g)],c+1)
# p=lambda g,c=-1:c*g or p([[s,[sum(s[i%(t:=~s.count(0)%len(s)+1)::t])for i in range(len(s))]][t>1]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([1<(t:=sum(map(bool,s)))and[sum(s[i%t::t])for i in range(len(s))]or s for s in zip(*g)],c+1)