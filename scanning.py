#!/usr/bin/python2

import  time 
import  commands
#  first  check your own ip 
'''
search any library that will work for network related things 
try to learn  REGEX in python to match  x.x.x.x  pattern 
module name is  re 
'''
print  commands.getoutput("tcpdump  -D  |   grep  -vE 'usb|nf|any'  |  cut -d.  -f2 | grep -E '^e|^w'")
print  "                                                          "
print  "__________________________________________________________"
print  "__________________________________________________________"
print  "__________________________________________________________"

nic=raw_input("type NIC name from above list  to check related IP :  ")

output=commands.getoutput('ifconfig  '+nic)

print  "finding IP plz wait .."
time.sleep(2)

myip=output.split()[5]
print  myip
print  "               "
print  "  Going back to startup programe             "
time.sleep(2)
execfile('start.py')
