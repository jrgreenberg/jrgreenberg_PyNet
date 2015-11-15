#!/usr/bin/env python
import telnetlib
import time
import socket
telnet_port = 23
telnet_timeout = 6
def creds(telnet_port,telnet_timeout):
    ip_addr = '50.76.53.27'
    uname = 'pyclass'
    pword = '88newclass'
    remote_conn = telnetlib.Telnet(ip_addr, telnet_port, telnet_timeout)
    output = remote_conn.read_until("Username:", telnet_timeout)
    remote_conn.write(uname + '\n')
    output = remote_conn.read_until("assword:", telnet_timeout)
    remote_conn.write(pword + '\n')
    time.sleep(2)
    output = remote_conn.read_very_eager()
    remote_conn.write('term le 0 \n')
    return remote_conn

def command(connection, command):
    command = command.rstrip()
    connection.write(command + '\n')
    time.sleep(1)
    return connection.read_very_eager()


def main():
    connection = creds(telnet_port,telnet_timeout)
    ip_int_brief = command(connection, "show ip int brief")
    shrun = command(connection, "show run")
    print ip_int_brief
    print shrun
    connection.close() 
if __name__ == "__main__":
    main()

