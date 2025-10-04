# best: 67(jailctf merger) / others: 70(4atj sisyphus luke Seek mukundan), 76(jacekwl Potatoman nauti), 76(jacekw Potatoman nauti natte), 76(jacekw Potatoman nauti), 76(natte)
# =============================== 67 ==============================
# 34567890123456789012345678901234567890123456789012345678901234567890
# p=lambda g:[[v for v,t in zip(s,zip(*g))if len({*t})>2]for s in g if len({*s})>2]
# lambda g:[[v for*t,v in zip(*g,s)if len({*t})>2]for s in g if len({*s})>2]
# lambda g:[[t[0]for t in zip(s,*g)if len({*t})>2]for s in g if len({*s})>2]
p=lambda g:[R for s in g if(R:=[t[0]for t in zip(s,*g)if len({*t}&{*s})>2])]
