# 最多色で切り取り
# best: 87(4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 88(biz), 91(mukundan), 91(duckyluuk), 94(kabutack), 99(jacekwl Potatoman)
# ========================================= 87 ========================================
# p=lambda g:(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))and[[v for v,t in zip(s,zip(*g))if c in t]for s in g if c in s]
# p=lambda g:[[v for v,t in zip(s,zip(*g))if c in t]for s in g if(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))in s]
# p=lambda g:[[v for*t,v in zip(*g,s)if c in t]for s in g if(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))in s]
p=lambda g,c=-1:c*g or p([[*s]for s in zip(*g)if max({*(u:=sum(g,[]))}-{0},key=u.count)in s],c+1)
# p=lambda g:[[v for*t,v in zip(*g,s)if c in t]for s in g if(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))in s]
