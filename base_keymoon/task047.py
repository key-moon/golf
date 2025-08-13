# best: 55
# 72
# p=lambda g:[[(t:=sum({*r,*s}))and[t,2][10<t]for s in zip(*g)]for r in g]
# 56
p=lambda g:[[sum({*r,*s})%13for s in zip(*g)]for r in g]
