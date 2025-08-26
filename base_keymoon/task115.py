# best: 67(luke) / others: 68(Seek64), 73(sisyphus), 85(joking+MWI), 87(kg583), 87(mukundan)
# {*g[0]}-{g[0][0]}
# {*g[0]}-{*g[5]}
# len({*g[0]})-1
# len({*g[0]})-1
# lambda g:len({*g[0]})-1and[[g:=r for r in g[0]if r!=g]]or[*zip(*p([*zip(*g)]))]
# lambda g,s={0}:[R for r in g if(R:=[(s:=s|{c})and c for c in r if{c}-s])]
# lambda g:[R for r in g if(R:=[(g:=[c,*g])[0]for c in r if-~g.count(c))]
# lambda g:[R for r in g if(R:=[(g:=[c,*g])[0]for c in r if c not in g])]
# lambda g:[R for r in g if(R:=[(g:=[c,*g])[0]for c in r if(c in g)<1])]
# =============================== 67 ==============================
p=lambda g:[R for r in g if(R:=[(g:=[c]+g)[0]for c in r if(c in g)-1])]

#  a in g
# {c}<{*g}
