# best: 62(duckyluuk) / others: 69(Bulmenisaurus), 70(att), 71(luke), 71(joking), 71(xsot)
# ============================ 62 ============================
# lambda g:[[c for c in range(1,10)if len({s.count(c) for s in g})>2]]
# port re;p=lambda g:[[int(re.search(r"([^0])[^[]*0, \1",str(g))[1])]]
# port re;p=lambda g:[[int(re.search(r"([^0]), (0, )+\1",str(g))[1])]]
import re;p=lambda g:[[int(re.search(r"([^0]), 0[^[]+\1",str(g))[1])]]
