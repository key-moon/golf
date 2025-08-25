# best: 62(luke, 4atj, luke/sisyphus/Seek, biz) / others: 63(mukundan), 63(kabutack), 63(sisyphus), 64(joking+MWI), 64(joking/MWI)
# ============================ 62 ============================
p=lambda g:(R:=range(len(g)))and[g[i][:1]+[(i==j)*2+(i==0)*4for j in R][1:]for i in R][::-1]
# p=lambda g:(n:=len(t:=g[0])-1,l:=[0]*~-n+[2])and[*eval("t[:1]+(l:=[l.pop()]+l),"*n)][::-1]+[t[:1]+[4]*n]
