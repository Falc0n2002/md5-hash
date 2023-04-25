import hashlib
import colorama
from hashlib import *
colorama.init(autoreset=True)
style = '''\033[31m
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     | \033[31m@Falcon Tame 2023
    :  ;    :        :   _/  \033[31m- Hashing Tools
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''--
██╗  ██╗ █████╗ ███████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║███████║███████╗███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██╔══██║╚════██║██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║  ██║███████║██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                               

'''
print (style)
print("=================================================")
print("\033[33m1] - Hash Checker \n2] - Hash lingth  \n3] - Hash type")
print("\033[33m4] - MD5 Encrypt  \n5] - Md5 Decrypt \033[38m")
print("=================================================")

choose = input("Please choose option : ")
if choose == '1' :
	print("This option For Hash Checker")
	hash1 = input(" Enter hash [1] :")
	hash2 = input(" Enter hash [2] :")
	if hash1 == hash2 :
		print("the hash is clean")
	else:
		print("the hash is virus")
if choose == '2' :
	print("This option For lingth Hash ")
	length = input("Enter Your Hash :")
	print("Length Hash is : ", len(length))
if choose == '3' :
	print("This option For know Hash Type")
	hash = input("Enter The Hash :")
	length = len(hash)
	if length == 32 :
		print("The hash is [md5]")
	if length == 40 :
		print("The hash is [sha1]")
	if length == 64 :
		print("The hash is [sha256]")
if choose == '4' :
	print("This option For text to MD5")
	word = input("Enter Your Text :")
	md5 = hashlib.md5(word.encode())
	print(md5.hexdigest())

if choose == '5' :
	print("This option For Decrypt")
	hash = input ("Enter Your Hash :")
	file = input ("Write file name :")
	with open(file , mode='r') as f :
		for line in f :
			line = line.strip()
			if md5(line.encode()).hexdigest() == hash :
				print("[-] Password Found :" +line )
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
