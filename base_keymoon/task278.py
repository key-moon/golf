# best: 118(4atj sisyphus luke Seek) / others: 121(jailctf merger), 126(mukundan), 143(xsot ovs att joking mewheni), 213(MasukenSamba), 224(jacekwl)
# ======================================================= 118 ========================================================
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=((...){0,2}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1|c%3%-2]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{%s,%s})?2.{%s}2)"%(a:=len(g)*3-4,a+6,a+5),"3",str([*zip(*g)][::1|c%3%-2]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{,6}.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1|c%3%-2]))),c+1)
import re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=(.{,6}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1|c%3%-2]))),c+1)
