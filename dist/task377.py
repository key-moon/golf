f=lambda x:[[*t]for s,t in zip([0]+x,x)if s!=t]
p=lambda g:f([*zip(*f(g))])