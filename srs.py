#!/usr/bin/env python2
import os
import socket
import time
import sys
try:
	host = str(sys.argv[1])
	port = 42023
except Exception as e:
	print("Please Specify a remote host!\nUsage:srs <host>")
	sys.exit()
class SafeRemoteShell:
	def __init__(self):
		#initalize our SRS Object
		pass
	@classmethod
	def remote_session(self):
	                print("Remote Session Open.")
        	        while True:
                	        command = raw_input("%s: " % str(host))
                        	srs.send(command)
				print(srs.recv(65536))
	@classmethod
	def send_password(self):
		global srs
		srs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Attempting Connection...")
		try:
			srs.connect((host, port))
		except Exception as e:
			print("Error while establishing connection to %s\nError: %s" % (host, str(e)))
			sys.exit()
		password = raw_input("Enter Password For %s: " % host)
		srs.send(password)
def run():
	print("""
Welcome To SRS - SafeRemoteShell
""")
	SafeRemoteShell.send_password()
	SafeRemoteShell.remote_session()
run()
