# best: 67(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 74(intgrah jimboko awu macaque sammyuri), 75(ox jam), 76(JRKX), 76(kabutack), 78(natte)
# p=lambda g:(t:=[g[i]+[*[*zip(*g[::-1])][i]]for i in range(len(g))])and t+[s[::-1]for s in t[::-1]]
# p=lambda g:(t:=[g[i]+[s[i]for s in g[::-1]]for i in range(len(g))])and t+[s[::-1]for s in t[::-1]]

# p=lambda g:(t:=[g[i]+[*v]for i,v in enumerate(zip(*g[::-1]))])and t+[s[::-1]for s in t[::-1]]
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
# p=lambda g:((t:=[*zip(*(g+[*zip(*g)][::-1]))])+[s[::-1]for s in t[::-1]])[::-1]

# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]

# =============================== 67 ==============================
p=lambda g:(u:=[*zip(*zip(*g),*g[::-1])])+[s[::-1]for s in u[::-1]]
