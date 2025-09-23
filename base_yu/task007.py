# best: 62(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 63(intgrah jimboko awu macaque sammyuri), 65(ox jam), 67(2F), 67(biz), 72(natte)
# ============================ 62 ============================
# lambda g:(G:=sum(g,[]))and[[max(G[(i+j)%3::3])for j in range(7)]for i in range(7)]
# lambda g,R=range(7):[[max(sum(g,[])[(i+j)%3::3])for j in R]for i in R]
# lambda g:(u:=[max(sum(g,[])[i::3])for i in(0,1,2)]*99)and[u[i*7:i*7+7] for i in range(7)]
p=lambda g:eval('eval("max(sum(g:=[[0]*2]+g,[])[2::3]),"*7),'*7)
