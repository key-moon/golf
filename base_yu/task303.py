# best: 62(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 63(lv1.dev), 63(jailctf merger), 63(intgrah jimboko awu macaque sammyuri), 64(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 64(ShadowPrompt Labs)
# ============================ 62 ============================
# ============================================================34567890
# 34567890123456789012345678901234567890123456789012345678901234567890
# p=lambda g:[[[2,v][any(s)*any(t)]for t,v in zip(zip(*g),s)]for s in g]
p=lambda g:[[v+2-2*any(s)*any(t)for t,v in zip(zip(*g),s)]for s in g]
# p=lambda g:[[(v-2)*any(s)*any(t)+2for t,v in zip(zip(*g),s)]for s in g]
