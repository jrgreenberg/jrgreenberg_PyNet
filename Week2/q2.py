#!/usr/bin/env python
import telnetlib
import time
import socket
TELNET_PORT = 23
TELNET_TIMEOUT = 6

def command(remote_conn, command):
    command = command.rstrip()
    remote_conn.write(command + "\n")
    time.sleep(1)
    return  remote_conn.read_very_eager()

def main():
    ip_addr = '50.76.53.27'
    uname = 'pyclass'
    pword = '88newclass'
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("Username:", TELNET_TIMEOUT)
    remote_conn.write(uname + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(pword + '\n')
    time.sleep(2)
    output = remote_conn.read_very_eager()
    term = command(remote_conn, 'term le 0')
    output = command(remote_conn, ' show run')
    
    remote_conn.close()
    print output



if __name__ == "__main__":
    main()

