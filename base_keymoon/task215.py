# best: 42(jailctf merger) / others: 44(biz), 44(intgrah jimboko awu macaque sammyuri), 45(ox jam), 46(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 46(Code Golf International)
# p=lambda g,a=2:[max(g[(a:=(a+1)%3)::3])for _ in g] 50
# p=lambda g:[max(g[i%3::3])for i in range(len(g))] 49
# p=lambda g:[max((g:=[[],[]]+g)[2::3])for r in g]
# p=lambda g:[max((g:=[[]]*2+g)[2::3])for r in g]
# p=lambda g:[max((g:=[r,[]]+g)[2::3])for r in g]
# ================== 42 ==================
p=lambda g:[max((g:=g[:2]+g)[2::3])for r in g]
