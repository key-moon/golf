# best: 62(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 64(intgrah jimboko awu macaque sammyuri), 65(4atj sisyphus luke Seek), 65(xsot ovs att joking mewheni), 65(mukundan), 67(biz)
# ============================ 62 ============================
# lambda g:eval('eval("max(sum(g:=g+[[0]],[])[-2::-3]),"*7),'*7)
p=lambda g:eval('eval("max(sum(g:=[[0]*2]+g,[])[2::3]),"*7),'*7)

