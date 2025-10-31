# best: 83(Code Golf International) / others: 89(jailctf merger), 89(ox jam), 90(intgrah jimboko awu macaque sammyuri), 94(4atj sisyphus luke Seek mukundan), 94(FuunAgent)
# ======================================= 83 ======================================
# lambda g,c=-3:c*g or p([[v or(3in s[:i])*max(s[i:])for i,v in enumerate(s)]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or[[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*p(g,c+1)[::-1])]
