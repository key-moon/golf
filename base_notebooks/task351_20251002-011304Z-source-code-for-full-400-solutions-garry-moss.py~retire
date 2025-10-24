def p(e,a=len,p=range):
 l,u,r,n=a(e),a(e[0]),[],[]
 for f in p(l//2+1):
  for a in p(u):
   if e[f][a]==3:e[f][a]=e[-(f+1)][a];r+=[f];n+=[a]
   if e[-(f+1)][a]==3:e[-(f+1)][a]=e[f][a];r+=[l-(f+1)];n+=[a]
 for f in p(l):
  for a in p(u//2+1):
   if e[f][a]==3:e[f][a]=e[f][-(a+1)];r+=[f];n+=[a]
   if e[f][-(a+1)]==3:e[f][-(a+1)]=e[f][a];r+=[f];n+=[u-(a+1)]
 e=e[min(r):max(r)+1];e=[f[min(n):max(n)+1]for f in e];return e