# best: 59(jailctf merger) / others: 60(JRKKX), 60(4atj sisyphus luke Seek mukundan), 60(Code Golf International), 60(ox jam), 60(biz)
# =========================== 59 ==========================
# 3456789012345678901234567890123456789012345678901234567890
p=lambda g:[[u^v^s[0]or v for v,u in zip(s,g[0])]for s in g]
# p=lambda g:[[v^(s[0]^u)*(s[0]*u>0)for v,u in zip(s,g[0])]for s in g]
# p=lambda g:[[(v,v^s[0]^u)[s[0]*u>0]for v,u in zip(s,g[0])]for s in g]
