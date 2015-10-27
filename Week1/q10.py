#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
import os
os.system('clear')
cisco_cfg = CiscoConfParse("cisco.txt")
crypto_PFS2 = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")
for c in crypto_PFS2:
    print c.text
    print (c.children[1]).text
    print "\n"
