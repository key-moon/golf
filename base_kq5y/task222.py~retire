# best: 106(xsot ovs att joking mewheni) / others: 107(jailctf merger), 114(4atj sisyphus luke Seek), 144(natte), 171(mukundan), 233(jacekw)
# ================================================= 106 ==================================================

#p=lambda g,e=enumerate:(v:=max(map(max,g)),r,c:=zip(*[(i,j)for i,R in e(g)for j,C in e(R)if C]),[[v if min(r)<=i<=max(r)and min(c)<=j<=max(c)else 0 for j,_ in e(g[0])]for i,_ in e(g)])[-1]
#p=lambda g,r=range:(v:=next(r[j]for r,R in zip(g,g[1:])for j in r(len(g[0])-1)if(t:=r[j])and t==R[j]==r[j+1]==R[j+1]),[[c*(c==v)for c in A]for A in g])[-1]

#これの後に３辺が0の長方形を消す処理を入れたい
#p=lambda g:(v:=next(a for r,R in zip(g,g[1:])for a,b,c,d in zip(r,R,r[1:],R[1:])if a==b==c==d and a),[[c*(c==v)for c in r]for r in g])[-1]
#p=lambda g,E=enumerate:(h:=(v:=next(a for r,R in zip(g,g[1:])for a,b,c,d in zip(r,R,r[1:],R[1:])if a==b==c==d and a),[[c*(c==v)for c in r]for r in g])[-1],[[c*((i>0 and h[i-1][j]>0)+(i<len(h)-1 and h[i+1][j]>0)+(j>0 and h[i][j-1]>0)+(j<len(h[0])-1 and h[i][j+1]>0)>1)for j,c in E(r)]for i,r in E(h)])[-1]

#2x2を消したい
#p=lambda g,k=15:k and p([[c*((i>0 and g[i-1][j]==c)+(i<len(g)-1 and g[i+1][j]==c)+(j>0 and g[i][j-1]==c)+(j<len(g[0])-1 and g[i][j+1]==c)>1)for j,c in enumerate(r)]for i,r in enumerate(g)],k-1)or g

#len(code)=373 len(compressed)=250
#p=lambda g,E=enumerate,L=len:(h:=[[c*((i>0 and g[i-1][j]==c)+(i+1<L(g)and g[i+1][j]==c)+(j>0 and g[i][j-1]==c)+(j+1<L(g[0])and g[i][j+1]==c)>1)for j,c in E(r)]for i,r in E(g)],(v:=next((c for i,r in E(h)for j,c in E(r)if c and((i>0 and h[i-1][j]==c)+(i+1<L(h)and h[i+1][j]==c)+(j>0 and h[i][j-1]==c)+(j+1<L(h[0])and h[i][j+1]==c)>2)),0),[[c*(c==v)for c in r]for r in h])[-1])[-1]

#len(code)=382 len(compressed)=240 best+134だから絶対違う
p=lambda g,k=1,E=enumerate,L=len:k and p([[c*((i>0 and g[i-1][j]==c)+(i+1<L(g)and g[i+1][j]==c)+(j>0 and g[i][j-1]==c)+(j+1<L(g[0])and g[i][j+1]==c)>1)for j,c in E(r)]for i,r in E(g)],k-1)or(v:=next((c for i,r in E(g)for j,c in E(r)if c and((i>0 and g[i-1][j]==c)+(i+1<L(g)and g[i+1][j]==c)+(j>0 and g[i][j-1]==c)+(j+1<L(g[0])and g[i][j+1]==c)>2)),0),[[c*(c==v)for c in r]for r in g])[-1]
