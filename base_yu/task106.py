# best: 55(ox jam) / others: 59(jailctf merger), 66(lv1.dev), 66(LogicLynx), 66(FuunAgent), 66(intgrah jimboko awu macaque sammyuri)
# p=lambda g:(t:=[g[i]+[*[*zip(*g[::-1])][i]]for i in range(len(g))])and t+[s[::-1]for s in t[::-1]]
# p=lambda g:(t:=[g[i]+[s[i]for s in g[::-1]]for i in range(len(g))])and t+[s[::-1]for s in t[::-1]]

# p=lambda g:(t:=[g[i]+[*v]for i,v in enumerate(zip(*g[::-1]))])and t+[s[::-1]for s in t[::-1]]
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
# p=lambda g:((t:=[*zip(*(g+[*zip(*g)][::-1]))])+[s[::-1]for s in t[::-1]])[::-1]

# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]

# ========================= 55 ========================
p=lambda g:(u:=[*zip(*zip(*g),*g[::-1])])+[s[::-1]for s in u[::-1]]
