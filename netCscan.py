import socket
import threading
from optparse import OptionParser
from subprocess import Popen,PIPE
import sys
import re
import time

print('''\033[1;3;34m
            _    _____                     
           | |  / ____|                    
 _ __   ___| |_| |     ___  ___ __ _ _ __  
| '_ \ / _ \ __| |    / __|/ __/ _` | '_ \ 
| | | |  __/ |_| |____\__ \ (_| (_| | | | |
|_| |_|\___|\__|\_____|___/\___\__,_|_| |_|	netCscan_Version 1.1.1
                                           
        \033[0m''')

def scan(ip, port):
	try:
		# 使用socket模块对IP端口进行探测。
		port = 80
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.1)
		s.connect((ip, port))
		print("\033[1;4;32m[+]Connection Succeeded Yes! %s:%s Open 80\033[0m"%(ip,port))
		s.close()
	except Exception:
		print("\033[36m[-]connection failed %s:%s not open 80\033[0m"%(ip,port))

def main():
	# 循环C段1-255
	for i in range(1,255):
		ip = str(host) + str(i)
		# 调用多线程
		for t in range(1):
			t = threading.Thread(target=scan,args=(ip,t,))
			t.start()

if __name__ == '__main__':
	# 帮助文档
	parser = OptionParser()
	parser.add_option("-u", "--url", dest="url",default=False,help="Target URL (e.g. ""http://www.demo.com/"")", metavar="FILE")
	parser.add_option("-c", "--cpart", dest="part",default=False,help="Please enter an IP paragraph (e.g. ""127.0.0"")", metavar="FILE")

	(options, args) = parser.parse_args()

	# 判断url参数和part参数是否一起使用
	if options.url is not False and options.part is not False:
		parser.print_help()
		sys.exit(1)

	# 判断url参数是http or https
	elif options.url is not False:
		print("\033[1;3;33m[+]netSscan Version 1.1.1\033[0m")
		time.sleep(0.5)
		print("\033[1;3;33m[+]Detection protocol in http or https\033[0m")
		time.sleep(0.5)
		r = re.match('http://',options.url)
		if r is not None:
			print("\033[1;3;33m[+]Target address "+ str(options.url) +'\033[0m')
			time.sleep(0.5)
			print("\033[1;3;33m[+]Probe Target IP in \033[0m")
			ip = options.url[7:-1]
			ping = Popen(['/bin/bash','-c','ping -c 1 '+ip],stdin=PIPE,stdout=PIPE)
			data = ping.stdout.read()
			pat = re.compile(r'([0-9]{1,3})')
			r = re.findall(pat,str(data))
			list = []
			for i in r:
				a = i + '.'
				list.append(a)
			host = ''.join(list[:3])
			print("\033[1;3;33m[+]Target address IP "+ str(host) +'0/24\033[0m')
			time.sleep(1)
			print("\033[1;3;33m[+]The program is starting \033[0m")
			time.sleep(2)
			main()
			
		# https
		elif options.url is not False:
			#print("\033[1;3;33m[+]netSscan Version 1.1.1\033[0m")
			time.sleep(0.5)
			r = re.match('https://',options.url)
			if r is not None:
				print("\033[1;3;33m[+]Target address "+ str(options.url) +'\033[0m')
				time.sleep(0.5)
				print("\033[1;3;33m[+]Probe Target IP in \033[0m")
				ip = options.url[8:-1]
				ping = Popen(['/bin/bash','-c','ping -c 1 '+ip],stdin=PIPE,stdout=PIPE)
				data = ping.stdout.read()
				pat = re.compile(r'([0-9]{1,3})')
				r = re.findall(pat,str(data))
				list = []
				for i in r:
					a = i + '.'
					list.append(a)
				host = ''.join(list[:3])
				print("\033[1;3;33m[+]Target address IP "+ str(host) +'0/24\033[0m')
				time.sleep(1)
				print("\033[1;3;33m[+]The program is starting \033[0m")
				time.sleep(2)
				main()
			else:
				parser.print_help()
				sys.exit(1)
		
	# 判断part参数是否有值，有值进行正则匹配,拼接出一个ip传递过去扫描
	elif options.part is not False:
		pat = re.compile(r'([0-9]{1,3})\.')
		r = re.findall(pat,options.part+".")
		listip = []
		if len(r)==4 and len([x for x in r if int(x)>=0 and int(x)<=255])==4:
			for i in r:
				a = i + '.'
				listip.append(a)
			host = ''.join(listip[:-1])
			print("\033[1;3;33m[+]netSscan Version 1.1.1\033[0m")
			time.sleep(0.5)
			print("\033[1;3;33m[+]Target address"+ host +'0/24\033[0m')
			time.sleep(0.5)
			print("\033[1;3;33m[+]Correct Coming soon Run !\033[0m")
			time.sleep(0.5)
			main()
		elif len(r)==3 and len([x for x in r if int(x)>=0 and int(x)<=255])==3:
			for i in r:
				a = i + '.'
				listip.append(a)
			host = ''.join(listip)
			print("\033[1;3;33m[+]netSscan Version 1.1.1\033[0m")
			time.sleep(0.5)
			print("\033[1;3;33m[+]Target address"+ host +'0/24\033[0m')
			time.sleep(0.5)
			print("\033[1;3;33m[+]Correct Coming soon Run !\033[0m")
			time.sleep(0.5)
			main()
		else:
			parser.print_help()
			sys.exit(1)

	# 如果没有输入就返回帮助文档退出
	else:
		parser.print_help()
		sys.exit(1)

