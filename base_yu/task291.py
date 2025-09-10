# best: 61(jailctf merger) / others: 62(duckyluuk), 62(4atj sisyphus luke Seek mukundan), 62(xsot ovs att joking mewheni), 69(Bulmenisaurus), 70(intgrah jimboko awu macaque sammyuri)
# ============================ 61 ===========================
# lambda g:[[c for c in range(1,10)if len({s.count(c) for s in g})>2]]
# port re;p=lambda g:[[int(re.search(r"([^0])[^[]*0, \1",str(g))[1])]]
# port re;p=lambda g:[[int(re.search(r"([^0]), (0, )+\1",str(g))[1])]]
import re;p=lambda g:[[int(re.search(r"([^0]), 0[^[]+\1",str(g))[1])]]








