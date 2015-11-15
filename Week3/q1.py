#!/usr/bin/env python
import pickle
import pysnmp
import snmp_helper
device_IP = '50.76.53.27'
user= 'pynsmp'
auth_key = 'ga;ileo1'
encrypt_key = 'ga;ileo1'
snmp_user = (user, auth_key, encrypt_key)
pynet_rtr2 = (device_IP, 8061)



def main():
  snmp_data = snmp.helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, '1.3.6.1.4.1.9.9.43.1.1.1.0'
  print snmp_data  

if __name__ = "__main__"
    main()

