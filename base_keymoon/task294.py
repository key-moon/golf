# best: 70(jailctf merger) / others: 76(kg583), 76(mukundan), 76(Seek64), 76(luke), 76(joking)
# ================================ 70 ================================
# lambda g,S=[0]*99:[S:=[v and[2,5][V*W==0]for V,v,W in zip([0]+S,s,T[1:]+[0])]for s,T in zip(g,g[1:]+[S])]
import re;p=lambda g:eval(re.sub(f"(?<=5.{(C:='.'*-~len(g[0])*3)})5(?=.{C}5)",'2',str(g)))
