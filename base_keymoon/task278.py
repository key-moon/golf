# best: 104(intgrah jimboko awu macaque sammyuri) / others: 118(jacekw Potatoman nauti natte), 118(Code Golf International), 118(4atj sisyphus luke Seek mukundan), 118(import itertools), 119(jailctf merger)
# ================================================ 104 =================================================
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=((...){0,2}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{%s,%s})?2.{%s}2)"%(a:=len(g)*3-4,a+6,a+5),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{,6}.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=(.{,6}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
import re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=.{,3}(.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
