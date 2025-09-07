# best: 63(jailctf merger) / others: 64(4atj sisyphus luke Seek mukundan), 64(intgrah jimboko awu macaque sammyuri), 65(4atj sisyphus luke Seek), 65(mukundan), 67(biz)
# ============================= 63 ============================
# lambda g:eval('eval("max(sum(g:=g+[[0]],[])[-2::-3]),"*7),'*7)
p=lambda g:eval('eval("max(sum(g:=[[0]*2]+g,[])[2::3]),"*7),'*7)

