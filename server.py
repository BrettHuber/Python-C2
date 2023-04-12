import socket # Imports socket module

hostAddress = "localhost" # IP Address of machine that runs server
portNumber = 6969 # Specifies the port used for communication

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP and IPV4 socket
sock.bind((hostAddress, portNumber)) # Binds a socket to a specific host address and port number
sock.listen(5) # Specifies that up to five connections can be handled by the socket via a queue

print(f"Listening on {hostAddress} at port {portNumber}:") # Prints out the host address and port number
connection, address = sock.accept() # Accepts a client socket connection and gets the client socket connection and address 
print(f"Connected to by {address}") # Prints out the client address

try:
    x = ""
except Exception as error:
    print(f"Error Message: {error}")
finally:
    x = ""