# 最多色で切り取り
# best: 87(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 88(2F), 88(biz), 90(intgrah jimboko awu macaque sammyuri), 91(duckyluuk), 94(JRKX)
# ========================================= 87 ========================================
# p=lambda g:(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))and[[v for v,t in zip(s,zip(*g))if c in t]for s in g if c in s]
# p=lambda g:[[v for v,t in zip(s,zip(*g))if c in t]for s in g if(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))in s]
# p=lambda g:[[v for*t,v in zip(*g,s)if c in t]for s in g if(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))in s]
p=lambda g,c=-1:c*g or p([[*s]for s in zip(*g)if max({*(u:=sum(g,[]))}-{0},key=u.count)in s],c+1)
# p=lambda g:[[v for*t,v in zip(*g,s)if c in t]for s in g if(c:=max({*(u:=sum(g,[]))}-{0},key=u.count))in s]
