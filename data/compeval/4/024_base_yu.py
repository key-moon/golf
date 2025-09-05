# p=lambda g:[[(1 in s)+3*(3 in s)or(2 in t)*2for t in zip(*g)]for s in g]
p=lambda g:[[max({*s}-{2})or(2 in t)*2for t in zip(*g)]for s in g]