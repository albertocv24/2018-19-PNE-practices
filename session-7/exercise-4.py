#Programming our first client

import socket

while True:

    # Create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8080
    #MY IP
    IP = "212.128.253.91"


    file = input("Type a message: ")
    # Connect to the server
    s.connect((IP, PORT))

    s.send(str.encode(file))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FORM THE SERVER: ")
    print(msg)

    s.close()


    print("The end")
