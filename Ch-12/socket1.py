import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


# This code establishes a connection to a web server, sends an HTTP GET request to retrieve a text file from the server, and then receives the contents of the file and prints it to the console.

# Here is a step-by-step explanation of what the code does:

# Import the socket module to work with sockets.

# Create a socket object mysock using socket.socket(). This creates a new socket object that uses the Internet address family (AF_INET) and the Stream Control Transmission Protocol (SOCK_STREAM) to communicate.

# Use the connect() method of the mysock object to connect to the web server at the address 'data.pr4e.org' on port 80. Port 80 is the default port for the HTTP protocol.

# Create a cmd variable containing the HTTP GET request to retrieve the text file at 'http://data.pr4e.org/romeo.txt'. The request is encoded as bytes using the .encode() method so that it can be sent over the network.

# Use the send() method of the mysock object to send the GET request to the server.

# Enter a while loop that receives data from the server in chunks of up to 512 bytes using the recv() method of the mysock object. The loop continues until the server sends an empty byte string, which indicates that there is no more data to receive.

# Inside the while loop, decode the received data using the .decode() method to convert the byte string to a string, and then print the decoded data to the console using the print() function.

# After the while loop completes, close the socket connection using the close() method of the mysock object.

# When the code is run, it establishes a socket connection to the web server, sends an HTTP GET request to retrieve the text file at 'http://data.pr4e.org/romeo.txt', receives the file contents in chunks of up to 512 bytes, and prints the contents to the console.