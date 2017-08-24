import ftplib
import os
import socket


HOST = '[ftp site url]'
DIRN = '/'
filematch = '*.xml'
username = '[ftp username]'
password = '[ftp password]'
storetodir = '[C:\\Users\\...]'

#Open ftp connection
ftp = ftplib.FTP(HOST, username, password)


#List the files in the current directory
print "File List:"
files = ftp.dir()
print files

#List the xml files in the current directory
ftp.cwd(DIRN)

currdir = os.getcwd()

os.chdir(storetodir)
s= 0;

for filename in ftp.nlst(filematch):
    fhandle = open(filename,'wb')
    print 'Getting ' + filename + '...'
    ftp.retrbinary('RETR ' + filename, fhandle.write)
    s = s + 1

print 'File Transfer Completed!'
