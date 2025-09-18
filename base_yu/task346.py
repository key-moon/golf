# best: 58(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 68(ox jam), 68(4atj sisyphus luke Seek mukundan), 68(xsot ovs att joking mewheni), 77(jacekwl Potatoman nauti), 107(Yuchen20)
# ========================== 58 ==========================
# p=lambda g,E=enumerate:[[sum(s[j] for i,s in E(g)for j,t in E(zip(*g))if len({*(u:=[0,*s,0][j:j+3:2]+[0,*t,0][i:i+3:2])})==1and[s[j]]*4!=u>[1])]]
# p=lambda g,E=enumerate:[[s[j]for i,s in E(g)for j,t in E(zip(*g))if(u:=[0,*s][j:j+3])==[0,*t][i:i+3]==u[::-1]>[1]and u[0]!=s[j]!=0]]
# p=lambda g:[[g[i+1][j+1]*(g[i][j:j+3]==g[i+2][j:j+3]==[g[i][j]]*3>[1])for j in range(len(g[i])-2)]for i in range(len(g)-2)]
# p=lambda g:[[g[i+1][j+1]for i in range(len(g)-2)for j in range(len(g[i])-2)if[1]<g[i][j:j+3]==g[i+2][j:j+3]==[g[i][j]]*3 and 0<g[i+1][j+1]!=g[i][j]]]
# p=lambda g:[[g[i+1][j+1]for i in range(len(g)-2)for j in range(len(g[i])-2)if g[i][j:j+3]+g[i+1][j:j+3:2]+g[i+2][j:j+3]==[g[i][j]]*8>[1]]]
# p=lambda g,E=enumerate:[[s[j]for i,s in E(g)for j,t in E(zip(*g))if(u:=s[j-1:j+2])==[*t][i-1:i+2]==u[::-1]>[1]and u[0]!=s[j]!=0]]
p=lambda g,E=enumerate:[[s[j]for i,s in E(g)for j,t in E(zip(*g))if(u:=s[j-1:j+2])==[*t][i-1:i+2]>[1]and u[-1]==u[0]!=s[j]>0]]
