# best: 64(4atj sisyphus luke Seek mukundan, jailctf merger, rucin93, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 65(dbdr), 66(HETHAT), 67(2F), 67(biz), 67(jonas ryno kg583)
# ============================= 64 =============================
# 1の2x2の数を数えて配置しなおす x,yは[0,0,1,2,2],[0,2,1,0,2]
# def p(g):
#  *r,=eval("[0]*3,"*3)
#  for i in range(sum(sum(g,[]))//8):r[int(.7*i)][i*2%3]=1
#  return r

# def p(g):
#  t=sum([[i*8<sum(sum(g,[])),0]for i in range(5)],[])
#  return[t[:3],t[3:6],t[6:9]]

# def p(g):
#  t=[]
#  for i in range(5):t+=[i*8<sum(sum(g,[])),0]
#  return[t[:3],t[3:6],t[6:9]]

# def p(g):
#  x=sum(sum(g,t:=[]))
#  exec("x-=7;t+=[x>0,0];"*5)
#  return[t[:3],t[3:6],t[6:9]]

# p=lambda g:[[(x:=sum(sum(g,t:=[]))/8)>0,0,x>1],[0,x>2,0],[x>3,0,x>4]]
p=lambda g:[[(x:=sum(sum(g,[]))/8)>0,0,x>1],[0,x>2,0],[x>3,0,x>4]]



