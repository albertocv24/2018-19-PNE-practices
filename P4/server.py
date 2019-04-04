import socket
import termcolor


IP = "127.0.0.1"
PORT = 8080
MAX_OPEN_REQUESTS = 5


def process_client(cs):

    msg = cs.recv(2048).decode("utf-8")

    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    if msg.startswith("GET /blue"):
        with open("blue.html", "r") as file:
            content = file.read()
    elif msg.startswith("GET /pink"):
        with open("pink.html", "r") as file:
            content = file.read()
    elif msg.startswith("GET /index") or msg.startswith("GET /"):
        with open("index.html", "r") as file:
            content = file.read()
    else:
        with open("error.html", "r") as file:
            content = file.read()

    status_line = "HTTP/1.1 200 ok\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(content)))

    response_msg = status_line + header + "\r\n" + content
    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serversocket.bind((IP, PORT))


serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
