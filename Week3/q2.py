#!/usr/bin/env python
import snmp_helper
from  datetime import datetime
import time
import pygal
device_IP = '50.76.53.27'
user= 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (user, auth_key, encrypt_key)
pynet_rtr2 = (device_IP, 8061)
pynet_rtr1 = (device_IP,7961)
OIDs = [
('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5'),
]
inbytes=[]
outbytes=[]
inpkts=[]
outpkts=[]
def main():
    run_time = 0
    while run_time <= 12: 
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=OIDs[1][1])
        inbytes.append(int(snmp_helper.snmp_extract(snmp_data)))
    
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=OIDs[2][1])
        inpkts.append(int(snmp_helper.snmp_extract(snmp_data)))
                
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=OIDs[3][1])
        outbytes.append(int(snmp_helper.snmp_extract(snmp_data)))
    
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=OIDs[4][1])
        outpkts.append(int(snmp_helper.snmp_extract(snmp_data)))
        run_time = run_time + 1
        time.sleep(300)
    line_chart = pygal.Line()
    line_chart.title = 'input/output bytes'
    line_chart.x_labels = ['5','10','15','20','25','30','35','40','45','50','55','60']
    line_chart.add('Inbytes',inbytes)
    line_chart.add('Outbytes',outbytes)
    line_chart.add('InPackets',inpkts)
    line_chart.add('Outpackets',outpkts)
    line_chart.render_to_file('interfacechart.svg')   

if __name__ == '__main__':
    main()
