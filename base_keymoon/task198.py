# best: 122(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 126(jacekw Potatoman nauti), 135(intgrah jimboko awu macaque sammyuri), 207(jacekwl Potatoman nauti), 226(Yuchen20), 239(MasukenSamba)
# ========================================================= 122 ==========================================================
# port re;S=re.sub;p=lambda g,c=-63:eval(S(*"03",str(g)))*c or p(eval(S("0(?=([^(]+[^(04]{9}|, 4))","4",str([*zip(*g)][::-1]))),c+1)
# port re;p=lambda g,c=-63:g*c or[*zip(*eval(re.sub(*["0","3(?=([^[(]+[^[(34]{9}|, 4))","3","4"][c%2::2],str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-63:g*c or[*zip(*eval(re.sub(*["0","3(?=([^[(]+[^[(34]{9}|, 4))","3","4"][c%2::2],str(p(g,c+1)))))][::-1]
# port re;S=re.sub;p=lambda g,c=-63:S(*"03",str(g))*c or[*zip(*eval(S("3(?=([^[(]+[^[(34]{9}|, 4))","4",str(p(g,c+1)))))][::-1]
# import re;S=re.sub;p=lambda g,c=-63:g*c or[*zip(*eval(S("3(?=([^[(]+[^[(34]{9}|, 4))","4",S(*"03",str(p(g,c+1))))))][::-1]
# import re;S=re.sub;p=lambda g,c=-63:g*c or[*zip(*eval(S("3(?=[^[(]+[^[(34]{9}|, 4)","4",S(*"03",str(p(g,c+1))))))][::-1]
import re;S=re.sub;p=lambda g,c=-63:g*c or eval(S("3(?=[^(]+[^(34]{9}|, 4)","4",S(*"03",str([*zip(*p(g,c+1)[::-1])]))))
