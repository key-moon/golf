# best: 86(jailctf merger) / others: 94(luke), 94(4atj sisyphus luke Seek), 94(xsot ovs att), 94(att), 103(joking MeWhenI)
# lambda g:[[t[i]and(4<<sum([*t[i-1:i]+t[i+1:i+2]]+s[j-1:j]+s[j+1:j+2]))%7 for j,t in enumerate(zip(*g))]for i,s in enumerate(g)]
# lambda g,E=enumerate:[[t[i]and sum([*t[i-1:i+2]]+s[j-1:j+2])**4%7 for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[t[i]and sum([0,*t][i:i+3]+[0,*s][j:j+3])**4%7 for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[t[i]*sum([0,*t][i:i+3]+[0,*s][j:j+3])**4*3%7for j,t in E(zip(*g))]for i,s in E(g)]
# ======================================== 86 ========================================
# lambda g,A=[[0]*99]:[[v and sum(B)%7^1for*B,v in zip([0]+S,T[1:]+[0],s)]for S,s,T in zip(A+g,g,g[1:]+A)] <- 失敗

