# best: 83(jailctf merger) / others: 84(Code Golf International), 84(ox jam), 85(4atj sisyphus luke Seek mukundan), 90(LogicLynx), 90(FuunAgent)
# ======================================= 83 ======================================
# lambda g,c=-1:c*g or p([[s[i]or(12<sum(s[:i])+6<sum(s))*3for i in range(len(s))]for s in zip(*g)],c+1)
# lambda g,c=-1:c*g or p([[s[i]or(8in s[:i])*(8in s[i:])*3for i in range(len(s))]for s in zip(*g)],c+1)
# lambda g,c=-1:c*g or p([[v or(8in s[:i])*(8in s[i:])*3for i,v in enumerate(s)]for s in zip(*g)],c+1)
# lambda g,c=-1,a=0:c*g or[*zip(*[[v+(v<1)*(a:=a^(23<sum(s)+v))*3for v in s]for s in p(g,c+1)])]
# lambda g,c=-1,a=0:c*g or[*zip(*[[v+(v<(a:=a^(23<sum(s)+v)))*3for v in s]for s in p(g,c+1)])]
# p=lambda g,c=-1,a=0:c*g or[*zip(*[[v+(v<(a:=a^sum(s,v)//24))*3for v in s]for s in p(g,c+1)])]
p=lambda g,c=-1,a=0:c*g or[[v+(v<(a:=a^sum(s,v*2)//32))*3for v in s]for s in zip(*p(g,c+1))]
