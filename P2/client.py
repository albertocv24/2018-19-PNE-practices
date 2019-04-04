# Programming our fist client
import socket
from Seqp2 import Seq

print("Socket created")

PORT = 8081
IP = "127.0.0.1"

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    seq0 = input("Type a valid sequence:")
    seq1 = Seq(seq0).complement().strbases
    seq2 = Seq(seq0).reverse().strbases

    sequence = [seq0, seq1, seq2]
    s.send(str.encode(str(sequence)))

    msg = s.recv(2048).decode("utf-8")
    print("HEY I AM THE CLIENT")
    print(msg)
    s.close()
