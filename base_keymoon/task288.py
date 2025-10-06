# best: 89(jailctf merger) / others: 90(jacekw Potatoman nauti natte), 90(jacekw Potatoman nauti), 92(ox jam), 93(Yuchen20), 94(cg-klogw-sekken)
# ========================================== 89 =========================================
# 109
def p(g,a=3):
 l=len(g)//2
 for i in range(2-0**g[-2][l-1],l+1):g[-a][l-i]=g[-a][l+i]=g[-1][l];a+=1
 return g
# 111
# def p(g,a=1):
#  l=len(g)//2
#  for s in g[-2-0**g[-2][l-1]::-1][:l]:s[l-a]=s[l+a]=s[l+a]or g[-1][l];a+=1
#  return g

