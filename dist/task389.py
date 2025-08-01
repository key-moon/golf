def p(g):
 d=next(x for r in g for x in r if x-5);return[[d*(x==5)for x in r]for r in g]