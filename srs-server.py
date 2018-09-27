#!/usr/bin/env python2
import os
import socket
import hashlib
import subprocess
import sys
import time
port = 42023
default_password_directory = "/usr/share/srs/password.auth"
class SRS_Server:
	def __init__(self):
		#initalize our object
		pass
	@classmethod
	def server(self):
		srs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		srs.bind(("", port))
		srs.listen(50)
		print("SRS Server Waiting for connection...")
		conn, address = srs.accept()
		f = open(default_password_directory, 'r').readlines()
		fl = str(f).replace("'", "")
		fll = fl.replace("[", "")
		flll = fll.replace(']', "")
		received_hash = hashlib.md5(conn.recv(65536)).hexdigest()
		print("Received Hash:",received_hash)
		print("Actual Hash:",flll)
		if str(received_hash) == str(flll):
			time.sleep(1)
			pass
		else:
			time.sleep(1)
			print("Failed Login Attempt! Shutting down SRS...")
			conn.close()
			srs.close()
			sys.exit()
			pass
		print("%s Has Connected To Us!" % str(address))
		while True:
			comm = subprocess.Popen(conn.recv(65536).decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			conn.send(b"\r\033[94m{*} Press ENTER to get the \nresults of the command...\n\033[0;0m")
			conn.send(comm.stderr.read())
			conn.send(comm.stdout.read())
			conn.send("\n\033[94m{*} Executed.")
def run():
	SRS_Server.server()
run()
