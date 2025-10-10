# best: 73(jailctf merger) / others: 75(ox jam), 76(4atj sisyphus luke Seek mukundan), 80(intgrah jimboko awu macaque sammyuri), 84(jacekw Potatoman nauti natte), 84(import itertools)
# p=lambda g,c=-3:c*g or p([[y or x>0for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# ================================== 73 =================================
p=lambda g,c=-3:c*g or[[(c>0)|(c:=y)for y in s]for s in zip(*p(g,c+1)[::-1])]
