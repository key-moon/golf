# best: 65(mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 67(biz), 67(xsot ovs att joking mewheni), 72(cg), 72(HETHAT), 72(kabutack)
# ============================== 65 =============================
# lambda g:eval('eval("max(sum(g:=g+[[0]],[])[-2::-3]),"*7),'*7)
p=lambda g:eval('eval("max(sum(g:=[[0]*2]+g,[])[2::3]),"*7),'*7)

