#coded by N17RO (noob hackers)

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (red+"""

██╗██████╗ ██╗  ██╗
██║██╔══██╗██║ ██╔╝
██║██████╔╝█████╔╝ 
██║██╔═══╝ ██╔═██╗ 
██║██║     ██║  ██╗
╚═╝╚═╝     ╚═╝  ╚═╝
                                                      v 1.0
"""+red)
print (lgreen+bold+"         <===[[ coded by Khiem tran]]===> \n"+clear)
print (yellow+bold+"   <---(( Khò khò khò ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Nạn nhân]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[Nhà mạng]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Cơ quan]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[Thành phố]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Vùng đất]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Kinh độ]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Vĩ độ]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Múi giờ]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Mã Bưu Chính]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Chấm dứt, tạm biệt'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" kiểm tra kết nối Internet của bạn!"+clear)
sys.exit(1)
