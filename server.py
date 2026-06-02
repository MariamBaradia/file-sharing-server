from socket import *
import os

serverPort = 6663
host = 'localhost'

totalReq = 0
sucessRes = 0
sucessDownloads = 0
failReq = 0

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(5)
print('The server is running on http://%s:%d' % (host, serverPort))

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(1024).decode()
    totalReq += 1

    try:
        print('Client IP:Port is %s:%s' % (addr[0], addr[1]))
        requestLine = request.splitlines()[0]
        path = requestLine.split()[1]
        print('Requested file/resource: %s' % path)

        if path in ['/', '/index.html', '/home_en.html', '/en'] :
            file_path = 'html/home_en.html'
        elif path in ['/ar', '/home_ar.html']:
            file_path = 'html/home_ar.html'
        elif path.startswith('/imgs/'):
            file_path = path.lstrip('/')
        elif path.startswith('/css/'):
            file_path = path.lstrip('/')
        elif path.startswith('/files/'):
            file_path = path.lstrip('/')
        else:
            file_path = 'files' + path
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            
            headers = 'HTTP/1.1 200 OK\r\n'
            if file_path.startswith('html'):
                headers += 'Content-Type: text/html\r\n'
            elif file_path.startswith('imgs'):
                if file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                    headers += 'Content-Type: image/jpeg\r\n'
                elif file_path.endswith('.png'):
                    headers += 'Content-Type: image/png\r\n'
                elif file_path.endswith('.gif'):
                    headers += 'Content-Type: image/gif\r\n'
            elif file_path.startswith('files'):
                headers += 'Content-Type: application/octet-stream\r\n'
                filename = file_path.split('/')[-1]
                headers += 'Content-Disposition: attachment; filename="%s"\r\n' % filename
                sucessDownloads += 1
            
            headers += '\r\n'
            response = headers.encode() + content
            connectionSocket.sendall(response)
            sucessRes += 1
            print("Response Status: 200 OK")
        else:
            response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html>' \
            '<head><title>404 Not Found</title></head>' \
            '<body><h1>Requested file Not Found</h1></body></html>'.encode()
            connectionSocket.sendall(response)
            failReq += 1
            print("Response Status: 404 Not Found")
    except:
        response = 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\nBad Request - Malformed HTTP Request'.encode()
        connectionSocket.sendall(response)
        failReq += 1
        print("Response Status: 400 Bad Request")
    finally:
        print('Total Requests: %d, Successful Responses: %d, Successful Downloads: %d, Failed: %d\n' % (totalReq, sucessRes, sucessDownloads, failReq))
        connectionSocket.close()

