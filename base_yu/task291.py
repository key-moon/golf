# best: 59(ox jam) / others: 61(Code Golf International), 61(jailctf merger), 62(4atj sisyphus luke Seek mukundan), 62(LogicLynx), 62(FuunAgent)
# =========================== 59 ==========================
# lambda g:[[c for c in range(1,10)if len({s.count(c) for s in g})>2]]
# port re;p=lambda g:[[int(re.search(r"([^0])[^[]*0, \1",str(g))[1])]]
# port re;p=lambda g:[[int(re.search(r"([^0]), (0, )+\1",str(g))[1])]]
import re;p=lambda g:[[int(re.search(r"([^0]), 0[^[]+\1",str(g))[1])]]
