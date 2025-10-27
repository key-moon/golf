# best: 73(jailctf merger) / others: 75(ox jam), 76(Code Golf International), 76(4atj sisyphus luke Seek mukundan), 77(HIMAGINE THE FUTURE.), 77(biz)
# p=lambda g,c=-3:c*g or p([[y or x>0for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# ================================== 73 =================================
p=lambda g,c=-3:c*g or[[(c>0)|(c:=y)for y in s]for s in zip(*p(g,c+1)[::-1])]
