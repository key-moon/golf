# best: 38(kambarakun, adakoda) / others: 39(cubbus), 39(jacekwl Potatoman nauti), 39(jacekw Potatoman nauti natte), 39(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 39(Code Golf International)
# ================ 38 ================
# p=lambda g:[u:=[g[0][0],g[1][0]]*3,u[::-1]]
# p=lambda g:[u:=(g[0]+g[1])[::6]*3,u[::-1]]
p=lambda g:[u:=sum(g,[])[::6]*3,u[::-1]]
