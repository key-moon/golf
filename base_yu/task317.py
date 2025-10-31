# best: 43(Code Golf International, ox jam) / others: 53(jailctf merger), 59(jacekw Potatoman nauti natte), 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 59(4atj sisyphus luke Seek mukundan), 59(lv1.dev)
# =================== 43 ==================
# p=lambda g:sum([[sum([[v/5]*3for v in s[1::3]],[])]*3for s in g[1::3]],[])
p=lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
