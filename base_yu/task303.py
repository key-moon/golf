# best: 62(4atj sisyphus luke Seek mukundan) / others: 63(jailctf merger), 63(intgrah jimboko awu macaque sammyuri), 64(2F), 64(biz), 64(xsot ovs att joking mewheni)
# ============================ 62 ============================
# ============================================================34567890
# 34567890123456789012345678901234567890123456789012345678901234567890
# p=lambda g:[[[2,v][any(s)*any(t)]for t,v in zip(zip(*g),s)]for s in g]
p=lambda g:[[v+2-2*any(s)*any(t)for t,v in zip(zip(*g),s)]for s in g]
# p=lambda g:[[(v-2)*any(s)*any(t)+2for t,v in zip(zip(*g),s)]for s in g]
