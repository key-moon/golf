# best: 64(jailctf merger, ox jam) / others: 65(open source), 65(jacekw Potatoman nauti natte), 65(Ali), 65(blob2822), 65(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ============================= 64 =============================
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*[u[i%(8-2*(u[3:6]in(u[:3],u[2::-1])))] for i in range(15)]))]
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*(u[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:[*map(list,zip(*((u:=[*zip(*g)])[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:(u:=[*zip(*g)])and[(s[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
# p=lambda g:[(s[:8-2*((u:=[*zip(*g)])[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
p=lambda g:[(r[:6+2*(r[:4]in(r[4:8],r[8:12]))]*3)[:15]for r in g]