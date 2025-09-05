# best: 50(mukundan, luke, joking, 4atj, kabutack, ovs, natte) / others: 55(Seek64), 55(att), 55(sisyphus), 58(kg583), 58(duckyluuk)
# lambda g:[(r:=[0,*g[0],0])[1:-1],[*map(max,zip(r[2:],r))]]*3
# lambda g:[r:=g[0],[*map(max,zip((a:=[0,*r,0])[2:],a))]]*3
# lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
# ====================== 50 ======================
p=lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
