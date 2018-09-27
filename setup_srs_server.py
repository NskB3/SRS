#!/usr/bin/env python
import os
import hashlib
print """

SRS Server Setup

----------------
SafeRemoteShell (SRS) is a simple python project
For safe remote shell access of computers.
SRS Servers are very very difficult to hack (more difficult than SSH)
So your PC Is protected.

"""
print "\nCreating Directories..."
os.system("mkdir /usr/share/srs/")
f = open("/usr/share/srs/password.auth", "wb")
password = raw_input("Specify a password for your server: ")
print "Hashing password.."
HASHED_PASS = hashlib.md5(password).hexdigest()
f.write(HASHED_PASS)
print "Setup DONE!"
