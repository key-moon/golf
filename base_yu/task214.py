# best: 62(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 63(xsot ovs att joking mewheni), 70(2F), 70(biz), 73(MasukenSamba), 73(cg)
# ============================ 62 ============================
# p=lambda g:[g[i][:4]+[g[2][i],g[1][i],g[0][i]]+g[2-i][3::-1]for i in(0,1,2)]
# p=lambda g:[s[:4]+[z,y,x]+t[3::-1]for s,(x,y,z),t in zip(g,[*zip(*g)][:3],g[::-1])]
# p=lambda g:[s[:4]+[z,y,x]+t[3::-1]for s,t,x,y,z,*_ in zip(g,g[::-1],*g)]
p=lambda g:[s[:4]+u[2::-1]+t[3::-1]for*u,s,t in zip(*g,g,g[::-1])]
# p=lambda g:[s[:4]+[*t]+u[3::-1]for s,t,u in zip(g,zip(*g[::-1]),g[::-1])]
# p=lambda g:[g[i][:4]+[*[*zip(*g[::-1])][i]]+g[~i][3::-1]for i in(0,1,2)]
# p=lambda g:[[*g[i][:4],*[*zip(*g[::-1])][i],*g[~i][3::-1]]for i in(0,1,2)]

# p=lambda g:[*zip(*((u:=[*zip(*g)][:4])+(v:=[*zip(*u[:3])][::-1])+u[3:]+[*zip(*v)][::-1]))]

# f=lambda v:[*zip(*v)]
# p=lambda g:f((u:=f(g)[:4])+(v:=f(u[:3])[::-1])+u[3:]+f(v)[::-1])

# f=lambda v:[*zip(*v[::-1])]
# p=lambda g:f((g:=f(g)[:4])+f((g:=f(f(g)))[1:])+g)





