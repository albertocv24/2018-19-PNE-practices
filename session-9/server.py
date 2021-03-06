import socket

PORT = 8081
IP = "127.0.0.1"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    #Reading the message from the client+
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))

    #Sending the message back to the client
    #because we are an echo server
    cs.send(str.encode(msg))


#Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is a socket that is use to connect to Internet, the other parameter is the type

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    #-- Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)
