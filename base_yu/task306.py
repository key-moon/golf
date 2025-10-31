# best: 63(Code Golf International, import itertools, ox jam) / others: 64(jailctf merger), 66(LogicLynx), 74(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 74(HIMAGINE THE FUTURE.), 75(FuunAgent)
# ============================= 63 ============================
# p=lambda g:[[max(max(s[j%10::10])for s in g[i%10::10])for j in range(len(g[i]))]for i in range(len(g))]
# p=lambda g:[[max((s+[0]+t)[j%10::10])for j in range(len(s))]for s,t in zip(g,(g+g[9:10]+g)[10:])]
# lambda g:[[max((s+[0]+t)[j%10::10])for j in range(len(s))]for s,t in zip(g,g[10:]+[[0]]+g)]
# lambda g:g*0!=0and[max(p(g[i]),*map(p,g[i%10::10]))for i in range(len(g))]or g
# lambda g:g*0!=0and[max(g[i],*map(p,g[i%10::10]))for i in range(len(g))]or g
# lambda g:g*0!=0and[max(r,*map(p,g[i%10::10]))for i,r in enumerate(g)]or g
# lambda g:g*0!=0and[max(r,*map(p,g[i%10::10]))for i,r in enumerate(g)]or g
p=lambda g:g*0!=0and[max(*map(p,g[i%10::10]*2))for i in range(len(g))]or g
