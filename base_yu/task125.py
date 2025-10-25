# best: 119(import itertools, intgrah jimboko awu macaque sammyuri) / others: 126(jailctf merger), 130(jacekw Potatoman nauti natte), 130(Code Golf International), 130(4atj sisyphus luke Seek mukundan), 130(THUNDER THUNDER)
# ======================================================== 119 ========================================================
# p=lambda g,c=-15,l=8:c*g or p([*zip(*[[x-(4*(l|y|2==6)+5*(c>-4<y%3<1))*((l:=x)>7)for x,y in zip(*t)]for t in zip(g,g[:1]+g)][::-1])],c+1)
p=lambda g,c=-15,l=8:c*g or p([*zip(*[[l:=x-x//8*(4*(l|y|2==6)+5*(c>-4<y%3<1))for x,y in zip(*t)]for t in zip(g,g[:1]+g)][::-1])],c+1)



# def p(g):
#  for _ in range(20):
# #   g=[(l:=8)and[[x-4*(l|2==y|2==6!=x==8)-5*(_>15 and y%3==0 and x==8),l:=x][0] for x,y in zip(s,t)]for s,t in zip(g,[[8]*15]+g)]
#   l=8
# #   g=[[[x,x-4*(l|2==y|2==6)-5*(_>15>1>y%3)][(l:=x)>7]for x,y in zip(*c)]for c in zip(g,[[8]*15]+g)]
#   g=[[x-(4*(l|y|2==6)+5*(_>15>1>y%3))*((l:=x)>7)for x,y in zip(*c)]for c in zip(g,[[8]*15]+g)]
#   g=[*zip(*g[::-1])]
#  return g
