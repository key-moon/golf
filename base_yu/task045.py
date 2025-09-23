# best: 45(ox jam, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti, jailctf merger, intgrah jimboko awu macaque sammyuri, Yuchen20, HETHAT, jacekwl Potatoman nauti) / others: 46(natte), 46(jacekwl), 47(cubbus), 47(JRKX), 47(jonas ryno kg583 kabutack)
# ==================== 45 ===================
# def p(g):return[r[:1]*10 if r[0]==r[-1]>0 else r for r in g]
# p=lambda g:[(s,s[:1]*10)[s[0]==s[9]]for s in g]
# p=lambda g:[(s,s[::9]*5)[s[0]==s[9]]for s in g]
# p=lambda g:[(s*10)[::10+(s[0]!=s[9])]for s in g]
# p=lambda g:[s[0]==s[9]and s[:1]*10or s for s in g]

# 34567890123456789012345678901234567890123456789
# p=lambda g:[(s,s[:1]*10)[s[0]==s[9]]for s in g]
# p=lambda g:[(s,s[:1]*10)[s==s[::-1]]for s in g]
# p=lambda g:[[s,*[s*(s==t)]*8,t]for s,*S,t in g]
# p=lambda g:[(S+[s],[s]*10)[s in S]for*S,s in g]
p=lambda g:[(S,[s]*9)[s in S]+[s]for*S,s in g]
