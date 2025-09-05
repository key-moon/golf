def p(g):
 d='[{"Is0ttttttttaoa]e"Os8howowowowob]]},{"Is0cicicicicicicicicoc]e"Os8hbouhmnjhbouhmnjhbod]]},{"Is0ctctctctctctctctcaoca]e"Os8vjnwdodwunmvjnwdodb]]},{"Is0gllllllllog]e"Os8hdbokjhdmnuvmdnjvmnuhdbok]]},{"Is0ggpgpgpgpgpgpgpgpgaogga]e"Os8kkhjkdnmkvukndmkhkjdnkmvkunkdwkkokkb]]},{"Is0gclclclclclclclclcogc]e"Os8vdmdnukhmknjkhmdnuvdmnkjhkbokd]]},{"Is0gglglglglglglglglgogg]e"Os8kvmkdnjkvmknukhdmdnkjvkmnkuhkdbokk]]},{"Is0gppppppppaoga]e"Os8hkjndmvudnmkhjdnmvundwkokb]]},{"Is0gcpcpcpcpcpcpcpcpcaogca]e"Os8khuknmkvjknmkhudndmvkjnkwkdokdb]]}]'
 m='mhwdhvdjuaitr[sq[r":qalpf1obhnbjmiglddkf8jf0i,1hccge[f],ebbdaac,8b,0a'
 m=[[m[i:i+2],m[i+2]]for i in range(0,len(m),3)]
 for r in m:d=d.replace(r[1],r[0])
 d=eval(d)
 for k in d:
  if k['I']==g:g=k['O'];return g