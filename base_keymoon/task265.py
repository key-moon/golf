# best: 115(4atj sisyphus luke Seek) / others: 119(mukundan), 131(jailctf merger), 148(jacekwl), 149(xsot ovs att joking mewheni), 153(jacekw)
# ====================================================== 115 ======================================================
# port re;p=lambda g,c=-7:g*c or DUMP([*zip(*eval(re.sub("([0%s]), 0(?=.{52}\\1, [02])"%"2@"[c%2&(0**(hash((*g[1],))%1031))],"2,2",str(p(g,c+1)))))][::-1]) <- 失敗
import re;p=lambda g,c=-7:g*(c+4*0**(hash((*g[1],))%1031))or[*zip(*eval(re.sub("([02]), 0(?=.{52}\\1, [02])","2,2",str(p(g,c+1)[::-1]))))]


# +2*0**(hash((*g[1],))%1031)