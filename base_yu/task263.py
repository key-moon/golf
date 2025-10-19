# best: 122(jailctf merger, ox jam, biz) / others: 130(4atj sisyphus luke Seek mukundan), 130(Code Golf International), 132(JRKKX), 141(jonas ryno kg583), 141(JRKXK)
# ========================================================= 122 ==========================================================
# lambda g:len(g)>3and(f:=sorted([(sum(t:=g[i:i+3],g[0]).count(0),t)for i in range(0,len(g),3)]))[-(f[0][0]==f[1][0])][1]or[*zip(*p([*zip(*g)]))]
# lambda g:len(g)>3and(f:=sorted([(str(t:=g[i:i+3]).count("0"),t)for i in range(0,len(g),3)]))[-(f[0][0]==f[1][0])][1]or[*zip(*p([*zip(*g)]))]
# lambda g:len(g)>3and(f:=sorted(zip(*[iter(g)]*3),key=(h:=lambda t:str(t).count("0"))))[-(h(f[0])==h(f[1]))][1]or[*zip(*p([*zip(*g)]))]
# lambda g,c=1:g*-c or(f:=sorted((str(t).count("0"),t)for t in zip(*[iter(zip(*p([*zip(*g)],c-1)))]*3))*2)[-(f[0][0]==f[1][0])][1]
# p=lambda g:len(g)>3and(f:=sorted((str(t).count("0"),t)for t in zip(*[iter(g)]*3)))[-(f[0][0]==f[1][0])][1]or[*zip(*p([*zip(*g)]))]
# p=lambda g,c=-1:c*g or[*zip(*(f:=sorted((str(t).count("0"),t)for t in zip(*[iter(p(g,c+1))]*3)))[-(f[0][0]==(f*2)[1][0])][1])]
p=lambda g,c=-1:c*g or(f:=sorted((str(t).count("0"),t)for t in zip(*[zip(*p(g,c+1))]*3))*2)[-(f[0][0]==f[1][0])][1]


# def p(g):
#  if len(g)<4:
#   return[*zip(*p([*zip(*g)]))]
# #  f=sorted([((g[i]+g[i+1]+g[i+2]).count(0),g[i:i+3])for i in range(0,len(g),3)])
#  f=sorted([(sum(t:=g[i:i+3],g[0]).count(0),t)for i in range(0,len(g),3)])
#  return f[-(f[0][0]==f[1][0])][1]
