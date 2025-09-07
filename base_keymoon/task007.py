# best: 62(4atj sisyphus luke Seek mukundan) / others: 63(jailctf merger), 64(intgrah jimboko awu macaque sammyuri), 65(4atj sisyphus luke Seek), 65(mukundan), 66(xsot ovs att joking mewheni)
# ============================ 62 ============================
# lambda g:eval('eval("max(sum(g:=g+[[0]],[])[-2::-3]),"*7),'*7)
p=lambda g:eval('eval("max(sum(g:=[[0]*2]+g,[])[2::3]),"*7),'*7)

