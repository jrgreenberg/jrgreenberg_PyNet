#!/usr/bin/env python
import yaml
import json
# create list
list1 = range(10)
list1.append('hello world')
list1.append( 'this is fun')
list1.append({'IP Address': '5.5.5.5'})
list1.append({'numbers': range(20)})

# export list to YAML
with open("q6yaml.yml", "w") as f:
    f.write("-" * 3)
    f.write("\n")
    f.write(yaml.dump(list1,default_flow_style=False))
# export list to JSON

with open("q6json.json","w") as f:
    json.dump(list1,f)

#print type(list1)
#print len(list1)
#print list1
