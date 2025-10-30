# best: 119(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 122(jailctf merger), 123(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 124(jacekwl Potatoman nauti), 124(jacekw Potatoman nauti natte), 124(jacekw Potatoman nauti)
# ======================================================== 119 ========================================================

# p=lambda g:[x for p in range(32)if min(map(len,(x:=[[sum(t)for j in range(16)if len(t:={s[j],(s+g[0])[p-j]}&{0,[*filter(int,sum(g,[]))][0]})<2]for s in g])))>15][0]
# p=lambda g:[x for p in range(32)if min(map(len,(x:=[[sum(t)for j in range(16)if len(t:={s[j],(s+g[0])[p-j]}&{0,max(sum(g,[]),key=bool)})<2]for s in g])))>15][0]
# p=lambda g:[x for p in range(32)if min(map(len,x:=[[sum(t)for j in range(16)if len(t:={s[j],(s+g[0])[p-j]}&{*max(g,key=any)})<2]for s in g]))>15][0]
# p=lambda g,c=0:min(map(len,x:=[[sum(t)for j in range(16)if len(t:={s[j],(s+g[0])[c-j]}&{*max(g,key=any)})<2]for s in g]))//16*x or p(g,c+1)
# p=lambda g,c=0:(x:=[sum([[*{s[j],(s+g[0])[c-j]}&{*max(g,key=any)}]for j in range(16)],[])for s in g])*([*map(len,x)]==[16]*16) or p(g,c+1)
# p=lambda g,c=0:([*map(len,x:=[sum([[*{s[j],(s+g[0])[c-j]}&{*max(g,key=any)}]for j in range(16)],[])for s in g])]==[16]*16)*x or p(g,c+1)
p=lambda g,c=0:({*map(len,x:=[sum([[*{s[j],(s+g[0])[c-j]}&{*max(g,key=any)}]for j in range(16)],[])for s in g])}=={16})*x or p(g,c+1)


# def p(g):
#  c=[*filter(int,sum(g,[]))][0]
#  for p in range(32):
#   x=[[sum(t)for j in range(16)if(t:={s[j],(s+g[0])[p-j]}&{0,c})<{0,c}]for s in g]
#   if min(map(len,x))>15:
#    return x


# def p(g):
#  c=[*filter(int,sum(g,[]))][0]
#  for p in range(32):
#   x=[[{s[j],(s+g[0])[p-j]}&{0,c}for j in range(16)]for s in g]
#   if{0,c}>max(max(x)):
#    return[[*map(sum,s)]for s in x]


# R=range
# def p(g):
#  c=[v for v in sum(g,[])if v][0]
#  for p in R(32):
#   if all((0<=p-j<16)and g[i][p-j]for I in R(256)if g[i:=I%16][j:=I>>4]==c):
#    return [[~(g[i][j]not in(0,c)and~g[i][p-j]or~g[i][j])for j in R(16)]for i in R(16)]
