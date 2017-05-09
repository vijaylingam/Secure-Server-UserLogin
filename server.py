import socket
import random
from pyprimes import *

# Use this in case the port is already in use: sudo lsof -t -i tcp:50007 | xargs kill -9

prime = primes()
table = []

def compute_sum(line):
  return sum(int(i) for i in line.split(','))

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("Server Hosted on localhost on port:", PORT)
print("Picking two primes p and q")
x = [next(prime) for _ in range(10)]
p = random.choice(x)
q = random.choice(x)
n = p*q
print("p:", p)
print("q:", q)
print("n:", n)

a1 = random.randint(-n, n)
a2 = random.randint(-n, n)
a3 = random.randint(-n, n)

print("a1:", a1)
print("a2:", a2)
print("a3:", a3)

b1 = (a1**2)%n
b2 = (a2**2)%n
b3 = (a3**2)%n

user1 = input("Enter Login name for user1: ")
table.append([user1, [b1,n]])
user2 = input("Enter Login name for user2: ")
table.append([user2, [b2,n]])
user3 = input("Enter Login name for user3: ")
table.append([user3, [b3,n]])
print()
print("Login Details")
for row in table:
  print(row)
print()
s.listen(3)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(1024).decode('utf-8')
    if not data: break
    print("SERVER RECIEVED : ", data)
    for entry in table:
      if entry[0] == data:
        print("Valid username")
        conn.sendall(str("valid").encode('utf-8')) 
        y = conn.recv(1024).decode('utf-8') # y is of type string
        print("received y:", y)
        t = random.randint(0,1)
        print("Sending t:", str(t))
        conn.sendall(str(t).encode('utf-8'))
        z = conn.recv(1024).decode('utf-8')
        print("Received z:", str(z))
        if t == 0:
          if int(y) == (int(z)**2)%n:
            conn.sendall(str("Welcome " + data).encode('utf-8'))
            exit(0) #exit for loop   
          else:
            conn.sendall(str("Access denied").encode('utf-8'))
            exit(0) #exit for loop   
        if t == 1:
          b = 0
          for entry in table:
            if entry[0] == data:
              b = int(entry[1][0])
              # print("Entry: ", entry) #for debugging
          if (b*int(y))%n == (int(z)**2)%n:
            conn.sendall(str("Welcome "+ data).encode('utf-8'))
            exit(0) #exit for loop   
          else:
            conn.sendall(str("Access denied").encode('utf-8'))
            exit(0) #exit for loop      
    message = "Invalid Username"
    #conn.sendall(str(message).encode('utf-8'))
    print(message)
    conn.sendall(str(message).encode('utf-8'))  
    conn.close()
    #compute_sum(data)
    #conn.sendall(str(compute_sum(data)))
conn.close()