#!/usr/bin/env python
import telnetlib
import time
from snmp_helper import snmp_get_oid,snmp_extract
snmp_port_rtr1 = '7961'
snmp_port_rtr2 = '8061'
ip_addr =  '50.76.53.27'
snmp_RO = 'galileo'
rtr1 = (ip_addr, snmp_RO, snmp_port_rtr1)
rtr2 = (ip_addr, snmp_RO, snmp_port_rtr2)

 
def main():
    OID_sysname='1.3.6.1.2.1.1.5.0'
    OID_sysdescr='1.3.6.1.2.1.1.1.0'
    rtr1_sysname = snmp_get_oid(rtr1, oid=OID_sysname)
    rtr1_sysdesc = snmp_get_oid(rtr1, oid=OID_sysdescr)
    rtr2_sysname = snmp_get_oid(rtr2, oid=OID_sysname)
    rtr2_sysdesc = snmp_get_oid(rtr2, oid=OID_sysdescr)
    o_rtr1_sn = snmp_extract(rtr1_sysname)
    o_rtr1_sd = snmp_extract(rtr1_sysdesc)
    o_rtr2_sn = snmp_extract(rtr2_sysname)
    o_rtr2_sd = snmp_extract(rtr2_sysdesc)
    print  "Router1 Name is " + o_rtr1_sn
    print  "router 1 description is " + o_rtr1_sd
    print  "router 2 Name is " + o_rtr2_sn
    print  " router 2 description is " + o_rtr2_sd
      
if __name__ == '__main__':
    main()

