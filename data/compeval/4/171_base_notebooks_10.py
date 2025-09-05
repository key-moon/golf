def p(g):
 d='[tNbygPigDNFbygPPigDQQlyRSSSiRTUUaJcnnnKcTUUUaJcnnnnnKcTVbJgWKgDNNbygPPPigDNNFbygPPPPigDEkkkkkkkJXXXXXXXKTYYMlJRZZZZKRDEkkkkJXXXXKTYMlJRZZKRTEEdJmnlKmTUHaJcnnKcTEEEEdJmnlnlnlKmDNNNbygPPPPPigTYYYMlJRZZZZZZKRTUUUUaJcnnnnnnnKcDNNNFbygPPPPPPigDQQGlyRSSSSiRTVVLbJgWWWWKgTVVbJgWWWKgTYYlJRZZZKRDEkkkkkJXXXXXKDQQQlyRSSSSSiRTVVVLbJgWWWWWWKgDQlyRSiRTUaJcnKcDEkkkkkkJXXXXXXKTEEEdJmnlnlKmTYYYlJRZZZZZKRTYlJRZKRTEEEEEEEdJmnlnlnlnlnlnlKmDNNNNbygPPPPPPPigDEkkJXXKDEkkkJXXXKDQGlyRSSiRTEEEEEdJmnlnlnlnlKmTEEEEEEEEdJmnlnlnlnlnlnlnlKmDQQQGlyRSSSSSSiRTUUUHaJcnnnnnnKcTVLbJgWWKgTUUHaJcnnnnKcDQQQQlyRSSSSSSSiRTVVVbJgWWWWWKgTYYYYlJRZZZZZZZKRTEEEEEEdJmnlnlnlnlnlKmTVVVVbJgWWWWWWWKgDEkJXKB]'
 m='nbZMMYjlXnaWLLVHHUDdTjbSgcRGGQjaPFFNlkMbkLimKymJakHlhGbhFdkECtDB,CA}Bz]A8]zxqywOxv"wuev0]usqtrIs{"rp[qo[p":ojdnggmbalhdkicj8fi0fhccge[f],ebbd8,caab0,a'
 m=[[m[i:i+2],m[i+2]]for i in range(0,len(m),3)]
 for r in m:d=d.replace(r[1],r[0])
 d=eval(d)
 for k in d:
  if k['I']==g:g=k['O'];return g