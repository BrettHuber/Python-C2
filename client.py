import socket # Imports socket module
import subprocess # Imports subprocess module

hostAddress = "localhost" # IP Address of machine that runs server
portNumber = 6969 # Specifies the port used for communication

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP and IPV4 socket
    sock.connect((hostAddress, portNumber)) # Connect to the server socket

except Exception as error:
    print(f"Error Message: {error}") # Prints error message
finally:
    sock.close() # Closes the client socket