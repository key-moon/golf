# best: 107(jailctf merger) / others: 112(mukundan), 117(joking MeWhenI), 121(4atj sisyphus luke Seek), 121(joking), 121(sisyphus)
# ================================================== 107 ==================================================

p=lambda g,c=-3:c*g or p([*zip(*[(t:=0)or[(t:=[max(t,v),t>0][v==1])%5|v for v in s][::-1]for s in zip(*g)])],c+1)

# def p(g):
#  g=[*zip(*g)]
#  g=[(t:=0)or[(t:=[max(t,v),t>0][v==1])%5 or v for v in s][::-1]for s in g]
#  g=[(t:=0)or[(t:=[max(t,v),t>0][v==1])%5 or v for v in s][::-1]for s in g]
#  g=[*zip(*g)]
#  return g

# def p(g):
#  g=[*zip(*[(t:=0)or[(t:=[max(t,v),t>0][v==1])%5 or v for v in s][::-1]for s in zip(*g)])]
#  g=[*zip(*[(t:=0)or[(t:=[max(t,v),t>0][v==1])%5 or v for v in s][::-1]for s in zip(*g)])]
#  return g

# (0,5):5
# (2,5):5
# (5,2):5
# (0,2):2
# (0,1):0
# (5,1):1

# (0,0):0
# (2,0):2
# (5,0):5
# (1,0):1