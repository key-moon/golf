# best: 89(jailctf merger, ox jam) / others: 94(4atj sisyphus luke Seek mukundan), 101(jacekw Potatoman nauti natte), 101(JRKX), 101(JRKXK), 101(JRKKX)
# ========================================== 89 =========================================
# lambda g,c=-3:c*g or p([[v or(3in s[:i])*max(s[i:])for i,v in enumerate(s)]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or[[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*p(g,c+1)[::-1])]
