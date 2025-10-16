# best: 38(kambarakun, adakoda) / others: 39(jailctf merger), 39(natte), 39(cubbus), 39(4atj sisyphus luke Seek mukundan), 39(jacekw Potatoman nauti natte)
# ================ 38 ================
# p=lambda g:[u:=[g[0][0],g[1][0]]*3,u[::-1]]
# p=lambda g:[u:=(g[0]+g[1])[::6]*3,u[::-1]]
p=lambda g:[u:=sum(g,[])[::6]*3,u[::-1]]
