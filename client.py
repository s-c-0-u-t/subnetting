import socket
 
# In this Line we define our local host
# address with port number
SERVER = "127.0.0.1"
PORT = 8081
# Making a socket instance
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER, PORT))
# Running a infinite loop
choice=-1
while choice!=13:
    print("Example : 192.234.56.43")
    # here we get the input from the user
    inp = input("Enter IP address: ")
    sub = input("enter subnet mask: ")
    print("Type '13' to terminate")
    choice=input("Enter choice for Compute!\n 1.Convert IP address to binary\n 2.Convert subnet mask to binary \n 3.Wildcard \n 4.Wildcard in binary\n 5.NetworkID in binary\n 6.NetworkID in Decimal\n 7.BroadcastIP in Binary\n 8.BroadcastIP in Decimal\n 9.Maximum IP address in network(in Binary)\n 10.Maximum IP address in network(in Decimal)\n 11.Minimum IP address in network(in Binary)\n 12.Minimum IP address in network(in Decimal)\n 13.Over")
    
    # If user wants to terminate
    # the server connection he can type Over
    # Here we send the user input
    # to server socket by send Method
    client.sendall(str.encode("\n".join([str(inp),str(sub),str(choice)])))
 
    # Here we received output from the server socket
    answer = client.recv(1024)
    print("Answer is "+answer.decode())
#     if choice == "13":
#         break
    #print("Type 'Over' to terminate")
 
client.close()
