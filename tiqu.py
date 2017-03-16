import re
import string

def tiqu():
	namelist=open("namelist.txt",'rw').readlines()
	for i in namelist:
		i=str(i).replace("\n","")
		full_name=string.lower(i)
		patt=re.compile(r'[A-Z]+')
		res=patt.findall(i)
		nick_name=""
		for j in res:
			nick_name += j
		print i,full_name,nick_name

if __name__=="__main__":
	tiqu()
	
