def p(g):
 d='[BgwKWxRgwKXhGhKKKMyNkYxFyNNtQlNNMTxWRTZXQrMTxYRTZXQrMTWxRTXQZrMUkWxFUvPQhvvMUxYRUvvPQhvMUkYxFUvPQhvvMyNYxRyNtQlNNNMUYxRUPQhvvvMgwKkWxFgwKKXhGhKKMyNxYRyNNNtQlNMyNkYxFyNNtQlNNMTxWRTZXQrMgwKWxRgwKXhGhKKKMUWxRUPQhvvvMTkYxFTrXQZMTYxRTXQZrMgwKxWRgwKKKXhGhKMTkWxFTrXQZMUxWRUvvPQhvJ]'
 m=[['rr','Z'],['ul','Y'],['tl','X'],['Vb','W'],['Pb','V'],['qv','U'],['Sr','T'],['bj','S'],['kF','R'],['Gl','Q'],['th','P'],['ey','N'],['LB','M'],['J,','L'],['uw','K'],['H}','J'],[']]','H'],[',4','G'],['Eo','F'],['DO','E'],["C'",'D'],[']c','C'],['Ao','B'],['zI','A'],["{'",'z'],['jb','y'],['kk','x'],['fa','w'],['eq','v'],['eg','u'],['s2','t'],['c[','s'],['ij','r'],['pg','q'],['af','p'],['nd','o'],['m[','n'],["':",'m'],['hh','l'],['ig','k'],['fb','j'],['eb','i'],[',2','h'],['ba','g'],[',8','f'],['cd','e'],['[0','d'],['],','c'],['aa','b'],[',0','a']]
 for r in m:
  d=d.replace(r[1],r[0])
 d=eval(d)
 for k in d:
  if k['I']==g:
   g=k['O']
   return g