def p(g):
 n,s={*sum(g,[])}-{0}
 if 5<str(g).count(f" {n},"*2):n,s=s,n
 e=lambda g:range(l:=min((*a,s).index(s)for a in g),h:=max(bytes(a).rfind(s)for a in g),(h-l+1)//3);return[[[0,n][g[i][j]==s]for j in e(g)]for i in e([*zip(*g)])]