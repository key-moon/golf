def p(g):l=[g[i][i]for i in range(min(len(g),len(g[0])))];u=[l[0]]+[l[i]for i in range(1,len(l))if l[i]!=l[i-1]];return [u]if len(g[0])>len(g)else [[i]for i in u]
