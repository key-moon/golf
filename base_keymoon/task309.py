# best: 38
# {1: 1, 8: 8, 7: 5}
# 40
# p=lambda g:eval(str(g).replace("7","5"))
# 39
# p=lambda g:[[x&~2for x in r]for r in g]
# p=lambda g:[[x&13for x in r]for r in g]
p=lambda g:[[x&13for x in r]for r in g]
