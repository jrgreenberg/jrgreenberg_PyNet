#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
import os
os.system('clear')
cisco_cfg = CiscoConfParse("cisco.txt")
crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")
for c in crypto:
    print c.text
    print "-" * 20
    child_out = c.children
    for cc in child_out:
        print cc.text
    print "\n"
