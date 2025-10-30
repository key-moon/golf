# best: 118(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, import itertools, jailctf merger) / others: 119(ox jam), 129(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 133(HIMAGINE THE FUTURE.), 135(biz), 147(THUNDER THUNDER)
# ======================================================= 118 ========================================================
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=((...){0,2}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{%s,%s})?2.{%s}2)"%(a:=len(g)*3-4,a+6,a+5),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=, (.{,6}.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
# port re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=(.{,6}.{%s}|, )2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
import re;p=lambda g,c=-11:g*c or p(eval(re.sub(r"0(?=.{,3}(.{%s})?2.{%s}2)"%(a:=len(g)*3-2,a+3),"3",str([*zip(*g)][::1-c%3|1]))),c+1)
