# best: 48(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 49(intgrah jimboko awu macaque sammyuri), 49(xsot ovs att joking mewheni), 54(Potatoman), 54(MasukenSamba), 54(jacekwl Potatoman nauti)
# ===================== 48 =====================
# p=lambda g:[r*2for r in zip(*filter(max,zip(*g)))if max(r)]
# p=lambda g,F=filter:[r*2for r in F(max,zip(*F(max,zip(*g))))]
# p=lambda g,c=2:c and p([*filter(max,zip(*g))]*c,c-1)or g
# p=lambda g,F=filter:[*F(max,zip(*[*F(max,zip(*g))]*2))]
p=lambda g,F=lambda c:[*filter(max,zip(*c))]:F(F(g)*2)






