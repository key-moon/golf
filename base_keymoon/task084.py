# best: 62(jailctf merger, natte, 2F, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 63(kabutack), 63(JRKKX), 63(JRKXK), 63(JRKX), 63(MasukenSamba)
# 79
# p=lambda g,i=0:[[1for r[-i],g[-1][i]in[[2,4]]]for r in g[:-1]if(i:=i+1)]and g
# 64
# def p(g,i=1):
#  *a,b=g
#  for r in a:r[-i]=2;b[-i]=4;i+=1
#  return g
# 64
# def p(g,i=1):
#  for r in g[:-1]:r[-i]=2;g[-1][i]=4;i+=1
#  return g
# lambda g,i=1:exec("g[i-1][-i]=2;g[-1][i]=4;i+=1;"*(len(g)-1),locals())or g 76
# lambda g:exec("i=1\nfor r in g[:-1]:r[-i]=2;g[-1][i]=4;i+=1",{"g":g})or g  75
# ============================ 62 ============================
def p(g,i=1):
 for r in g[:-1]:r[-i]=2;g[-1][i]=4;i+=1
 return g
