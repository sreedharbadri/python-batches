#!/usr/bin/python
import socket,sys

# creating a socket

try:
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,error:
  print 'Failed to create a socket. Error Code: ' + str(error[0]) + ' , Error message :' + str(error[1])
  sys.exit()

print 'socket created'

host = 'www.icicibank.com'
port = 80 

try:
  remote_ip = socket.gethostbyname( host )
except:
  print 'Hostname could not be resolved.exiting'
  sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip

print "connecting to the server \n"

s.connect((remote_ip,port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip
  
# sending a data outside
#message = raw_input("enter the message you want to pass on: \n")
message= "GET / HTTP/1.1\r\n\r\n"

try:
  s.sendall(message)
except socket.error:
  print 'send failed'
  sys.exit()

print 'Message sending succesfully'

# receiving the data from system.
reply = s.recv(4096)

print reply
