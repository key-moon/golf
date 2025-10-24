g=lambda f:[[f[g][a]for g in range(len(f))]for a in range(len(f[0]))]
def o(f,a,o):
 if f[a][o]!=2or f[a][o+1]!=2:return
 for a in range(max(0,a-1),min(len(f),a+2)):
  for g in range(max(0,o-1),min(len(f[0]),o+3)):
   if f[a][g]!=2:f[a][g]=3
def n(f):
 for a in range(len(f)):
  for g in range(len(f[0])-1):o(f,a,g)
def p(f):n(f);f=g(f);n(f);return g(f)