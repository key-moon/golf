# best: 106(HIMAGINE THE FUTURE.) / others: 108(intgrah jimboko awu macaque sammyuri), 111(jailctf merger), 112(ox jam), 116(jacekw Potatoman nauti natte), 116(import itertools)
# ================================================= 106 ==================================================
# lambda g,c=23:-c*g or p([*zip(*eval(str(g).replace((c//2*", 5")[2:],(c//2*f",{len({*sum(g,g[0])})*3%5}")[1:])))],c-1)
# lambda g,c=23:-c*g or p([*zip(*eval(str(g).replace("5"+c//2*", 5",(a:="len({*sum(g,g[0])})*3%5")+c//2*f",{a}")))],c-1)
# lambda g,c=23:-c*g or p(eval(str([*zip(*g)]).replace((c//2*", 5")[2:],(c//2*",len({*sum(g,())})*3%5")[1:])),c-1)
# lambda g,c=23:-c*g or p(eval(str([*zip(*g)]).replace((c//2*", 5")[2:],(c//2*",len({*str(g)})**2%7")[1:])),c-1)
p=lambda g,c=47:-c*g or p(eval(str([*zip(*g)][::-1]).replace(c//4*", 5",c//4*",len({*str(g)})**2%7")),c-1)

# mapping = {8: 1, 9: 4, 10: 2}

# def p(g):
#  for c in range(4,24)[::-1]:
# #   g=eval(str(g).replace((c//2*", 5")[2:],(c//2*f",{4**len({*str(g)})%7}")[1:]))
# #   g=[*map(list,zip(*g))]
#   g=eval(str(g).replace((c//2*", 5")[2:],(c//2*f",{len({*sum(g,g[0])})*3%5}")[1:]))
#   g=[*zip(*g)]
#  return g
