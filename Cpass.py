#*-*coding:utf-8*-*
import check

spe_nums=["2013","2014","2015","2016","2017","1234","123",]
spe_chars="@#$%&*/!"
spe_strs=["abc","ABC","nihao","password","abcd","Abc","qwe","pwd","Abcd","QWE"]
others=["welcom@1","Password@1234","woaini@1234","abc@12345678",'p@ssw0rd']


def fullname_C(full_name,passlist):		#fullname+special_char+special_number,example:lihua@2013
	for i in spe_nums:
		for j in spe_chars:
			passwd=full_name+j+i
			check_pwd(passwd,passlist)

def other_C(passlist):			#some weak password
	for other in others:
		passwd=other
		check_pwd(passwd,passlist)

def spe_char_C(passlist):		#special_str+special_chars+special_number,example:passwd@2014
	for k in spe_nums:
		for i in spe_strs:
			for j in spe_chars:
				passwd=i+j+k
				check_pwd(passwd,passlist)

def nickname_C(nick_name,passlist):		#nickname+special_char+special_str,example:lh@2013
	for i in spe_strs:
		for j in spe_chars:
			passwd=nick_name+j+i
			check_pwd(passwd,passlist)
				
def check_pwd(strs,passlist):
	ck_result=check.check_all(strs)
	if ck_result:
		passlist.write(strs+"\n")
	else:
#		print "Weak password!"
		pass

if __name__=="__main__":
	spe_nums=["2013","2014","2015","2016","2017","1234","123",]
	spe_chars="@#$%&*/!"
	spe_strs=["abc","ABC","nihao","password","abcd","Abc","qwe","pwd","Abcd","QWE"]
	others=["welcom@1","Password@1234","woaini@1234","abc@12345678",'p@ssw0rd']

	passwd_file=raw_input("Enter file to save your password:")
	full_name=raw_input("Enter fullname:")
	nick_name=raw_input("Enter nickname:")
	passlist=open(passwd_file,'w+')
	try:
		fullname_C()
		other_C()
		spe_char_C()
		nickname_C()
		passlist.close()
	except:
		print "Something ERROR!"
		exit(1)
