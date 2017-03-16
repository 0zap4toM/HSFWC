# HSFWC
Https form weak check!
#VPN/Domain Account WeakPasswd Check

#Description:
This script is used to check weak_password for https post check!

#Idea:
(1)Create Weak_password Dictortry which is
密码字典满足一下四点要求，因为域账号默认需满足一定密码强度。
*至少包含一位大写字母
*至少包含一位小写字母
*至少包含一位数字
*至少包含一位特殊字符
*密码长度大于八位
Cpass.py可以生成满足以上需求的密码字典，用户还可自行定义生成时所需的各种字符

(2)Use python moudle pycurl to send https request and you can check respnosecode to confirm which one is the answer you what.

#Using:
first:生成一个账户列表，规格为：名字每个字的首字母大写，其他字母小写。
second:讲namelist.txt放到当前目录，然后使用python brute.py。

定时查看，如果有弱口令被检测出，则会保存在report/report.txt中。

