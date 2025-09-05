# best: 62(luke/sisyphus/Seek, Seek64, luke, 4atj) / others: 63(mukundan), 66(joking+MWI), 66(joking/MWI), 66(joking), 66(xsot)
# ============================ 62 ============================
# lambda g:[(u:=[0]+[2]*sum(sum(g,[]))+[0]*7)[1:4],u[::4],[0]*3]
# lambda g:[(u:=[2]*sum(sum(g,[]))+(b:=[0]*3))[:3],[0,u[3],0],b]
# lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0]+u[3:5],[0]*3]
p=lambda g:[(u:=[2]*sum(sum(g,a:=[0]))+a*9)[:3],a+u[3:5],a*3]
