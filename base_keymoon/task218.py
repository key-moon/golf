# best: 56(jailctf merger, ox jam) / others: 58(2F), 58(biz), 60(Code Golf International), 60(4atj sisyphus luke Seek mukundan), 62(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# lambda g,c=-1:g*c or[g:=r for r in zip(*p(g,c+1))if any(r)and g!=r]
# 類題: 377
# ========================= 56 =========================
p=lambda g,c=-1:g*c or[g:=r for r in zip(*p(g,c+1))if(g!=r)&any(r)]
