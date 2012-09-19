import sys
import socket
import string
import os
import time
import random
from settings import *
from functions import *
    
def connect_to_server():
    s = socket.socket() # Create the socket
    s.connect((HOST, PORT)) # Connect to server 
    s.send('NICK ' + NICK + '\r\n') # Send the nick to server
    s.send('USER '+ IDENT + ' ' + HOST + ' bla :' + REALNAME + '\r\n') # Identify to server
    return s

def close_connection(socket):
    socket.close()

if __name__ == "__main__":
    s = connect_to_server()
    while 1:
        line = s.recv(4096) # Recieve server messages
        #print line # Server message is output
        if line.find("Welcome to the Internet Relay Network") != -1:
            s.send('JOIN '+ CHANNELINIT + ' ' + CHANNELPASS + '\r\n') # Join a channel
            JOINED = True
            s.send('PRIVMSG ' + CHANNELINIT + ' :' + JOINMSG + '\r\n')
        if line.find('PRIVMSG') != -1: # Call a parsing function 
            parsemsg(s, line)
            #line = line.rstrip() #remove trailing 'rn'
        if line.find("JOIN") != -1:
            auto_op(s, line)
        if(line.find("PING", 0, 4) != -1): # If server pings then pong
            s.send('PONG ' + HOST + '\r\n')
            #print "I PONG TO GET SOME PING"