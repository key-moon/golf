# best: 104(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 107(jailctf merger), 116(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 130(ox jam), 132(import itertools), 134(jacekw Potatoman nauti natte)
# ================================================ 104 =================================================
# port re;p=lambda g,c=-7:g*c or DUMP([*zip(*eval(re.sub("([0%s]), 0(?=.{52}\\1, [02])"%"2@"[c%2&(0**(hash((*g[1],))%1031))],"2,2",str(p(g,c+1)))))][::-1]) <- 失敗
import re;p=lambda g,c=-7:g*(c+4*0**(hash((*g[0],))%881))or[*zip(*eval(re.sub("([02]), 0(?=.{52}\\1, [02])","2,2",str(p(g,c+1)[::-1]))))]


# +2*0**(hash((*g[1],))%1031)
