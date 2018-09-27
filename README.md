# SRS
SRS - SafeRemoteShell - Is a python tool for managing another Linux/UNIX Computer.
#How does SRS Work?
server-setup.py will ask for a new password for your SRS Server. The inputted password will be stored in /usr/bin/srs/password.auth as an MD5 Hash.
#Security
As said before, the password is an MD5 hash, so if someone accesses your PC They Can NOT See it in clear text. You can not write an SRS Password bruteforcer, since if the client  enteed the wrong password, it will first notify you, then shut down the SRS Server, but on the client side it seems like they are still connected, but no commans return anything, so they can enter any commands they want, it will not affect the Server.
#Port used
SRS uses port 42023 by default.
#Original Creator
NSK B3. NSK B3 Coded every single line by himself.
#Enjoy using SRS. Have a nice day.
