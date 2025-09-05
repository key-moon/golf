# best: 86(4atj sisyphus luke Seek, luke/sisyphus/Seek, sisyphus) / others: 101(luke), 109(joking+MWI), 109(joking/MWI), 109(joking), 109(joking MeWhenI)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([(u:={0})and[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
p=lambda g,c=-1,u={0}:c*g or p([[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)