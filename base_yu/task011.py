# best: 121(jailctf merger) / others: 124(4atj sisyphus luke Seek mukundan), 125(xsot ovs att joking mewheni), 133(jonas ryno kg583), 142(MasukenSamba), 155(duckyluuk)
# ========================================================= 121 =========================================================
# p=lambda g:min([[[g[[i//4+t%3*4,3][i%4>2]][[j//4+t//3*4,3][j%4>2]]for j in range(11)]for i in range(11)]for t in range(9)],key=lambda v:max(sum(v,[])))
# p=lambda g:min([(max(sum(v:=[[g[[i//4+t%3*4,3][i%4>2]][[j//4+t//3*4,3][j%4>2]]for j in range(11)]for i in range(11)],[])),v)for t in range(9)])[1]
# p=lambda g:[v for t in range(9)if 1-(8in sum(v:=[[g[[i//4+t%3*4,3][i%4>2]][[j//4+t//3*4,3][j%4>2]]for j in range(11)]for i in range(11)],[]))][0]
p=lambda g:min([(8in sum(v:=[[g[[i//4+t%3*4,3][i%4>2]][[j//4+t//3*4,3][j%4>2]]for j in range(11)]for i in range(11)],g),v)for t in range(9)])[1]



