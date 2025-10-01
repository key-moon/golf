# best: 60(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 66(HETHAT), 66(ox jam), 66(biz), 67(jonas ryno kg583 kabutack), 67(JRK)
# =========================== 60 ===========================
# lambda g:[[((c:=sum(sum(g,[])))>0)*2,(c>1)*2,(c>2)*2],[0,(c>3)*2,0],[0,0,0]]
# lambda g:[([2]*(c:=sum(sum(g,[])))+[0]*2)[:3],[0,(c>3)*2,0],[0,0,0]]
# lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0,*u[3:5]],[0,0,0]]
# lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0,*u[3:5]],u[-3:]]
# lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0]+u[3:5],u[-3:]]
# lambda g:[(u:=[0]+[2]*sum(sum(g,[]))+[0]*7)[1:4],u[::4],[0]*3]
# lambda g:[(u:=[2]*sum(sum(g,[]))+(b:=[0]*3))[:3],[0,u[3],0],b]
# lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0]+u[3:5],[0]*3]
p=lambda g:[(u:=[2]*sum(sum(g,a:=[0]))+a*9)[:3],a+u[3:5],a*3]
