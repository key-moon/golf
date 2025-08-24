# best: 54(att) / others: 55(4atj), 56(luke), 57(sisyphus), 61(joking+MWI), 61(mukundan)
# lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(g[0])-2),8]]*(len(g)-2)+a
# lambda g,c=-1:g*c or p([*zip(*(a:=[[8]*len(g[0])])+g[1:-1]+a)],c+1)
# lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(a)-2),8]]*(len(g)-2)+a
# lambda g,c=-3:g*c or p([r+[8]for*r,_ in zip(*g[::-1])],c+1)
# lambda g,c=-1:g*c or p([[8,*r,8]for _,*r,_ in zip(*g)],c+1)
# lambda g,c=-1:g*c or p([[8,*r[2:],8]for r in zip(*g)],c+1)
# lambda g,c=-1:g*c or p([[8,*r,8]for*r,_,_ in zip(*g)],c+1)
# ======================== 54 ========================
p=lambda g,c=-1:g*c or p([[8,*r[2:],8]for r in zip(*g)],c+1)