# best: 70(Code Golf International, jailctf merger) / others: 74(ox jam), 76(4atj sisyphus luke Seek mukundan), 77(HIMAGINE THE FUTURE.), 78(biz), 78(intgrah jimboko awu macaque sammyuri)
# p=lambda g,c=-3:c*g or p([[y or x>0for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# ================================ 70 ================================
p=lambda g,c=-3:c*g or[[(c>0)|(c:=y)for y in s]for s in zip(*p(g,c+1)[::-1])]
