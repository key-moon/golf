# best: 108(biz) / others: 109(ShadowPrompt Labs), 116(Code Golf International), 116(4atj sisyphus luke Seek mukundan), 116(jailctf merger), 116(ox jam)
# ================================================== 108 ===================================================

# p=lambda g,t=[0,0]:[
#     # 未storeでnot any(c)ならcを返す
#     # 未storeでany(c)なら4のindex２つをstore、cを返す
#     # storeがあり、not any(c)なら、[0]*(i1+1)+[2]*(i2-i1-1)+[0]*(10-i2)を返す
#     # storeがあり、any(c)なら、未storeに戻してcを返す
#     ([(t:=[0,0])if any(t)else (t:=[i for i,v in enumerate(c) if v>3]),c][1]if any(c)else[c,[0]*(t[0]+1)+[2]*(t[1]-t[0]-1)+[0]*(10-t[1])][any(t)])
#     for c in g
# ]

#p=lambda g,t=[0,0]:[any(c)and[(t:=(0,0))if t[1]else(t:=[i for i,v in enumerate(c)if v>3]),c][1]or[c,[0]*(t[0]+1)+[2]*(t[1]-t[0]-1)+[0]*(10-t[1])][any(t)]for c in g]
#p=lambda g,t=[0,0]:[any(c)and[t:=(0,0)if t[1]else[i for i,v in enumerate(c)if v>3],c][1]or[c,[0]*(t[0]+1)+[2]*(t[1]-t[0]-1)+[0]*(10-t[1])][any(t)]for c in g]
#p=lambda g,t=[0,0]:[any(c)and[t:=(0,0)if t[1]else[i for i,v in enumerate(c)if v>3],c][1]or[c,[2*(t[0]<i<t[1])for i in range(10)]][any(t)]for c in g]
#p=lambda g,t=0:[any(c)and[t:=0if t else[i for i,v in enumerate(c)if v],c][1]or([2*(t[0]<i<t[1])for i in range(10)]if t else c)for c in g]
# p=lambda g,t=[]:[sum(c)and[t:=[i for i,v in enumerate(c)if v]*(t==[]),c][1]or([2*(t[0]<i<t[1])for i in range(10)]if t else c)for c in g]
# p=lambda g,t=[],R=range(10):[sum(c)and[t:=[i for i in R if c[i]]*(t==[]),c][1]or([2*(t[0]<i<t[1])for i in R]if t else c)for c in g]
# p=lambda g,t=[],R=range(10):[sum(c)and[t:=[i for i in R if c[i]if[]==t],c][1]or([2*(t[0]<i<t[1])for i in R]if t else c)for c in g]
p=lambda g,t=[],R=range(10):[sum(c)and[t:=[i for i in R if c[i]if[]==t],c][1]or[2*([]<t!=t[0]<i<t[1])for i in R]for c in g]
