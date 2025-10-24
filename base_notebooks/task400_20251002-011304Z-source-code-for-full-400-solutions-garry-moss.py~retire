def p(m,o=len,p=range):
 f,f,l,d=o(m),o(m[0]),[],[];e=1
 for o in p(f//2+1):
  for a in p(f):
   if m[o][a]==e:m[o][a]=m[-(o+1)][a];l+=[o];d+=[a]
   if m[-(o+1)][a]==e:m[-(o+1)][a]=m[o][a];l+=[f-(o+1)];d+=[a]
 for o in p(f):
  for a in p(f//2+1):
   if m[o][a]==e:m[o][a]=m[o][-(a+1)];l+=[o];d+=[a]
   if m[o][-(a+1)]==e:m[o][-(a+1)]=m[o][a];l+=[o];d+=[f-(a+1)]
 m=m[min(l):max(l)+1];m=[o[min(d):max(d)+1]for o in m];return m