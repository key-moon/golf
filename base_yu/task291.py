# best: 62(duckyluuk) / others: 69(Bulmenisaurus), 70(att), 71(luke), 71(joking), 71(xsot)
# ============================ 62 ============================
# import re
# p=lambda g:[[int(re.search("([1-9])(, 0)+, \\1",str(g)).group(1))]]

p=lambda g:[[c for c in range(1,10)if len({s.count(c) for s in g})>2]]