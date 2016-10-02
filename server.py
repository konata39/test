if __name__ == '__main__':  
	import socket  
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	sock.bind(('', 8880))  
	sock.listen(5)  
	wait = True
	while wait:  
		connection,address = sock.accept()  
		try:  
			connection.settimeout(5)  
			buf = connection.recv(1024)  
			if buf == '1':  
				connection.send('welcome to server!')
				buf = connection.recv(1024) 
				connection.send('welcome to server!')  
				print buf
			else:  
				connection.send('please go out!')  
		except socket.timeout:  
			print 'time out'  
		connection.close()
		wait = False