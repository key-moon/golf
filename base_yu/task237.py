# best: 67(ox jam, xsot ovs att joking mewheni) / others: 68(4atj sisyphus luke Seek mukundan), 68(jailctf merger), 68(intgrah jimboko awu macaque sammyuri), 73(HETHAT), 77(JRKX)
# =============================== 67 ==============================
# p=lambda g,c=0:[[(c:=max(s)or c)*any(s[:i+1])for i in range(len(s)-1)]+[c]for s in g]
# p=lambda g,c=0:[(u:=[])+[(c:=max(s)or c)*any(u:=u+[v])for v in s[:-1]]+[c]for s in g]
# p=lambda g,c=0:[(d:=0)or[d:=d+v for v in s[:-1]]+[c:=d or c]for s in g]
p=lambda g,c=0:[(d:=0)or[d:=d+v for v in s]+[c:=d or c]for*s,_ in g]



# def p(g,c=0):
#  for s in g:
#   for i in range(1,len(s)):s[i]|=s[i-1]
#   c=s[-1]=s[-1]or c
#  return g
