# best: 46(Code Golf International, FuunAgent, ox jam) / others: 50(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 50(lv1.dev), 50(LogicLynx), 50(ALE-Agent), 51(cubbus)
# ==================== 46 ====================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
