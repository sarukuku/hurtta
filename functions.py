import sys
import socket
import string
import os
import time
import random
import re
import urllib2
import json
from settings import *

def parsemsg(s, msg):
    complete = msg[1:].split(':', 1) # Parse the message into useful data 
    info = complete[0].split(' ') 
    msgpart = complete[1] 
    sender = info[0].split('!')
    chan = info[2]
    save_url(s, chan, msg)
    if msgpart[0] == COMMAND and sender[1] in OWNER:
        cmd = msgpart[1:].split(' ')
        if cmd[0].rstrip() == 'quit':
            s.send("QUIT :" + QUITMSG + "\r\n")
            exit()
        elif cmd[0] == 'op': 
            s.send('MODE ' + info[2] + ' +o ' + cmd[1] + '\r\n')
        elif cmd[0] == 'deop': 
            s.send('MODE ' + info[2] + ' -o ' + cmd[1] + '\r\n')
        elif cmd[0] == 'voice': 
            s.send('MODE ' + info[2] + ' +v ' + cmd[1] + '\r\n')
        elif cmd[0] == 'devoice': 
            s.send('MODE ' + info[2] + ' -v ' + cmd[1] + '\r\n')
        elif cmd[0] == 'say':
            s.send('PRIVMSG ' + chan + ' :' + string.join(cmd[1:]," ") + '\r\n' )
        elif cmd[0].rstrip() == 'joke':
            s.send('PRIVMSG ' + chan + ' :' + get_joke() + '\r\n' )
        else:
        	s.send('PRIVMSG ' + chan + ' :' + UNKNOWNCOMMANDMSG + '\r\n' )

def auto_op(s, msg):
    info = msg.split('!')
    nick = info[0].split(':')[1].rstrip()
    info = info[1].split(' ')
    chan = info[2].split(':')[1].rstrip()
    if info[0] in OWNER:
        #print 'MODE ' + chan + ' +o ' + nick + '\r\n'
        s.send('MODE ' + chan + ' +o ' + nick + '\r\n')

def save_url(s, chan, msg):
        for x in URLREGEXPS:
            if x.search(msg) != None:
                f = open('logs/urls.log', 'a')
                f.write(x.search(msg).group(0) + '\r\n')
                s.send('PRIVMSG ' + chan + ' :' + URLSAVEDMSG + '\r\n' )
                break

def get_joke():
    req = urllib2.Request("http://api.icndb.com/jokes/random")
    opener = urllib2.build_opener()
    f = opener.open(req)
    obj = json.load(f)
    if obj['type'] == 'success':
        obj = string.replace(obj['value']['joke'], '&quot;', '\"')
        return obj
    else:
        return JOKEFAILMSG