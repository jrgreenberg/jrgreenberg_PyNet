#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
import os
os.system('clear')
cisco_cfg = CiscoConfParse("cisco.txt")
crypto_PFS2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")
for c in crypto_PFS2:
    print c.text
    print "\n"
