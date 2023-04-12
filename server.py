import socket # Imports socket module

hostAddress = "localhost" # IP Address of machine that runs server
portNumber = 6969 # Specifies the port used for communication

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP and IPV4 socket
sock.bind((hostAddress, portNumber)) # Binds a socket to a specific host address and port number
sock.listen(5) # Specifies that up to five connections can be handled by the socket via a queue

print(f"Listening on {hostAddress} at port {portNumber}:") # Prints out the host address and port number
clientConnection, address = sock.accept() # Accepts a client socket connection and gets the client socket connection and address 
print(f"Connected to by {address}") # Prints out the client address

try:
    while True: # Runs a loop until break statement is triggered
        inputCommand = input(">> ") # Takes the command as input
        if not inputCommand.strip() or inputCommand.upper() == "QUIT": # Checks if input was quit or nothing
            break # Breaks the loop
        clientConnection.sendall(inputCommand.encode()) # Sends the client connection the encoded command
        commandOutput = clientConnection.recv(4096).decode() # Gets the output from the client
        print(commandOutput) # Prints output of command when executed on client
except Exception as error:
    print(f"Error Message: {error}") # Prints error message
finally:
    x = ""