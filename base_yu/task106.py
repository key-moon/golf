# best: 72(luke/sisyphus/Seek, sisyphus) / others: 73(luke), 73(mukundan), 73(4atj), 75(joking+MWI), 75(joking/MWI)
# ================================= 72 =================================
# p=lambda g:(t:=[g[i]+[*[*zip(*g[::-1])][i]]for i in range(len(g))])and t+[s[::-1]for s in t[::-1]]
# p=lambda g:(t:=[g[i]+[s[i]for s in g[::-1]]for i in range(len(g))])and t+[s[::-1]for s in t[::-1]]

# p=lambda g:(t:=[g[i]+[*v]for i,v in enumerate(zip(*g[::-1]))])and t+[s[::-1]for s in t[::-1]]
p=lambda g:(t:=[*zip(*(g+[*zip(*g)][::-1]))])and[s[::-1]for s in t]+t[::-1]
# p=lambda g:((t:=[*zip(*(g+[*zip(*g)][::-1]))])+[s[::-1]for s in t[::-1]])[::-1]
