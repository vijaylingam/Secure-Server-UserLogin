# Client 1


import socket

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

user = input("Username: ")
s.sendall(user.encode('utf-8'))
rec = s.recv(1024).decode('utf-8')
print(rec)
if(rec == "Invalid Username"):
    exit(1)
else:    
    x = int(input("Enter the value for x: "))
    n = int(input("Enter the value of n: "))
    y = (x**2)%n
    print("Sending y:",y," to the server.")
    s.sendall(str(y).encode('utf-8'))
    rec = s.recv(1024).decode('utf-8')
    print("RECEIVED t: ", rec)

    if rec == '0':
        z = x
        print("Sending Z:", z, " to server")
        s.sendall(str(z).encode('utf-8'))
        rec = s.recv(1024)
        print(str(rec.decode('utf-8')))
    if (rec == '1'):
        a1 = int(input("Enter the value of a: "))
        z = a1*x
        s.sendall(str(z).encode('utf-8'))
        rec = s.recv(1024)
        print(str(rec.decode('utf-8')))

    s.close()