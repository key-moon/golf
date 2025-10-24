def p(s,o=range(9),u=range(3)):
 r,q=__import__('collections').Counter(s[0]+s[1]+s[2]).most_common(1)[0][0],[[0for o in o]for g in o]
 for(t,r)in[(g,o)for o in u for g in u if s[g][o]==r]:
  for g in o:q[3*t+g%3][3*r+g//3]=s[g%3][g//3]
 return q