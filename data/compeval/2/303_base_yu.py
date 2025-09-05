# ============================================================34567890
# 34567890123456789012345678901234567890123456789012345678901234567890
# p=lambda g:[[[2,v][any(s)*any(t)]for t,v in zip(zip(*g),s)]for s in g]
p=lambda g:[[v+2-2*any(s)*any(t)for t,v in zip(zip(*g),s)]for s in g]
# p=lambda g:[[(v-2)*any(s)*any(t)+2for t,v in zip(zip(*g),s)]for s in g]
