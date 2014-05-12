#!/usr/bin/python

###############################################################################
# The MIT License (MIT)

# Copyright (c) 2014 U Uday Krishna Sarma

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#################################################################################

import thread
import os
import time
import commands


proxy = ['10.3.100.209:8080',
	 '10.3.100.212:8080',
	 '10.3.100.210:8080',
	 '10.3.100.211:8080',
	 '144.16.192.245:8080',
	 '144.16.192.247:8080',
	 '144.16.192.216:8080']

ignoreList = "['localhost',  '127.0.0.1', 'hosts', '10.*' ]"

# Find curl on system

p = commands.getstatusoutput('curl -V')
if (p[1] == 'sh: 1: curl: not found' ):
	print "install curl and re-run"
	print "to install curl, use: sudo apt-get install curl"
	exit()

x = []

# Function to curl header of google 

def pr( threadName, proxy):
	s=commands.getstatusoutput('curl -s -w %{time_connect}:%{time_starttransfer}:%{time_total} curl -x http://'+proxy+' -I http://www.google.com')
	if (s[0] == 0):
		x.append(proxy)
	
# Create threads as follows

for i in proxy:
	try:
   		thread.start_new_thread( pr, ("Thread-1", i, ) )
	except:
   		print "Error: unable to start thread"

time.sleep(2) 

if (len(x) == 0):
	print "None of the proxies are running."
	exit()

print "In order of fastest"

for i in x:
	print (str(x.index(i)+1)+". "+i)


var = raw_input("Enter index of proxy: ")



if ( int(var) > len(x) or  int(var) < 1):
	print "Please go fornicate yourself!"
else:

# Set proxies

	os.system('gsettings set org.gnome.system.proxy mode manual')
	os.system('gsettings set org.gnome.system.proxy.http enabled true')

# If you have user authentication pass and id

	#os.system('gsettings set org.gnome.system.proxy.http authentication-user user_id')
	#os.system('gsettings set org.gnome.system.proxy.http authentication-password password')

	os.system('gsettings set org.gnome.system.proxy.http host '+x[int(var) - 1].split(':')[0])
	os.system('gsettings set org.gnome.system.proxy.http port 8080')
	os.system('gsettings set org.gnome.system.proxy.https host '+x[int(var) - 1].split(':')[0])
	os.system('gsettings set org.gnome.system.proxy.https port 8080')
	os.system('gsettings set org.gnome.system.proxy.ftp host '+x[int(var) - 1].split(':')[0])
	os.system('gsettings set org.gnome.system.proxy.ftp port 8080')

# ignoreList

	os.system('gsettings set org.gnome.system.proxy ignore-hosts "'+ignoreList+'"')

	print str(x[int(var) - 1].split(':')[0])+":8080 has been set as your system proxy"
	print "credits : uuksarma@gmail.com, 001.amby@gmail.com"


