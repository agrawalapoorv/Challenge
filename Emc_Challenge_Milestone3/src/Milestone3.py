
import socket
import os

HOST, PORT = '', 9003
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    files = str(os.listdir(os.curdir))
    print files
    rootDir = '.'
    list1=[]
    for dirName, subdirList, fileList in os.walk(rootDir):
        list1.append(dirName)
        list1.append(subdirList)
        print('Found directory:',dirName)
        for fname in fileList:
            list1.append(fname)
            print('\t%s' % fname)
    list2=str(list1)
    print list1
    client_connection.send('HTTP/1.0 200 OK\n')
    client_connection.send('Content-Type: text/html\n')
    client_connection.send('\n') # header and body should be separated by additional newline
    client_connection.send("""
        <html>
        <body>
        <h1>Hello World</h1>
        </body>
        </html>
    """) # Use trte string.
    #client_connection.send(files)
    client_connection.send(list2)

    client_connection.close()
