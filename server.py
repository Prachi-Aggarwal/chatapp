import socket
 
def Main():
    # in case of muliple devices connected over same network change loacalhost to ip of the network
    host = "localhost"
    port = 80
     
    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Server started on",port)
    print("Waiting for connections...")
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print ("from connected  user: " + str(data))
             
            # data = str(data).upper()
            data = input("Enter message: ")
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()
