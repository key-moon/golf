# best: 112(jailctf merger) / others: 115(Code Golf International), 115(4atj sisyphus luke Seek mukundan), 116(ox jam), 125(intgrah jimboko awu macaque sammyuri), 134(jacekw Potatoman nauti natte)
# ==================================================== 112 =====================================================
# def p(g):
#  w=1-any(g[1])
#  u=g[w:]
#  return(len(g)<6)*(g[:w]+[[v or any(t)*max(sum(g,[]))for*t,v in zip(*u,s)]for s in u])or p(g[:5])+p(g[5:])

# p=lambda g:(len(g)<6)*(g[:(w:=1-any(g[1]))]+[[v or any(t[1:])*max(sum(g,[]))for*t,v in zip(*g,s)]for s in g[w:]])or p(g[:5])+p(g[5:])
# p=lambda g:[(i%5==-any(g[i//5*5+1]))*g[i] or [v or any(t[i//5*5:][1:5])*max(sum(g[i//5*5:][:5],[]))for*t,v in zip(*g,g[i])]for i in range(10)]
# p=lambda g:[(i%5==-any(g[f:=i//5*5+1]))*g[i]or[v or any(t[f:f+5])*max(sum(g[f-1:f+4],[]))for*t,v in zip(*g,g[i])]for i in range(10)]
p=lambda g:[[v or(i%5!=-any(g[f:=i-i%5+1]))*any(t[f:f+5])*max(sum(g[f:f+4],[]))for*t,v in zip(*g,g[i])]for i in range(10)]



# def q(g):
#  w=1-any(g[1])
#  u=g[w:]
#  return g[:w]+[[v or any(t)*max(sum(u,[]))for*t,v in zip(*u,s)] for s in u]
# def p(g):
#  return q(g[:5])+q(g[5:])
