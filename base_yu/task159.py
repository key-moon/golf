# best: 106(intgrah jimboko awu macaque sammyuri) / others: 107(jailctf merger), 107(HIMAGINE THE FUTURE.), 109(Code Golf International), 109(4atj sisyphus luke Seek mukundan), 110(ox jam)
# ================================================= 106 ==================================================

# def p(g,k=0,u=[[2]*99]):
#  g=g*(k>0)or p(g,k:=sum(g,[]).count(2)//12)
#  return[*zip(*u+sum([k*[s]for s in g if{*s}-{0,2}],[])+u)]

# def p(g,k=0,u=[[2]*99]):
#  if k<1:g=p(g,k:=str(g).count("2")//12)
#  return[*zip(*sum([k*[s]for s in g if{*s}-{0,2}],u)+u)]

p=lambda g,c=-1,u=[[2]*99]:g*c or[*zip(*sum([str(g).count("2")//12*[s]for s in p(g,c+1)if{*s}-{0,2}],u)+u)]

# def p(g):
#  k=sum(g,[]).count(2)//12
#  u=[[2]*99]
#  t=[*zip(*u+sum([k*[s]for s in g if{*s}-{0,2}],[])+u)]
#  t=[*zip(*u+sum([k*[s]for s in t if{*s}-{0,2}],[])+u)]
#  return t

# def p(g):
#  k=sum(g,[]).count(2)//12
#  t=[*zip(*[s for s in g if {*s}-{0,2}])]
#  t=[*zip(*[s for s in t if {*s}-{0,2}])]
#  return [[2]*(k*3+2)]+sum([[[2]+sum([[v]*k for v in s],[])+[2]]*k for s in t],[])+[[2]*(k*3+2)]
