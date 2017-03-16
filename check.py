import re

def check_len(strs):
	if(len(strs)<=8):
		return False
	else:
		return True

def check_big(strs):
	BigPattern=re.compile(r'[A-Z]+')
	result=BigPattern.search(strs)
	if result:
		return True
	else:
		return False

def check_small(strs):
	SmallPattern=re.compile(r'[a-z]+')
	result=SmallPattern.search(strs)
        if result:
                return True
        else:
                return False

def check_num(strs):
	NumPattern=re.compile(r'[0-9]+')
	result=NumPattern.search(strs)
        if result:
                return True
        else:
                return False

def check_spc(strs):
	Spchar2=[]
	Spchar="@#$%&*/!"
	for i in Spchar:
		for j in strs:
			if i==j:
				Spchar2.append(i)
			else:
				pass
	if (len(Spchar2)==0):
		return False
	else:
		return True

def check_all(strs):
	#strs=raw_input("enter you password:")
        result=check_len(strs)+check_big(strs)+check_small(strs)+check_num(strs)+check_spc(strs)
        if result==5:
                return True
        else:
                return False

if __name__=="__main__":
	check_all()
