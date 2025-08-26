# 34567890123456789012345678901234567890123456789012345678901234567890
# p=lambda g:[[v for v,t in zip(s,zip(*g))if len({*t})>2]for s in g if len({*s})>2]
p=lambda g:[[v for*t,v in zip(*g,s)if len({*t})>2]for s in g if len({*s})>2]
