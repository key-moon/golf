def	p(g):
	d='[BNNNNtxEhkGkGkGkGkxJmmmmmmmmbkb]Ehtmhgjfhtmhgjfhtb]JrrrrrrrrbtbxEvfjGbkrhmjgvfjGbkbxJssssssssckc]EhbtshrjmvgKfvgjmhbtc]JLLLLLLLLltlxElhyjwhmcjrchsKcgvifjiGlklxJiyyyyyyyyki]EvrKmchujfchgKmvrjshcti]JMMMMMMMMlkl]EihwjyhujmchrKsvcgjifhitl]JcuuuuuuuutcxEhsjrvmKuhfKgvmjrhckcxJiwwwwwwwwtixEchmcjwhfcjuhmKrvsjcGikixF]';m='ggNlfMlgLbjKHBJF,HghG]}FDqECODd"CAqBzIA{"zfiya]xgiwbhvgcuaktcfsbgrp0qo[pn[o":nbfmccle1kahjcbi,1hafge0fd[e],dbbcaab,0a';m=[[m[i:i+2],m[i+2]]for	i	in	range(0,len(m),3)]
	for	r	in	m:d=d.replace(r[1],r[0])
	d=eval(d)
	for	k	in	d:
		if	k['I']==g:g=k['O'];return	g