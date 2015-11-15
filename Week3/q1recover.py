#!/usr/bin/env python
import pickle
import pysnmp
import snmp_helper
import time
import email_helper
device_IP = '50.76.53.27'
user= 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (user, auth_key, encrypt_key)
pynet_rtr2 = (device_IP, 8061)
snmp_oids = {
    ('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0'),
    ('ccmHistoryRunningLastSaved' , '1.3.6.1.4.1.9.9.43.1.1.2.0'),
    ('ccmHistoryStartupLastChanged', '1.3.6.1.4.1.9.9.43.1.1.3.0'),
}

def email(message):
    recepient = 'jon.r.greenberg@gmail.com'
    subject = 'configuration has changed'
    sender = 'jon.r.greenberg@gmail.com'
    email_helper.send_mail(recepient,subject,message,sender)     
    return()
def main():
#    snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, '1.3.6.1.4.1.9.9.43.1.1.1.0')
  changed = 5
  while changed != 1: 
    try:
        rf = open("snmp_data.pkl","rb")
        last_changed = pickle.load(rf)
        last_saved = pickle.load(rf)
        start_changed = pickle.load(rf)
        rf.close() 
    except:
        last_changed = '999999999999999999'
        last_saved = '999999999999999999999'
        start_changed = '999999999999999999'
    f = open("snmp_data.pkl","wb")
    for oid_name,the_oid in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=the_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print oid_name + " :" + output  
        pickle.dump(output,f)
    f.close()
    rf = open("snmp_data.pkl","rb")
    compare_lc = pickle.load(rf)
    if last_changed !='999999999999999999':
        if last_changed != compare_lc:
            message = 'configuration has changed at' + compare_lc
            print "configuration has changed"
            email(message)
            changed = 1
            
        else: 
            print "configuration has not changed"
            changed = 0
    else:
        print "no data yet"
        changed = 2
    time.sleep(20)
if __name__ == "__main__":
    main()

