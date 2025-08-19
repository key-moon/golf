# p=lambda g,a=2:[max(g[(a:=(a+1)%3)::3])for _ in g] 50
# p=lambda g:[max(g[i%3::3])for i in range(len(g))] 49
# p=lambda g:[max((g:=[[],[]]+g)[2::3])for r in g]
# p=lambda g:[max((g:=[[]]*2+g)[2::3])for r in g]
# p=lambda g:[max((g:=[r,[]]+g)[2::3])for r in g]
# ======= best: 46 by luke, 4atj, att ========
p=lambda g:[max((g:=g[:2]+g)[2::3])for r in g]