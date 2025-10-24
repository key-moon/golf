def p(i):
 i=[[0if t==max(i[0])else t for t in t]for t in i];i=[t for t in i if max(t)>0];i=[list(t)for t in zip(*i)];i=[t[::-1]for t in i];i=[t for t in i if max(t)>0];i=[t[::-1]for t in i];i=[list(t)for t in zip(*i)];t=[t[:]for t in i];i=[[t[0][0],0,t[0][3]],[0,0,0],[t[3][0],0,t[3][3]]]
 if t[0].count(0)==1:i[0][1]=max(t[0])
 if t[3].count(0)==1:i[2][1]=max(t[3])
 if i[2][0]==i[2][2]:i[2][1]=i[2][0]
 if t[0][0]==t[0][2]and t[0][0]>0:i[0][1]=i[0][0]
 if t[0][0]==t[2][0]and t[0][0]>0:i[1][0]=i[0][0]
 if t[0][3]==t[2][3]and t[0][3]>0:i[1][2]=i[0][2]
 if t[3][0]==t[1][0]and t[3][0]>0:i[1][0]=i[2][0]
 if t[3][3]==t[1][3]and t[3][3]>0:i[1][2]=i[2][2]
 if t[0][1]==t[0][2]and t[0][0]==0and t[0][3]==0:i[0][1]=t[0][1]
 if t[1][0]==t[2][0]and t[0][0]==0and t[3][0]==0:i[1][0]=t[1][0]
 if t[3][1]==t[3][2]and t[3][0]==0and t[3][3]==0:i[2][1]=t[3][1]
 if t[1][3]==t[2][3]and t[0][3]==0and t[3][3]==0:i[1][2]=t[2][3]
 return i