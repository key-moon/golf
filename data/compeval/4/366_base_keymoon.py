from re import*
s=sub
def p(g):
 h=len(g:=g[::-1]);w=len(g[0]);a,b=([l[:w//2]for l in g],[l[w//2:]for l in g])if h<w else(g[:h//2],g[h//2:])
 if h<w:w=w//2
 if len(set(str(a)))>len(set(str(b))):a,b=b,a
 A=s('[[ ,]','',str(a))+'0'*w;B=s('[[ ,]','',str(b));c=max(B,key=B.count);d=max(B:=s(']',c,B),key=s(c,'',B).count)
 for l in sorted(sum(([*findall(f"(?={c}.{{{w-2}}}"+f"{c}([^{c}]{{{j}}}){c}.{{{w-1-j}}}"*i+f".{c})",2*c*w+B+2*c*w)]for i in range(2,h)for j in range(2,w)),[]),key=lambda x:str(x).count(d)*.99-sum(map(len,x))):
  l=[*l];t='.'*(w-len(l[0])+1);p=''
  while l:u=l.pop();A=s(s(d,f"[^]{c+d}]",f"(?<={t.join([*l,''])}){u}(?=")+p+')',u,A,1);p=t+u+p
  A=s(d,c,A)
 return[[*map(int,r)]for r in s(c,d,A).split(']')[-3::-1]]