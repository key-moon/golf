# best: 77(mukundan, jailctf merger) / others: 80(4atj sisyphus luke Seek), 90(natte), 91(kabutack), 92(xsot ovs att joking mewheni), 109(duckyluuk)
# p=lambda g,c=-3:c*g or p([[y or x>0for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# ==================================== 77 ===================================
p=lambda g,c=-3:c*g or[[(c>0)|(c:=y)for y in s]for s in zip(*p(g,c+1)[::-1])]

