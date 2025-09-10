# best: 115(jailctf merger, xsot ovs att joking mewheni) / others: 117(4atj sisyphus luke Seek mukundan), 145(duckyluuk), 165(jacekwl), 165(jacekwl Potatoman nauti), 166(natte)
# ====================================================== 115 ======================================================
# p=lambda g,c=-3:c*g or p([*zip(*[(u:=0)or[[u:=u|(v>0)*(len({*s[i-3:i]})>2)*s[i-2],v][v>0]for i,v in enumerate(s)]for s in g[::-1]])],c+1)
# p=lambda g,c=-3:c*g or p([*zip(*[(u:=0)or[[u:=u|(len({*s[i-3:i]})>2>0<v)*s[i-2],v][v>0]for i,v in enumerate(s)]for s in g[::-1]])],c+1)

# port re;p=lambda g,c=-63:c*g or[*zip(*eval(re.sub(r"(0, ([^0]), ((?!\2|0)., )+(0, )*)0",r"\1\2",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=[, 0]*(, [^0])+(?!\1), ([^0]), 0)",r"\2",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=[^[(]*(, [^0])+(?!\1), ([^0]), 0)",r"\2",str(p(g,c+1)))))][::-1]
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(, 0)*(, [^0])+(?!\2), ([^0]), 0)",r"\3",str(p(g,c+1)))))][::-1]

# def p(g):
#  for _ in range(4):
#   g=[(u:=0)or[[u:=u|(len({*s[i-3:i]})==3 and v and s[i-2]),v][v>0]for i,v in enumerate(s)]for s in g]
#   g=[*zip(*g[::-1])]
#  return g










