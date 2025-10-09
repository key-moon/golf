# best: 83(4atj sisyphus luke Seek mukundan, Rafael Pooja, jailctf merger) / others: 87(ox jam), 92(jacekw Potatoman nauti natte), 92(intgrah jimboko awu macaque sammyuri), 93(natte), 94(jonas ryno kg583 kabutack)
# ======================================= 83 ======================================
# lambda g,c=-3:c*g or p([(l:=s[0],1)and[[v,l or v][v==8 and ((l:=0) or 1)]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([(l:=0)or[[v,(1-l)*s[0]or v][l:=l or v==8]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([(l:=1)and[[l*s[0]or v,v][l:=l and v!=8]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([(l:=1)and[[l*s[0]or v,v][l:=l*(v!=8)]for v in s]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or[[[l*s[0]or v,v][l:=l*(v!=8)]for v in s]for s in zip(*p(g,c+1)[::-1])if(l:=1)]
p=lambda g,c=-3:c*g or[eval(str(s).replace("8","s[0]or 8",1))for s in zip(*p(g,c+1)[::-1])]

# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("([1-9])((, 0)+, )8",r"\1\2\1",str(p(g,c+1))))[::-1])]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("8(?=[ ,0]{4,}([1-9]))",r"\1",str(p(g,c+1))))[::-1])]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("8(?=, 0[^[(]*([1-9]))",r"\1",str(p(g,c+1))))[::-1])]
