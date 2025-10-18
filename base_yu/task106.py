# best: 67(jailctf merger, 4atj sisyphus luke Seek mukundan, intgrah jimboko awu macaque sammyuri, import itertools) / others: 75(jacekw Potatoman nauti natte), 75(ox jam), 76(kabutack), 76(JRKKX), 76(JRKXK)
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
