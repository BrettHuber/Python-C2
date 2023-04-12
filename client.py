import socket # Imports socket module
import subprocess # Imports subprocess module

hostAddress = "localhost" # IP Address of machine that runs server
portNumber = 6969 # Specifies the port used for communication


try:
    x = ""
except Exception as error:
    print(f"Error Message: {error}")
finally:
    x = ""