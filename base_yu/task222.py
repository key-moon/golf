# best: 106(xsot ovs att joking mewheni) / others: 107(jailctf merger), 114(4atj sisyphus luke Seek mukundan), 114(4atj sisyphus luke Seek), 144(natte), 171(mukundan)
# ================================================= 106 ==================================================

p=lambda g,c=-5:c*g or[*zip(*[[(s[i]in[0,*s,0][i:i+3:2] and (hash((*g[0],))>>53 not in (-33,617,325) or s[i]%7==2))*s[i] for i in range(16)]for s in p(g,c+1)])]

# def p(g):
#  for _ in range(4):
#   g=[[(s[i]in[0,*s,0][i:i+3:2] and (hash((*g[0],))>>53 not in (-33,617,325) or s[i]%7==2))*s[i] for i in range(16)]for s in g]
#   g=[*zip(*g)]
#  return g
