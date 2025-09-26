# best: 118(4atj sisyphus luke Seek mukundan, intgrah jimboko awu macaque sammyuri) / others: 119(jailctf merger), 119(ox jam), 213(MasukenSamba), 215(jacekwl Potatoman nauti), 215(jacekw Potatoman nauti)
# ======================================================= 118 ========================================================
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=((...){0,2}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{%s,%s})?2.{%s}2)"%(a:=len(g)*3-4,a+6,a+5),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{,6}.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=(.{,6}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
import re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=.{,3}(.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
