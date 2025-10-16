# best: 121(import itertools) / others: 122(intgrah jimboko awu macaque sammyuri), 129(jailctf merger), 133(JRKKX), 134(4atj sisyphus luke Seek mukundan), 137(ox jam)
# ========================================================= 121 =========================================================
# p=lambda g,c=-1,z=[[0]*10]:c*g or p([*zip(*[[s[i]or(S==s==T and{*s[:i+1]}>{0}<{*s[i:]})*8for i in range(10)]for S,s,T in zip(z+g,g,g[1:]+z)])],c+1)
# p=lambda g,c=-1,R=range(10):c*g or p([*zip(*[[g[k][i]or(g[k-1]==g[k]==(g+[[0]*10])[k+1]and{*g[k][:i+1]}>{0}<{*g[k][i:]})*8for i in R]for k in R])],c+1)
# p=lambda g,c=-1,R=range(10):c*g or p([*zip(*[[g[k][i]or(g[k-1]==g[k]==g[(k+1)%10]and{*g[k][:i+1]}>{0}<{*g[k][i:]})*8for i in R]for k in R])],c+1)
# p=lambda g,c=-1,E=enumerate:c*g or p([*zip(*[[v or(g[k-1]==s==g[(k+1)%10]and{*s[:i+1]}>{0}<{*s[i:]})*8for i,v in E(s)]for k,s in E(g)])],c+1)
#p=lambda g,c=-1,E=enumerate:c*g or p([*zip(*[[v or(g[k-1]==s==g[(k+1)%10]!={0}<{*s[i:]}<{*s})*8for i,v in E(s)]for k,s in E(g)])],c+1)
p=lambda g,c=-1,E=enumerate:c*g or p([*zip(*[[v or(g[k-1]==s==g[k-9]!={0}<{*s[i:]}<{*s})*8for i,v in E(s)]for k,s in E(g)])],c+1)
