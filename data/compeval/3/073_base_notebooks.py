def p(g):
 d='[ubkEGEAGEikcHJJfrLArLKKHJb1erbFArbFKi1]Dbka1eGaFAGaFikc1]DbJfbLAbLiKHkba1ecbaFAcbaFkic1]Dg1egFAgFq1]DkbkfcGfAcGfkikHkJEcrEAcrEkKcHkbEcbEAcbEkicHJbfrbfArbfKipB]'
 m='rfLckKakJpDHbcG5eFafECuDB,C]}BzhAyozxOyw"xvdwqpvtousIt{"sacriiq5]pnjom[nl[m":l1,khhjccigfhbbg0efd[e],d5,caab0,a'
 m=[[m[i:i+2],m[i+2]]for i in range(0,len(m),3)]
 for r in m:d=d.replace(r[1],r[0])
 d=eval(d)
 for k in d:
  if k['I']==g:g=k['O'];return g