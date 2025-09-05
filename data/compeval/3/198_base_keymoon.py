import re
s=re.sub
def p(g):
 a='.'*len(g);d=a+']'+s('[[ ,]','',str(g))+a;v=f"[].{max(g)[0]}]"
 for x in d:d=s(f"0(?=({a})?4)|(?<={v+a}{v+a})0(?=({a}0)?({a}0)?{a+v})|(?<={v+a})0(?=({a}0)?{a+v})|(?<={v})0(?=0?{v})",'4',d)[::-1]
 return[[*map(int,r)]for r in s('0','3',d).split(']')[1:-2]]