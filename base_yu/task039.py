# best: 60(jailctf merger, 4atj sisyphus luke Seek mukundan, Code Golf International) / others: 61(jacekwl), 61(Potatoman), 61(jacekw Potatoman nauti natte), 61(ox jam), 61(MasukenSamba)
# =========================== 60 ===========================
# p=lambda g,c=-1:c*g or p([s for s in zip(*g) if any(s)],c+1)[:3]
# p=lambda g,c=-1:c*g or[*zip(*p([s for s in zip(*g)if any(s)],c+1))][:3]
p=lambda g,c=-1:c*g or[*zip(*p([*filter(any,zip(*g))],c+1))][:3]
