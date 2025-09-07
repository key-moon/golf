# best: 83(jailctf merger) / others: 86(4atj sisyphus luke Seek mukundan), 86(4atj sisyphus luke Seek), 87(xsot ovs att joking mewheni), 88(mukundan), 93(natte)
# ======================================= 83 ======================================
# lambda g,c=-3:c*g or p([(l:=s[0],1)and[[v,l or v][v==8 and ((l:=0) or 1)]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([(l:=0)or[[v,(1-l)*s[0]or v][l:=l or v==8]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([(l:=1)and[[l*s[0]or v,v][l:=l and v!=8]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([(l:=1)and[[l*s[0]or v,v][l:=l*(v!=8)]for v in s]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or[[[l*s[0]or v,v][l:=l*(v!=8)]for v in s]for s in zip(*p(g,c+1)[::-1])if(l:=1)]

# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("([1-9])((, 0)+, )8",r"\1\2\1",str(p(g,c+1))))[::-1])]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("8(?=[ ,0]{4,}([1-9]))",r"\1",str(p(g,c+1))))[::-1])]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("8(?=, 0[^[(]*([1-9]))",r"\1",str(p(g,c+1))))[::-1])]
