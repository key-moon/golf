# best: 62(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, FuunAgent, natte, import itertools, jailctf merger, ox jam, 2F, biz, intgrah jimboko awu macaque sammyuri) / others: 63(jonas ryno kg583 kabutack), 63(jacekwl Potatoman nauti), 63(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 63(JRKX), 63(ALE-Agent)
# ============================ 62 ============================
# def p(g):
#     for i in range(len(g)-1):
#         g[i][-1-i] = 2
#     g[-1][1:] = [4] * (len(g)-1)
#     return g


def p(g):
 for i in range(1,len(g)):g[~i][i]=2;g[-1][i]=4
 return g
# p=lambda g:exec("for i in range(len(g)-1):g[i][~i]=2;g[-1][~i]=4")or g

# p=lambda g:(R:=range(len(g)))and[g[i][:1]+[(i==j)*2+(i==0)*4for j in R][1:]for i in R][::-1]
# p=lambda g:(n:=len(t:=g[0])-1,l:=[0]*~-n+[2])and[*eval("t[:1]+(l:=[l.pop()]+l),"*n)][::-1]+[t[:1]+[4]*n]
