# best: 36(Code Golf International) / others: 38(jonas ryno kg583 kabutack), 38(cubbus), 38(jacekwl Potatoman nauti), 38(jacekw Potatoman nauti natte), 38(JRK)
# {1: 1, 8: 8, 7: 5}
# 40
# p=lambda g:eval(str(g).replace("7","5"))
# 39
# p=lambda g:[[x&~2for x in r]for r in g]
# p=lambda g:[[x&13for x in r]for r in g]
p=lambda g:[[x&13for x in r]for r in g]
