# best: 65
# 70
# p=lambda g:[[c or(any(s)+any(r))&2for c,s in zip(r,zip(*g))]for r in g]
# 65
p=lambda g:[[s[0]or(any(s)+any(r))&2for s in zip(r,*g)]for r in g]
