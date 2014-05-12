#!/usr/bin/python

###############################################################################
# The MIT License (MIT)
# Refer to README.md
# Credits : uuksarma@gmail.com, 001.amby@gmail.com
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

Version = '0.2'

# Find curl on system

p = commands.getstatusoutput('curl -V')
if (p[1] == 'sh: 1: curl: not found' ):
	print "install curl and re-run"
	print "to install curl, use: sudo apt-get install curl"
	exit()

x = []

# Convert string to int

def convertToInt(s):
	try:
		ret = int(s)
	except ValueError:
		print "re-run and enter an index of listed proxies"
		exit()
		
	return ret
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


var = raw_input("Press ENTER to set fastest proxy \nor Enter index of proxy: ")

if (len(var) == 0) :
	var = '1'


var1 = convertToInt(var)

if ( var1 >= 1 and var1 <= len(x) ):
	#print var1
# Set proxies
	proxyAddress = x[var1 - 1].split(':')[0]
	proxyPort = x[var1 - 1].split(':')[1]
	os.system('gsettings set org.gnome.system.proxy mode manual')
	os.system('gsettings set org.gnome.system.proxy.http enabled true')

# If you have user authentication pass and id

	#os.system('gsettings set org.gnome.system.proxy.http authentication-user user_id')
	#os.system('gsettings set org.gnome.system.proxy.http authentication-password password')

	os.system('gsettings set org.gnome.system.proxy.http host '+proxyAddress)
	os.system('gsettings set org.gnome.system.proxy.http port '+proxyPort)
	os.system('gsettings set org.gnome.system.proxy.https host '+proxyAddress)
	os.system('gsettings set org.gnome.system.proxy.https port '+proxyPort)
	os.system('gsettings set org.gnome.system.proxy.ftp host '+proxyAddress)
	os.system('gsettings set org.gnome.system.proxy.ftp port '+proxyPort)

# ignoreList

	os.system('gsettings set org.gnome.system.proxy ignore-hosts "'+ignoreList+'"')

	print str(x[var1 - 1])+" has been set as your system proxy"
	#print "credits : uuksarma@gmail.com, 001.amby@gmail.com"

else:
	print "re-run and enter an index of listed proxies"


	


