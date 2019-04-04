import socket

port = 8046
IP = "127.0.0.1"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, port))
msg = """AATGTCGTGTCGT\nlen\ncomplement\ncountA\npercC\nreverse"""

s.send(msg.encode())

info = s.recv(2048).decode('utf-8')
print(info)

s.close()