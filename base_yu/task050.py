# best: 86(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek) / others: 88(jailctf merger), 91(xsot ovs att joking mewheni), 96(mukundan), 101(duckyluuk), 101(MasukenSamba)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([[s[i]or(12<sum(s[:i])+6<sum(s))*3for i in range(len(s))]for s in zip(*g)],c+1)
# lambda g,c=-1:c*g or p([[s[i]or(8in s[:i])*(8in s[i:])*3for i in range(len(s))]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([[v or(8in s[:i])*(8in s[i:])*3for i,v in enumerate(s)]for s in zip(*g)],c+1)
