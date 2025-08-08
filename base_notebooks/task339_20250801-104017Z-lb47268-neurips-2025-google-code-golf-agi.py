def p(g):
 flat=[x for r in g for x in r if x!=0]
 maj=max(set(flat), key=flat.count)
 return [[maj]*flat.count(maj)]
